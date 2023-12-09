from sklearn.model_selection import train_test_split

class PreProcessor:

    def pre_processor(self, dataset, percentual_test, seed=7):
        """ Cuida de todo o pré-processamento. """
        # limpeza dos dados e eliminação de outliers
        

        # divisão em treino e teste
        X_train, X_test, Y_train, Y_test = self.__prepar_holdout(dataset,
                                                                  percentual_test,
                                                                  seed)
        # normalização/padronização
        
        return (X_train, X_test, Y_train, Y_test)
    
    def __prepar_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        data = dataset.values
        X = data[:, 0:-1]
        Y = data[:, -1]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)