import os


"""download the datasets and weights"""

weights_cmd = 'wget --header="Host: doc-0g-bo-docs.googleusercontent.com" --header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" --header="Accept-Language: en-US,en;q=0.9" --header="Cookie: AUTH_b5jtns4ck78tigmpo89ahjrn41g6mu2j=00136291565935142094|1519516800000|sfsjro36ifkiicmgv7uti32g05inh1vc; NID=112=vDKZHRBGRNz3a3IoJBaYtAavrx4gMh48DfN3XUoqzN_S9Szefm7JVfQ6ihEsYLxWD65UBwE7quJ5nY-vlEajsXX3tyXi5IjH7sQkzUGdHEq5ONxYTAQuGP34JrUdry9K" --header="Connection: keep-alive" "https://doc-0g-bo-docs.googleusercontent.com/docs/securesc/9l7nlf5ef9qbeb6uoi42plsmq4dnaq95/kc2uf3on6cfkgr27sa4v3dmt11u5qfru/1519516800000/11366482865001617448/00136291565935142094/1hRZB58u9P2SFWUnr07ocW7iE4Ll4Yo8J?e=download" -O "weights.zip" -c' 


dogscats_cmd = 'wget --header="Host: doc-00-bo-docs.googleusercontent.com" --header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" --header="Accept-Language: en-US,en;q=0.9" --header="Cookie: AUTH_b5jtns4ck78tigmpo89ahjrn41g6mu2j_nonce=716rc0fjso4ng; NID=112=vDKZHRBGRNz3a3IoJBaYtAavrx4gMh48DfN3XUoqzN_S9Szefm7JVfQ6ihEsYLxWD65UBwE7quJ5nY-vlEajsXX3tyXi5IjH7sQkzUGdHEq5ONxYTAQuGP34JrUdry9K" --header="Connection: keep-alive" "https://doc-00-bo-docs.googleusercontent.com/docs/securesc/9l7nlf5ef9qbeb6uoi42plsmq4dnaq95/pf53t2hsfp03d4gukqvpknjq185dmp5t/1519516800000/11366482865001617448/00136291565935142094/1SnuvIZIV3RMtrpD4kCXBWOxeV3q_dl1m?e=download&nonce=716rc0fjso4ng&user=00136291565935142094&hash=i0d4lb2g996jhkrabnhq1lmn8q4hllho" -O "dogscats.zip" -c'

planets_cmd = 'wget --header="Host: doc-04-bo-docs.googleusercontent.com" --header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" --header="Accept-Language: en-US,en;q=0.9" --header="Cookie: AUTH_b5jtns4ck78tigmpo89ahjrn41g6mu2j=00136291565935142094|1519516800000|sfsjro36ifkiicmgv7uti32g05inh1vc; NID=112=vDKZHRBGRNz3a3IoJBaYtAavrx4gMh48DfN3XUoqzN_S9Szefm7JVfQ6ihEsYLxWD65UBwE7quJ5nY-vlEajsXX3tyXi5IjH7sQkzUGdHEq5ONxYTAQuGP34JrUdry9K" --header="Connection: keep-alive" "https://doc-04-bo-docs.googleusercontent.com/docs/securesc/9l7nlf5ef9qbeb6uoi42plsmq4dnaq95/t4ho7spresuvotv11d4rgvbaihptcmqc/1519516800000/11366482865001617448/00136291565935142094/1hAxnVuSlYY8e3tRw3mSclFkgkLU31oT5?e=download" -O "planet.zip" -c'


numbers_cmd = 'wget --header="Host: doc-0s-bo-docs.googleusercontent.com" --header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" --header="Accept-Language: en-US,en;q=0.9" --header="Cookie: AUTH_b5jtns4ck78tigmpo89ahjrn41g6mu2j_nonce=56l7ru3bnu9vs; NID=112=vDKZHRBGRNz3a3IoJBaYtAavrx4gMh48DfN3XUoqzN_S9Szefm7JVfQ6ihEsYLxWD65UBwE7quJ5nY-vlEajsXX3tyXi5IjH7sQkzUGdHEq5ONxYTAQuGP34JrUdry9K" --header="Connection: keep-alive" "https://doc-0s-bo-docs.googleusercontent.com/docs/securesc/9l7nlf5ef9qbeb6uoi42plsmq4dnaq95/2m2dkc06jq7c1r4drec9odd0olft0u3i/1519588800000/11366482865001617448/00136291565935142094/1j6yLjAGe3wr-GEiDnVTWXBfD4lEwr699?e=download&nonce=56l7ru3bnu9vs&user=00136291565935142094&hash=5vgubr8jlsti77pvaq7ou8iiajki08he" -O "numbers.zip" -c'


reviews_cmd = 'wget --header="Host: files.fast.ai" --header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" --header="Accept-Language: en-US,en;q=0.9" --header="Cookie: _ga=GA1.2.1559169601.1513111499" --header="Connection: keep-alive" "http://files.fast.ai/data/aclImdb.tgz" -O "aclImdb.tgz" -c'



"""activation setup for environment"""

print ("Setting up environment...")
os.system("conda env update")
print ("Downloading packages necessary...")
os.system("conda activate fastai")

print ("Environment setup complete")

print ("Will begin downloading all necessary datasets and weights for models")

if not os.path.isfile('numbers.zip'):
    print ("downloading numbers.zip...")
    os.system(numbers_cmd)
    print ("done downloading numbers")
    print ("extracting and moving numbers data set")
    os.system("unzip numbers.zip -d courses/dl1/data/")
    print ("extraction complete")



if not os.path.isfile('weights.zip'):
    print ("downloading weights.zip...")
    os.system(weights_cmd)
    print ("done downloading weights for models")
    print ("extracting and moving weights to fastai directory")
    os.system("unzip weights.zip -d courses/dl1/fastai/")
    print ("extraction complete")


if not os.path.isfile('dogscats.zip'):
    print ("downloading dogscats.zip...")
    os.system(dogscats_cmd)
    print ("done downloading dogscats data set")
    print ("extracting and moving dogscats data set")
    os.system("unzip dogscats.zip -d courses/dl1/data/")
    print ("extraction complete")


if not os.path.isfile('planet.zip'):
    print ("downloading planet.zip...")
    os.system(planets_cmd)
    print ("done downloading planet data set")
    print ("extracting and moving planet data set")
    os.system("unzip planet.zip -d courses/dl1/data/")
    print ("extraction complete")


if not os.path.isfile('aclImdb.tgz'):
    print ("downloading acl IMDB reviews...")
    os.system(reviews_cmd)
    print ("done downloading review for NLP setup")
    print ("extracting and moving reviews to data set")
    os.system("tar -zxvf aclImdb.tgz -C courses/dl1/data/")
    print ("extraction complete")

print("downloading jupyter notebook and packages...")
#os.system("conda install opencv spacy")
#os.system("python3 -m pip install --upgrade pip; python3 -m pip install jupyter ipython ipywidgets; jupyter nbextension enable --py widgetsnbextension; python3 -m pip install graphviz isoweek torchtext sklearn_pandas feather_format jupyter_contrib_nbextensions plotnine docrepr pandas_summary torch torchvision")
print ("downloading english language for spacy... (Needed for NLP)")
os.system("python -m spacy.en.download")
print ("english langauage download complete")
print ("all good")




