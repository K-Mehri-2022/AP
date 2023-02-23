{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMKTGsZYo7jVzhsuS+8B70U",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/K-Mehri-2022/AP/blob/main/P01.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dgCUyJrBIxwa",
        "outputId": "ef2c7a20-17cf-4be1-fc95-f14bf8088089"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter number 1 : 24\n",
            "Enter number 2 : 12\n",
            "GCD is  12\n"
          ]
        }
      ],
      "source": [
        "# GCD \n",
        "n = int(input(\"Enter number 1 : \"))\n",
        "m = int(input(\"Enter number 2 : \"))\n",
        "temp = 1\n",
        "while m != 0 :\n",
        "  temp = n%m\n",
        "  n = m\n",
        "  m = temp \n",
        "print(\"GCD is \", n)"
      ]
    }
  ]
}