# fftprogram
FFT(高速フーリエ変換)をするためのプログラムです。
## description  
実験などで得られた値をフーリエ変換をしたいとき、input.txt値をに保存して実行することで、ピークをとる周波数を出力します。   
また、値を計測した際の時間の間隔をdtに設定する必要があります。デフォルトではdt=0.01sに設定してあります。  
ピーク値を設定する方法は手動になるので、出力されたグラフをみて必要に応じ変更して下さい。　　
デフォルト値はpeak_cut=10に設定してあります。
## demo  
出力されるグラフの例
<img width="777" alt="スクリーンショット 2020-03-13 10 43 03" src="https://user-images.githubusercontent.com/54773770/76581690-a54a8900-6517-11ea-8288-66b219d7e54b.png">
出力される周波数の例  
```
peak [ 0.39081583  0.78163166  1.17244748  1.51441133  1.61211529  1.70981925
  1.90522716 29.9951148 ]
```  
この場合、出力から一次の固有周波数は0.78163166Hzと読み取れます。


