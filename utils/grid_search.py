import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.model_selection import GridSearchCV
import gensim
from gensim.models import CoherenceModel
from gensim.corpora.dictionary import Dictionary

def grid_search(df_final):
    # Separar o DataFrame em conjuntos de treino e teste
    train_df = df_final.sample(frac=0.7, random_state=42)
    test_df = df_final.drop(train_df.index)

    print(f"Contagem df treino: {len(train_df)}")
    print(f"Contagem df teste: {len(test_df)}")

    train_texts = train_df['normalizado'].tolist()
    test_texts = test_df['normalizado'].tolist()

    vectorizer = TfidfVectorizer()
    train_matrix = vectorizer.fit_transform(train_texts)
    test_matrix = vectorizer.transform(test_texts)

    print(f"Matrix de treino e testes criadas!")

    # Definição do grid de parametros para grid search
    param_grid = {
    'n_components': [5, 8],
    'learning_decay': [0.3, 0.5],
    'learning_method': ['batch'],
    'max_iter': [5, 10],
    'doc_topic_prior': [0.1, 0.5],
    'topic_word_prior': [0.01, 0.1]
    }   

    # Crição do LDA object
    lda = LatentDirichletAllocation(random_state=42)

    # Set up do grid search
    grid_search = GridSearchCV(lda, param_grid=param_grid, cv=2, n_jobs=1, verbose=2)

    # Fit do grid search na matrix de treino
    grid_search.fit(train_matrix)

    # Retorno do best parameters e modelo
    best_params = grid_search.best_params_
    best_lda_model = grid_search.best_estimator_

    print(f"Best Parameters: {best_params}")

    # Transform the test matrix usando o melhor modelo LDA
    lda_matrix_test = best_lda_model.transform(test_matrix)

    print(f"Teste completo!")

    # Obtém os termos de cada tópico
    terms = vectorizer.get_feature_names_out()

    topics = []
    top_terms_dict = {}
    for idx, topic in enumerate(best_lda_model.components_):
        top_terms = [terms[i] for i in topic.argsort()[-10:]]
        topics.append((f"Topic {idx + 1}", ", ".join(top_terms)))
        top_terms_dict[idx] = ", ".join(top_terms)

    # Criação df com os tópicos
    df_topics = pd.DataFrame(topics, columns=["Topic", "Top Terms"])

    print(f"Tópicos gerados!")

    # Teste de perplexidade
    perplexity = best_lda_model.perplexity(test_matrix)
    print(f'Perplexity: {perplexity}')
 
    # Prepara o dado para coherence model
    texts = [doc.split() for doc in test_texts]
    dictionary = Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    # Fit do modelo LDA usando gensim
    lda_model = gensim.models.LdaModel(corpus, num_topics=best_params['n_components'], id2word=dictionary, passes=4)

    # Cálculo coherence score
    coherence_model_lda = CoherenceModel(model=lda_model, texts=texts, dictionary=dictionary, coherence='c_v')
    coherence_score = coherence_model_lda.get_coherence()
    print(f'Coherence Score: {coherence_score}')

    # Atribue os tópicos para o df original
    df_final['Topic'] = best_lda_model.transform(vectorizer.transform(df_final['normalizado'].tolist())).argmax(axis=1)
    df_final['Top Terms'] = df_final['Topic'].map(top_terms_dict)

    return df_topics, df_final
