# Interactive AEPsych

With the help of Voila and Binder, you can now
conduct experiments with interactive widgets.

To start or resume an experiment launch the interactive dashboard.

https://mybinder.org/v2/gh/Eric-Cortez/voila/HEAD?urlpath=voila%2Frender%2Fnotebooks%2FAEPsych_dashboard.ipynb
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Eric-Cortez/voila/HEAD?urlpath=voila%2Frender%2Fnotebooks%2FAEPsych_dashboard.ipynb)

Requirements: python 3.8+ and anaconda

Note: These steps are to install and run a jupyter notebook locally
rather than launching Binder as stated above.

We recommend installing Interactive AEPsych under a virtual
environment like Anaconda. Once you've created a virtual environment
for Interactive AEPsych and activated it, you can install the requirements
using pip:

```bash
git clone https://<<---add--->>
cd <<---add--->>
pip install -r requirements.txt
```


### Activate virtual environment

```bash
source bin/activate
conda activate
jupyter notebook
```
### Deactivate virtual environment
```bash
deactivate
conda deactivate
```

### Voila

Use the following command to run voila locally

```bash
voila <filename>.ipyn
```
