ass Tree:
        def __init__(self, left, right, elem):
                    self.left = left
                            self.right = right
                                    self.elem = elem

                                        
                                        def print_t(tree):
                                                if tree != None:
                                                            print(tree.elem)
                                                                    print_t(tree.left)
                                                                            print_t(tree.right)

                                                                                    
                                                                                    def my_mediana(X, j):
                                                                                            if len(X)>=1:
                                                                                                        med = np.median(X, axis=0)[j]
                                                                                                                if np.shape(X)[0] % 2 == 0:
                                                                                                                                print(X[:,j])
                                                                                                                                            num = np.argsort(X[:, j] - med)[0]
                                                                                                                                                        return X[num, j]
                                                                                                                                                            return med
                                                                                                                                                                
                                                                                                                                                                
                                                                                                                                                        def kd_tree(X, i):
                                                                                                                                                                j = i % np.shape(X)[1]

                                                                                                                                                                    med = my_mediana(X, j)
                                                                                                                                                                        left = X[np.where(X[:, j] < med)]
                                                                                                                                                                            right = X[np.where(X[:, j] > med)]
                                                                                                                                                                                elem = X[np.where(X[:, j] == med)]

                                                                                                                                                                                    if len(elem) > 1:
                                                                                                                                                                                                print(left,elem[1][np.newaxis, :])
                                                                                                                                                                                                        left = np.concatenate((left, elem[1][np.newaxis, :]), axis = 0)
                                                                                                                                                                                                                elem = elem[0][np.newaxis, :]
                                                                                                                                                                                                                #     print('left = \n', left)
                                                                                                                                                                                                                #     print('right = \n', right)
                                                                                                                                                                                                                #     print('elem = \n', elem)
                                                                                                                                                                                                                #     print('\n\n\n')        

                                                                                                                                                                                                                    if len(X) > 1:        
                                                                                                                                                                                                                                return Tree(kd_tree(left, i + 1), kd_tree(right, i + 1), elem)
                                                                                                                                                                                                                                elif len(X) == 1:
                                                                                                                                                                                                                                            return Tree(None, None, elem)
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                        tree = kd_tree(X_test, 0)
                                                                                                                                                                                                                                        print_t(tree)
                                                                                                                                                                                                                                        #неожиданно я понял что KDTree не надо реализовыватьclass Tree:
                                                                                                                                                                                                                                            def __init__(self, left, right, elem):
                                                                                                                                                                                                                                                        self.left = left
                                                                                                                                                                                                                                                                self.right = right
                                                                                                                                                                                                                                                                        self.elem = elem

                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                            def print_t(tree):
                                                                                                                                                                                                                                                                                    if tree != None:
                                                                                                                                                                                                                                                                                                print(tree.elem)
                                                                                                                                                                                                                                                                                                        print_t(tree.left)
                                                                                                                                                                                                                                                                                                                print_t(tree.right)

                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                        def my_mediana(X, j):
                                                                                                                                                                                                                                                                                                                                if len(X)>=1:
                                                                                                                                                                                                                                                                                                                                            med = np.median(X, axis=0)[j]
                                                                                                                                                                                                                                                                                                                                                    if np.shape(X)[0] % 2 == 0:
                                                                                                                                                                                                                                                                                                                                                                    print(X[:,j])
                                                                                                                                                                                                                                                                                                                                                                                num = np.argsort(X[:, j] - med)[0]
                                                                                                                                                                                                                                                                                                                                                                                            return X[num, j]
                                                                                                                                                                                                                                                                                                                                                                                                return med
                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                            def kd_tree(X, i):
                                                                                                                                                                                                                                                                                                                                                                                                    j = i % np.shape(X)[1]

                                                                                                                                                                                                                                                                                                                                                                                                        med = my_mediana(X, j)
                                                                                                                                                                                                                                                                                                                                                                                                            left = X[np.where(X[:, j] < med)]
                                                                                                                                                                                                                                                                                                                                                                                                                right = X[np.where(X[:, j] > med)]
                                                                                                                                                                                                                                                                                                                                                                                                                    elem = X[np.where(X[:, j] == med)]

                                                                                                                                                                                                                                                                                                                                                                                                                        if len(elem) > 1:
                                                                                                                                                                                                                                                                                                                                                                                                                                    print(left,elem[1][np.newaxis, :])
                                                                                                                                                                                                                                                                                                                                                                                                                                            left = np.concatenate((left, elem[1][np.newaxis, :]), axis = 0)
                                                                                                                                                                                                                                                                                                                                                                                                                                                    elem = elem[0][np.newaxis, :]
                                                                                                                                                                                                                                                                                                                                                                                                                                                    #     print('left = \n', left)
                                                                                                                                                                                                                                                                                                                                                                                                                                                    #     print('right = \n', right)
                                                                                                                                                                                                                                                                                                                                                                                                                                                    #     print('elem = \n', elem)
                                                                                                                                                                                                                                                                                                                                                                                                                                                    #     print('\n\n\n')        

                                                                                                                                                                                                                                                                                                                                                                                                                                                        if len(X) > 1:        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    return Tree(kd_tree(left, i + 1), kd_tree(right, i + 1), elem)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    elif len(X) == 1:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                return Tree(None, None, elem)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            tree = kd_tree(X_test, 0)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            print_t(tree)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #неожиданно я понял что KDTree не надо реализовывать