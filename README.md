# NBAC - Naive Bayes Ads Classifier
Suppose a big player in the classifieds market that have millions of ads in their database and thousands of new ads per day have a big challenge: How can it suggest the category for a new ad?

NBAC will categorize a list of documents by using a [Naive Bayes classifier][1] that takes the most common words in a list of ads already known.

***Note***: NBAC works with Portuguese text ads and it is based on [Mustafa Atik et al. project][2].

## How to classify the ads?
Basically, we will have a training dataset and a test dataset;  
These datasets should be extracted from files in the input folder;  
Each file contains a list with thousands ads;  
Each file represents a known ad category, e.g. '3060.json' means the ad category '3060';  
Each file row must have the following fields in JSON format:  
- category: the ad category
- subject: the ad subject
- body: the ad description

E.g.: JSON file of Smartphone category:
```json
[{"category":"3060","subject":"Moto G 16gb 2 chips 4g","body":"Moto G 2 geração 16gb 2 chips 4g, Android 6.0 marshmelow, entrada para cartão de memória externa, funcionando perfeitamente!! Aparelhos em excelente estado, sem marcas de uso ou riscos, impecável!! Usado pouquíssimas vezes, quase novo!"},
{"category":"3060","subject":"IPhone 5s 16gb Space Gray","body":"aparelho em bom estado, com película de vidro e todos acessórios. funcionando tudo perfeitamente, desbloqueado e iCloud liberado. Anatel 4G. avista: 1150,00 na troca: 1250,00 aceito cartões visa e master em até 6x com acréscimo."},
{"category":"3060","subject":"Samsung Galaxy S6 32GB","body":"Samsung Galaxy S6 32GB 4G Câm. 16MP + Selfie 5MP Tela 5.1 Proc. Octa Core. O Samsung Galaxy S6 é feito de vidro tanto na parte traseira quanto frontal, e rodeado por uma moldura de alumínio que olha, é um luxo!"}]
```
NBAC will load the ads, split them into training and test datasets and, finally, train and classify them.

## Usage
You can run this classifier using the following ```python``` command:
```python
# Usage: python nbac.py <training-set-limit>
# Suppose you have 10K ads from each file and you want to train with 9K to classify 1K:
python nbac.py 9000
# You may also set a percentage (.9 -> 90%) for the training dataset:
python nbac.py .9
```
***Note***: You must have at least one file in the input folder and the classification result will be saved in the output folder.

## TODO
* Exception handling;
* Implement other languages tokenizers;
* Run NBAC with multiple categories on single file;
* Save the classification result in JSON format.

## Author

* **Marcus Machado**   -   marcus.machado@ppgi.ufrj.br

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


  [1]: https://en.wikipedia.org/wiki/Naive_Bayes_classifier
  [2]: https://github.com/muatik/naive-bayes-classifier
