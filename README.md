## Software and Platform 

- **Software**: Google Colab
- **Add-on package**: Pandas, NumPy, TensorFlow, Matplotlib, Seaborn, Scikit-Learn
- **Platform**: Mac

## Documentation Map 

- **Data Folder** Contains all data
  - _Beagle_: Folder containing all images classified as the Beagle dog breed.
  - _Boxer_: Folder containing all images classified as the Boxer dog breed.
  - _Bulldog_: Folder containing all images classified as the Bulldog dog breed.
  - _Chihuahua_: Folder containing all images classified as the Chihuahua dog breed.
  - _Chow_: Folder containing all images classified as the Chow dog breed.
  - _CockerSpaniel_: Folder containing all images classified as the Cocker Spaniel dog breed.
  - _Doberman_: Folder containing all images classified as the Doberman dog breed.
  - _GermanShepherd_: Folder containing all images classified as the German Shepherd dog breed.
  - _Golden_: Folder containing all images classified as the Golden Retriever dog breed.
  - _GreatDane_: Folder containing all images classified as the Great Dane dog breed.
  - _Husky_: Folder containing all images classified as the Husky dog breed.
  - _Lab_: Folder containing all images classified as the Labrador Retriever dog breed.
  - _Pomeranian_: Folder containing all images classified as the Pomeranian dog breed.
  - _Pug_: Folder containing all images classified as the Pug dog breed.
  - _Rottweiler_: Folder containing all images classified as the Rottweiler dog breed.
  - _SaintBernard_: Folder containing all images classified as the Saint Bernard dog breed.
  - _Shih-tzu_: Folder containing all images classified as the Shih Tzu dog breed.
  - _StandardPoodle_: Folder containing all images classified as the Standard Poodle dog breed.
  - _StandardSchnauzer_: Folder containing all images classified as the Standard Schnauzer dog breed.
  - _Whippet_: Folder containing all images classified as the Whippet dog breed.
  - `Data Appendix Project 3.pdf`: Description of the data used 
- **Scripts Folder**: Contains all source code and scripts
  - `DataAppendix.ipynb`: Used to create `Data Appendix Project 3.pdf`
  - `Project3MI2EDA.ipynb`: Exploratory data analysis on the image data
  - `Project3MI3Analysis.ipynb`: Prediction analysis using the image data based on train and validation set
  - `rename_files.py`: Used to rename the image files for easy reference
- **Output Folder**: Contains output generated by analysis
  - MI2_EDA: Folder containing pertinent figures from EDA
    - `Distribution of Image Widths and Heights.png`
    - `Distribution of Pixel Intensities.png`
    - `Dog Breed Distribution.png`
  - MI3: Folder containing pertinent figures from analysis
    - `Confusion Matrix of Dog Breed Predictions.png`

## Reproduction Information 
1. **Data Gathering**: We got our data from the Stanford Dogs dataset - [Stanford Dogs Dataset] (http://vision.stanford.edu/aditya86/ImageNetDogs/). We selected 20 dog breeds to conduct prediction analysis on - these 20 breeds are found in various folders in the _Data Folder_.
2. **Data Cleaning**: Running the `rename_files.py` script renames the images in the dog breed folders to their corresponding breed, followed by a numerical value. This is done to ease the analysis process.
3. **Exploratory Data Analysis**: To explore the data and gather initial insights to refine the analysis plan, run the `Project3MI2EDA.ipynb` script under the _Scripts Folder_.
4. **Analysis**: To conduct analysis on the data, there is one main file to run: `Project3MI3Analysis.ipynb`. You can find it in the _Scripts Folder_. 

## References 
[1] A. Khosla, N. Jayadevaprakash, B. Yao, and L. Fei-Fei, “Stanford Dogs Dataset,” Stanford dogs dataset for fine-grained visual categorization, http://vision.stanford.edu/aditya86/ImageNetDogs/ (accessed Nov. 4, 2024). 
