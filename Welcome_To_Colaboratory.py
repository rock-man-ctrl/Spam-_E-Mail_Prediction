{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rock-man-ctrl/Spam-_E-Mail_Prediction/blob/main/Welcome_To_Colaboratory.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.feature_extraction.text import TfidfVectorizer\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.metrics import accuracy_score"
      ],
      "metadata": {
        "id": "6fMw-0akmORD"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "raw_mail_data = pd.read_csv('/content/mail_data.csv')\n"
      ],
      "metadata": {
        "id": "BpflgbQ9mOYC"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(raw_mail_data)"
      ],
      "metadata": {
        "id": "Sd7_5fErm_Pr",
        "outputId": "31eae35c-b01e-4237-c500-1d512dfc2b2c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     Category                                            Message\n",
            "0         ham  Go until jurong point, crazy.. Available only ...\n",
            "1         ham                      Ok lar... Joking wif u oni...\n",
            "2        spam  Free entry in 2 a wkly comp to win FA Cup fina...\n",
            "3         ham  U dun say so early hor... U c already then say...\n",
            "4         ham  Nah I don't think he goes to usf, he lives aro...\n",
            "...       ...                                                ...\n",
            "5567     spam  This is the 2nd time we have tried 2 contact u...\n",
            "5568      ham               Will ü b going to esplanade fr home?\n",
            "5569      ham  Pity, * was in mood for that. So...any other s...\n",
            "5570      ham  The guy did some bitching but I acted like i'd...\n",
            "5571      ham                         Rofl. Its true to its name\n",
            "\n",
            "[5572 rows x 2 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')"
      ],
      "metadata": {
        "id": "sy2WNgpqm_Sa"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "mail_data.head()"
      ],
      "metadata": {
        "id": "4st2alnUm_VF",
        "outputId": "d6766b95-95fa-42a7-ae94-bb76bd063712",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        }
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  Category                                            Message\n",
              "0      ham  Go until jurong point, crazy.. Available only ...\n",
              "1      ham                      Ok lar... Joking wif u oni...\n",
              "2     spam  Free entry in 2 a wkly comp to win FA Cup fina...\n",
              "3      ham  U dun say so early hor... U c already then say...\n",
              "4      ham  Nah I don't think he goes to usf, he lives aro..."
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-68346f1b-78f4-4693-affa-7bd008616e5c\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Category</th>\n",
              "      <th>Message</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>ham</td>\n",
              "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>ham</td>\n",
              "      <td>Ok lar... Joking wif u oni...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>spam</td>\n",
              "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>ham</td>\n",
              "      <td>U dun say so early hor... U c already then say...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>ham</td>\n",
              "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-68346f1b-78f4-4693-affa-7bd008616e5c')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-68346f1b-78f4-4693-affa-7bd008616e5c button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-68346f1b-78f4-4693-affa-7bd008616e5c');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mail_data.shape"
      ],
      "metadata": {
        "id": "NKRQYxv-m_Xs",
        "outputId": "cf7c98f6-8249-4c40-ba79-452eea5b2b25",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(5572, 2)"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0\n",
        "mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1"
      ],
      "metadata": {
        "id": "vxVWwa5lm_aT"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X = mail_data['Message']\n",
        "Y = mail_data['Category']"
      ],
      "metadata": {
        "id": "s3h6lUmSm_c6"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)"
      ],
      "metadata": {
        "id": "n30ib_t6m_fi"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(X.shape)\n",
        "print(X_train.shape)\n",
        "print(X_test.shape)"
      ],
      "metadata": {
        "id": "_mngUOGtm_iS",
        "outputId": "2a78cbd3-f0ea-45eb-b289-17a07f0e0379",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(5572,)\n",
            "(4457,)\n",
            "(1115,)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase=True)\n",
        "X_train_features = feature_extraction.fit_transform(X_train)\n",
        "X_test_features = feature_extraction.transform(X_test)\n",
        "Y_train = Y_train.astype('int')\n",
        "Y_test = Y_test.astype('int')"
      ],
      "metadata": {
        "id": "CmwBf-mlm_mr"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(X_train)"
      ],
      "metadata": {
        "id": "99CvTvtdn0lz",
        "outputId": "6feb9eb0-1d56-4f07-826d-e1595590729c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3075                  Don know. I did't msg him recently.\n",
            "1787    Do you know why god created gap between your f...\n",
            "1614                         Thnx dude. u guys out 2nite?\n",
            "4304                                      Yup i'm free...\n",
            "3266    44 7732584351, Do you want a New Nokia 3510i c...\n",
            "                              ...                        \n",
            "789     5 Free Top Polyphonic Tones call 087018728737,...\n",
            "968     What do u want when i come back?.a beautiful n...\n",
            "1667    Guess who spent all last night phasing in and ...\n",
            "3321    Eh sorry leh... I din c ur msg. Not sad alread...\n",
            "1688    Free Top ringtone -sub to weekly ringtone-get ...\n",
            "Name: Message, Length: 4457, dtype: object\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(X_train_features)"
      ],
      "metadata": {
        "id": "vskyMf17n0sS",
        "outputId": "20f5e984-20a4-4ddc-a2e7-f8ed733c5e7f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  (0, 5413)\t0.6198254967574347\n",
            "  (0, 4456)\t0.4168658090846482\n",
            "  (0, 2224)\t0.413103377943378\n",
            "  (0, 3811)\t0.34780165336891333\n",
            "  (0, 2329)\t0.38783870336935383\n",
            "  (1, 4080)\t0.18880584110891163\n",
            "  (1, 3185)\t0.29694482957694585\n",
            "  (1, 3325)\t0.31610586766078863\n",
            "  (1, 2957)\t0.3398297002864083\n",
            "  (1, 2746)\t0.3398297002864083\n",
            "  (1, 918)\t0.22871581159877646\n",
            "  (1, 1839)\t0.2784903590561455\n",
            "  (1, 2758)\t0.3226407885943799\n",
            "  (1, 2956)\t0.33036995955537024\n",
            "  (1, 1991)\t0.33036995955537024\n",
            "  (1, 3046)\t0.2503712792613518\n",
            "  (1, 3811)\t0.17419952275504033\n",
            "  (2, 407)\t0.509272536051008\n",
            "  (2, 3156)\t0.4107239318312698\n",
            "  (2, 2404)\t0.45287711070606745\n",
            "  (2, 6601)\t0.6056811524587518\n",
            "  (3, 2870)\t0.5864269879324768\n",
            "  (3, 7414)\t0.8100020912469564\n",
            "  (4, 50)\t0.23633754072626942\n",
            "  (4, 5497)\t0.15743785051118356\n",
            "  :\t:\n",
            "  (4454, 4602)\t0.2669765732445391\n",
            "  (4454, 3142)\t0.32014451677763156\n",
            "  (4455, 2247)\t0.37052851863170466\n",
            "  (4455, 2469)\t0.35441545511837946\n",
            "  (4455, 5646)\t0.33545678464631296\n",
            "  (4455, 6810)\t0.29731757715898277\n",
            "  (4455, 6091)\t0.23103841516927642\n",
            "  (4455, 7113)\t0.30536590342067704\n",
            "  (4455, 3872)\t0.3108911491788658\n",
            "  (4455, 4715)\t0.30714144758811196\n",
            "  (4455, 6916)\t0.19636985317119715\n",
            "  (4455, 3922)\t0.31287563163368587\n",
            "  (4455, 4456)\t0.24920025316220423\n",
            "  (4456, 141)\t0.292943737785358\n",
            "  (4456, 647)\t0.30133182431707617\n",
            "  (4456, 6311)\t0.30133182431707617\n",
            "  (4456, 5569)\t0.4619395404299172\n",
            "  (4456, 6028)\t0.21034888000987115\n",
            "  (4456, 7154)\t0.24083218452280053\n",
            "  (4456, 7150)\t0.3677554681447669\n",
            "  (4456, 6249)\t0.17573831794959716\n",
            "  (4456, 6307)\t0.2752760476857975\n",
            "  (4456, 334)\t0.2220077711654938\n",
            "  (4456, 5778)\t0.16243064490100795\n",
            "  (4456, 2870)\t0.31523196273113385\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model = LogisticRegression()"
      ],
      "metadata": {
        "id": "GebiIWAtn02i"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.fit(X_train_features, Y_train)"
      ],
      "metadata": {
        "id": "Ca1pFMNRn05S",
        "outputId": "6dd28011-f615-4c6d-cd55-126c3b5df941",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 75
        }
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "prediction_on_training_data = model.predict(X_train_features)\n",
        "accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)"
      ],
      "metadata": {
        "id": "Bq-qG9qwn08a"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('Accuracy on training data : ', accuracy_on_training_data)"
      ],
      "metadata": {
        "id": "ux0VeZPon0-z",
        "outputId": "f36a4650-7c2e-48e1-cbb8-c3d6bc01ae2f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy on training data :  0.9670181736594121\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "prediction_on_test_data = model.predict(X_test_features)\n",
        "accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)"
      ],
      "metadata": {
        "id": "FwAeTWplm_pd"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('Accuracy on test data : ', accuracy_on_test_data)"
      ],
      "metadata": {
        "id": "o04YauNXoJas",
        "outputId": "80e5bb5a-58d6-48ec-abd5-930df5986fb1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy on test data :  0.9659192825112107\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "input_mail = [\"WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only.\"]\n",
        "input_data_features = feature_extraction.transform(input_mail)\n",
        "prediction = model.predict(input_data_features)\n",
        "print(prediction)\n",
        "if (prediction[0]==1):\n",
        "  print('Ham mail')\n",
        "else:\n",
        "  print('Spam mail')"
      ],
      "metadata": {
        "id": "hughRplkoJdK",
        "outputId": "71b2ceab-a0e9-4320-e3e9-cb523e0719f3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0]\n",
            "Spam mail\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "input_mail = [\"Hi this mail is from mom, come by evening\"]\n",
        "input_data_features = feature_extraction.transform(input_mail)\n",
        "prediction = model.predict(input_data_features)\n",
        "print(prediction)\n",
        "if (prediction[0]==1):\n",
        "  print('Ham mail')\n",
        "else:\n",
        "  print('Spam mail')"
      ],
      "metadata": {
        "id": "nEX5pVKppxUc",
        "outputId": "964c7786-4ea0-4440-d603-a0f775ad9a9b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1]\n",
            "Ham mail\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome To Colaboratory",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}