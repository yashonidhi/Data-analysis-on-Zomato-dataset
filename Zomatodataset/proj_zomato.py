{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "56192fe8",
   "metadata": {},
   "outputs": [],
   "source": [
    "##EDA on zomato dataset "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bede4c37",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pandas'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Input \u001b[0;32mIn [7]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmatplotlib\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpyplot\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mplt\u001b[39;00m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pandas'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline \n",
    "#%matplotlib inline helps display visuals right below the code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "edfb650e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [6]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m df\u001b[38;5;241m=\u001b[39m\u001b[43mpd\u001b[49m\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mzomato.csv\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "df=pd.read_csv('zomato.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc8f3fdb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
