# 1

Base64 をやるだけ。

https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=V1dWekxDQkpKMjBnZEdobElHTnNiM2R1RFFwSkoyMGdkR2hsSUdwdmEyVWdlVzkxSjNabFExTk1lMWRsYkdOdmJXVmZOREJ0VUY5emIyNW5jMzBOQ21Gc2QyRjVjeUJyYm05M2JpQnRaU0JoY3l3Z2MyOE5DbGRvYVd4bElFa25iU0I1YjNWeUlIQjFjSEJsZEN3Z2QyOTFiR1FnZVc5MUlHdHBibVJzZVEwS1VHeGxZWE5sSUhCc1lYa2dkMmwwYUNCdFpTQmhaMkZwYmc9PQ&ieol=CRLF&oeol=CRLF

`CSL{Welcome_40mP_songs}`

# 2

URL デコードすると CSL{文字列}があることがわかる。
中身を Base64 すれば OK

https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=VEdWMEozTmZabWx1WkY5dGVWOXRaVzF2Y21GaWJHVmZjMjl1WjNNaA

`CSL{Let's_find_my_memorable_songs!}`

# 3

Base64 デコードすると、モールスコードが出てくる。後は、CSL{}で括れば OK

https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Morse_Code('Space','Line%20feed')&input=TGkwZ0xTMGdMaTR0TFM0dElDNHVJQzR1TFMwdUxTQXVMU0F1TGkwdExpMGdMUzR0TGlBdUxTNHVJQzB0TFNBdUxTMGdMUzRnTGk0dExTNHRJQzB0TFNBdUxTNGdMaTB1TFM0dElDNHRMaTB1TFNBdUxTNHRMaTBnTGk0dExTNHU&oenc=65001&ieol=NEL
`CSL{AM_I_A_CLOWN_OR...?}`

# 4

総まとめ
spin と言っているので何回か繰り返す。
今回のスライドでは、Base92, 64, 32, 16 しかやっていないので、この中から該当しそうなものを選んでいく。
すると、文字化けした文字列が現れるので XOR でブルートフォースすれば OK

https://gchq.github.io/CyberChef/#recipe=From_Base92()From_Base32('A-Z2-7%3D',true)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base92()From_Base32('A-Z2-7%3D',true)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)XOR_Brute_Force(1,100,0,'Standard',false,true,false,'CSL%7B')&input=PEw7bSk%2BL3g0XlZ8VUtnRUBhRng2LzFSQCFYQyhjTHs8bXViOkAxYlt0Xl8pL0FPPlcwXUVVMD1VaEVDQEo/KTpEaWpGfV4yczxUMlNRVUs0Rzw9MXNXcVBaYW9AMjw9PHA7fTtpXjM0Vl07KHtVTkBjdTkoKC8mQCRfRT9lVVM8Sl13KU1eMmJJVn1WQDEmQEE8OSxBLnQ/clt1KT9BZDlfdDAzMC9Hc0Zhaj55ZEo/fWhtRVQwPG1tXXw/ZkdSM11RemlnW0NoQ09xPy1VTDRoPDFCcC83SyNTQ2xYYUo/PUcwMEpeUz85RiwoYyhXOiRGKzF2LlIpV1RxbiMoUj42PEkqdFdwYmpZaFU7YWI/PUZfME0tb0VXRmNWME9qPE5GLz0yXjJWOlBZVSphbD55JTovLi5SeSZhbD89aiw%2BWTtQKU0uQz9kUmhTUWx5P3pSJ0VaLiM/aFNIbGJNLD9baWpBSC5RRUtcWihZXXg6ZHVNMXIudFwoU0dAKis2PE1qMj94XkJnWlY7VSM5Rj9bR0AxeTBcP3ZhbihjPDk1Ky94eS5ZZg&oenc=65001&ieol=NEL

`CSL{Plzzzzz_listen_to_the_Karakuri_Pierrot}`
