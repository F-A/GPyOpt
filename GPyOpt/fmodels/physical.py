class PhysicalExperiment: 
    def __init__(self):
 
    def PhysicalExperiment(X):
        n, p = X.shape   
        if n==1:
            print 'Experimental conditions:'
            print X
            feval = input('Insert here experimental value:')
            output =np.array([[feval]])
        else:
            output = np.zeros(n).T    
            print 'Batch of %s samples is requiered:' %n
            print '---------------------------------'
            for k in range(n):
            print 'Experimental conditions for sample %s:' %k+1
            print X[k,]
            output[k] = input('Insert experimental value:')
        return output