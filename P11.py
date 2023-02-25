{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPBu8FwF/T+2PTswhBrNiTO",
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
        "<a href=\"https://colab.research.google.com/github/K-Mehri-2022/AP/blob/main/P11.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "hchAdhkEHOFr"
      },
      "outputs": [],
      "source": [
        "# Library for defining square delta\n",
        "import math\n",
        "\n",
        "# Get the three values for Coefficients from the user \n",
        "a = int(input(\"Enter fist value: \"))\n",
        "b = int(input(\"Enter second value: \"))\n",
        "c = int(input(\"Enter third value: \"))\n",
        "\n",
        "# Formula for the delta of three roots\n",
        "delta = (b * b) - (4 * a * c)\n",
        " \n",
        "# Using the conditional if structure to calculate and print the roots\n",
        "# Two roots\n",
        "if(delta > 0):\n",
        "    x1 = (-b + math.sqrt(delta))/(2*a)\n",
        "    x2 = (-b - math.sqrt(delta))/(2*a)\n",
        "   print(\"x1 = \",x1,\"\\n\",\"x2 = \",x2)\n",
        "# One root\n",
        "if(delta ==0):\n",
        "    x1 = (-b) / (2*a)\n",
        "    print(\"x1 = \",x1)\n",
        "\n",
        "# Without any root\n",
        "if(delta < 0):\n",
        "    print(\"Undefined.\")\n",
        "\n"
      ]
    }
  ]
}