# hangmanGame

Siz bu kodları copy paste yaparak adam asmaca oynadım dersiniz ben Pythonda sys modulünün argv niteliğini kullanmayı öğrenip, mini bir adam asmaca kodu yazıp,  githuba attığımı söylerim teşekkürler..


Before using the sys module I ran this code like this python hangman.py.When you run the code after the using the sys module you will see ['hangman.py'].As you see sys.argv command gives a list.First item of this list is name of the our project file name.


I ran the same program as follows ['hangman.py,'cpsc231-lexic.txt'].Why did I do that because why not:).Anyway I added second element to the list which is txt.file name.Then I assigned the filename to the 2nd element of sys.argv in the code,as a result the filename we called was 'cpsc231-lexic.txt'.


You can't run this code like python hangman.py anymore.You must write ==> python hangman.py cpsc231-lexic.txt if you don't write you will give an error message.
