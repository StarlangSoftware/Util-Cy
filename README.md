For Developers
============
You can also see [Python](https://github.com/starlangsoftware/Util-Py), [Java](https://github.com/starlangsoftware/Util), [C++](https://github.com/starlangsoftware/Util-CPP), [C](https://github.com/starlangsoftware/Util-C), [Swift](https://github.com/starlangsoftware/Util-Swift), [Js](https://github.com/starlangsoftware/Util-Js), or [C#](https://github.com/starlangsoftware/Util-CS) repository.

## Requirements

* [Python 3.9 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3.9 install NlpToolkit-Util-Cy

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called Util will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/Util-Cy.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `Util-Cy` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [Interval](#interval)
+ [Subset](#subset)
+ [SubsetFromList](#subsetfromlist)
+ [Permutation](#permutation)

## Interval 

Aralık veri yapısını tutmak için Interval sınıfı

	a = Interval()

1 ve 4 aralığı eklemek için

	a.add(1, 4)

i. aralığın başını getirmek için (yukarıdaki örnekteki 1 gibi)

	getFirst(self, index: int) -> int

i. aralığın sonunu getirmek için (yukarıdaki örnekteki 4 gibi)

	getLast(self, index: int) -> int

## Subset 

Altküme tanımlamak ve tüm altkümelere ulaşmak için Subset ve SubsetFromList sınıfları

Subset veri yapısını tanımlamak için

	Subset(self, rangeStart: int, rangeEnd: int, elementCount: int)

Burada elemenCount elemanlı, elemanları rangeStart ile rangeEnd arasında değerler alabilen
tüm altkümeleri gezen bir yapıdan bahsediyoruz. Örneğin

Subset(1, 4, 2), bize iki elemanlı elemanlarını 1 ile 4 arasından gelen tüm alt kümeleri 
seçmek için kullanılan bir constructor'dır. Tüm altkümeleri elde etmek için

	a = Subset(1, 4, 2);
	subset = a.get()
	while a.next():
		subset = a.get()
		....

Burada subset sırasıyla {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4} altkümelerini gezer. 

## SubsetFromList 

Altküme tanımlamak ve tüm altkümelere ulaşmak için Subset ve SubsetFromList sınıfları

SubsetFromList veri yapısını kullanmak için

	SubsetFromList(self, _list: list, elementCount: int)

Burada elementCount elemanlı, elemanları list listesinden çekilen değerler olan ve tüm 
altkümeleri gezen bir yapıdan bahsediyoruz. Örneğin

SubsetFromList([1, 2, 3, 4], 3), bize üç elemanlı elemanlarını [1, 2, 3, 4] listesinden 
seçen ve tüm alt kümeleri gezmekte kullanılan bir constructor'dır. Tüm altkümeleri elde 
etmek için

	a = SubsetFromList([1, 2, 3, 4], 3)
	subset = a.get()
	while a.next():
		subset = a.get()
		....

Burada SubsetFromList sırasıyla {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4} altkümelerini 
gezer. 

## Permutation

Permütasyon tanımlamak ve tüm permütasyonlara ulaşmak için Permutation sınıfı

	Permutation(self, n: int)

Burada 0 ile n - 1 arasındaki değerlerin tüm olası n'li permütasyonlarını gezen bir 
yapıdan bahsediyoruz. Örneğin

Permutation(5), bize değerleri 0 ile 4 arasında olan tüm 5'li permütasyonları gezmekte 
kullanılan bir constructor'dır. Tüm permütasyonları elde etmek için

	a = Permutation(5)
	permutation = a.get()
	while a.next():
		permutation = a.get();
		...

Burada Permutation sırasıyla {0, 1, 2, 3, 4}, {0, 1, 2, 4, 3} gibi permütasyonları gezer.

For Contibutors
============

### Setup.py file
1. Do not forget to set package list. All subfolders should be added to the package list.
```
    packages=['Classification', 'Classification.Model', 'Classification.Model.DecisionTree',
              'Classification.Model.Ensemble', 'Classification.Model.NeuralNetwork',
              'Classification.Model.NonParametric', 'Classification.Model.Parametric',
              'Classification.Filter', 'Classification.DataSet', 'Classification.Instance', 'Classification.Attribute',
              'Classification.Parameter', 'Classification.Experiment',
              'Classification.Performance', 'Classification.InstanceList', 'Classification.DistanceMetric',
              'Classification.StatisticalTest', 'Classification.FeatureSelection'],
```
2. Package name should be lowercase and only may include _ character.
```
    name='nlptoolkit_math',
```
3. Package data should be defined and must ibclude pyx, pxd, c and py files.
```
    package_data={'NGram': ['*.pxd', '*.pyx', '*.c', '*.py']},
```
4. Setup should include ext_modules with compiler directives.
```
    ext_modules=cythonize(["NGram/*.pyx"],
                          compiler_directives={'language_level': "3"}),
```

### Cython files
1. Define the class variables and class methods in the pxd file.
```
cdef class DiscreteDistribution(dict):

    cdef float __sum

    cpdef addItem(self, str item)
    cpdef removeItem(self, str item)
    cpdef addDistribution(self, DiscreteDistribution distribution)
```
2. For default values in class method declarations, use *.
```
    cpdef list constructIdiomLiterals(self, FsmMorphologicalAnalyzer fsm, MorphologicalParse morphologicalParse1,
                               MetamorphicParse metaParse1, MorphologicalParse morphologicalParse2,
                               MetamorphicParse metaParse2, MorphologicalParse morphologicalParse3 = *,
                               MetamorphicParse metaParse3 = *)
```
3. Define the class name as cdef, class methods as cpdef, and \_\_init\_\_ as def.
```
cdef class DiscreteDistribution(dict):

    def __init__(self, **kwargs):
        """
        A constructor of DiscreteDistribution class which calls its super class.
        """
        super().__init__(**kwargs)
        self.__sum = 0.0

    cpdef addItem(self, str item):
```
4. Do not forget to comment each function.
```
    cpdef addItem(self, str item):
        """
        The addItem method takes a String item as an input and if this map contains a mapping for the item it puts the
        item with given value + 1, else it puts item with value of 1.

        PARAMETERS
        ----------
        item : string
            String input.
        """
```
5. Function names should follow caml case.
```
    cpdef addItem(self, str item):
```
6. Local variables should follow snake case.
```
	det = 1.0
	copy_of_matrix = copy.deepcopy(self)
```
7. Variable types should be defined for function parameters, class variables.
```
    cpdef double getValue(self, int rowNo, int colNo):
```
8. Local variables should be defined with types.
```
    cpdef sortDefinitions(self):
        cdef int i, j
        cdef str tmp
```
9. For abstract methods, use ABC package and declare them with @abstractmethod.
```
    @abstractmethod
    def train(self, train_set: list[Tensor]):
        pass
```
10. For private methods, use __ as prefix in their names.
```
    cpdef list __linearRegressionOnCountsOfCounts(self, list countsOfCounts)
```
11. For private class variables, use __ as prefix in their names.
```
cdef class NGram:
    cdef int __N
    cdef double __lambda1, __lambda2
    cdef bint __interpolated
    cdef set __vocabulary
    cdef list __probability_of_unseen
```
12. Write \_\_repr\_\_ class methods as toString methods
13. Write getter and setter class methods.
```
    cpdef int getN(self)
    cpdef setN(self, int N)
```
14. If there are multiple constructors for a class, define them as constructor1, constructor2, ..., then from the original constructor call these methods.
```
cdef class NGram:

    cpdef constructor1(self, int N, list corpus):
    cpdef constructor2(self, str fileName):
    def __init__(self,
                 NorFileName,
                 corpus=None):
        if isinstance(NorFileName, int):
            self.constructor1(NorFileName, corpus)
        else:
            self.constructor2(NorFileName)
```
15. Extend test classes from unittest and use separate unit test methods.
```
class NGramTest(unittest.TestCase):

    def test_GetCountSimple(self):
```
16. For undefined types use object as type in the type declarations.
```
cdef class WordNet:

    cdef object __syn_set_list
    cdef object __literal_list
```
17. For boolean types use bint as type in the type declarations.
```
	cdef bint is_done
```
18. Enumerated types should be used when necessary as enum classes, and should be declared in py files.
```
class AttributeType(Enum):
    """
    Continuous Attribute
    """
    CONTINUOUS = auto()
    """
```
19. Resource files should be taken from pkg_recources package.
```
	fileName = pkg_resources.resource_filename(__name__, 'data/turkish_wordnet.xml')
```
