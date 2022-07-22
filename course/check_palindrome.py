import sys
sys.setrecursionlimit = 1000000

def palindrome(A,left,right):
    if left <= right:
        if A[left] != A[right]:
            return 0
        return palindrome(A,left+1,right-1)
    return 1


A = "ababa"
A="kmwcgtpmzsuwvtzdnpdlxzgwgaewksrmrtkohnnldgnnunteezkgyexxcwcuznuuukygmxcacupthnwsezponuzsmuteqdpagwoxylfdhmpcixmpevrgxmiogufdwihydthbsypkofpiwendztwxrumwuyeotposasxlyekqkhogouikpfoemjurvfsgoccepiobtuufpfestybtmlfawczmthroigljoldnoglauipfjgwitdtgnlhukbplabcnzokcnfsoaiqkemkbndsxtqqenweiapvsdxthuiubxvrfoyaufcspebcxxdugieaccwtmwdpzqvsmtaquhcbbmoklqdldjlosoqsdopdouwqvxxstftnkamorzihkmganadspkgognejmbxjcxjiddncvynekuoosbnwipysowhfgqdhxjoblernbejcaxxgixamtioeiqshvzxkjxotinxyoacubjukrxsvnmcbdvffsoiyrgnyzxnjhmptmgzyvocdtfkvxhoujlequtswoikugzqpeyiqpwduovmkcldgmlfzrdmcspdiuebizxekntrxfgklhuihwzwnjabwjtmfzugjczoucgpknqvcltlgsglyzhkggoqlinsadowyryrwgrrdyeejghparvjycljktvrvwebwfobdhgfpankwaqawgwmnaemxtbyywylxvrtpuabuiabudlzwjanyngpxjkjsktoyxjxzngsxwuioxxqqpoazpcmkpejewsinygmnrgaezbmvvvhrzlisbwbouqaqebpsmvmllqdfmhvkalsmgnnvabsfutkgxyfemzeenddvuvrejytnfpofdexqctwulyghgxemtavemczodunszmybxrazitzhtywvdvbzaanodkenhskifztvtdmqryvkpmuzgrryatgycpgiollhvolxqjvowkxknnivttengzbnjsyfsrkhctcxtpvkgbvironztntdxuuozwuympeudlssdrqaqabbpysswbjeycdhuucxvwlprtaeugqedgvoivmoteyoqbgcirsjerllfqojndvxawnkdpiokzbeslbpkxypqslszwrybhhfnvzmnngwozuefgritimluffowupezyqgppxgworqiojpjqnqzbgzlfqxefphesvqhmrutrcnnievxidruzzxyrecqtbbhfcyajirhejpkajsvnwhjxtcgfqgiypozjqrpfupnuvspxovbgkeeznwvgayjnysrwkafoiyktobjcfogjtrsbmxibcjypetuicwtdhnsgyjcworvixiidkassmsqgqpgrgqftbakmplphabgimrpflcsooksbcgmzhvguibuxwaabjahwatyjsnbqfigrfmxywgwflvhopnerpyplurkauryajffaxvaulyzjpdpvtzskmiangzefncwlfdtxuoazrrqwwbpdxdgkiupsfhutmsdprqkvuspwuxulrpkflqcutpzooilijvqrehzybdywupqiqzadgmbhjzrfpymdibmaoovnejdqxuhcvsiklbxrdakzmremjeqcnvnrvtpyzzjomqstbhvcvtdceeaaygrawtwagtweoqzyprfyljsjiwrkqztshpiyfywbsvjdvtyniejebknzuwuxgmowulyzxwrstrtouuclabxouexjszrepsqvastqzqxyywxfgntbzjegyhpclxewfjqnxvckpxryszqhqqmweizkljaybrtoipwtolhtstjivwovojspiulxvdbdnfngkpbcaxxxpgrbsxejkxdinunoqnoexltozkqaflisrazjdkzscbnfdukysjcatctnlcsmlnvibrkztqwrgftuexeodcitcytconohqwhjhgccgubctjbjifcqbehcspgibhjbiwuakqiuoqswdssywirsnucmpiqfgtmrctfwudsahgrmfmbwavqtfqexbhkdmthcascukbfdrgeudblmkwyqvkcyuxbmslveyxekanglgdyssujdtfkphhkoboggewxxgzjyvdobenhdyzzlbdlhhethzegpucagkaebedqgiaaypecorahhhnuwyiufagleamqifqjmsbnkauivmqtxpbgmrmfuuitgegauduikuoubdhazkmguazqfszdwvizxccdiumfugapqxgwbgxzfjgjptxxuxrezezjyjehteoqghbpvqzdecqkdqunluzdqfxpiwwbicrohdssjpwbrigqarvhwmdatlazdcdypkneaymsnzuitbkctrmmfzhidkvxskhvlqkvthpexelbtrsemctxqzfksokwtvkxmawvvxckvovhafrpvtpqqaevhrjlhyfvblyxfnnjzvaqondwakqdskwannqoalcglbzuppawfiudwysmwuyjthtaematbfzhgyqbzmyyhornfsmkrpyovqqayhaftchipgtncmblupjhbawxhvajhlwoaeyxehgorrlwppnzvovqninssvjdoxvdkfcdlidwyheppbxuztidpebxnsxjgvruowrerqavjkeolurmawuteyyxkgsugoimydnmpirmjjcsfavepdnohczovenrcbcijmaxrkjvgscjhxaycginkyoegcinkcstxvvfrhkzvlqwmpexhblmropgwsycdolydwormpfasisgfwiyyuuyxxzpugzpxtfcmdjvnjafezxspncqayvnqpovxatwwwkxnrrmylbmcmebaeiqbzhtgossperquvmgyexgqcbkkrhxahjpbjvqrimdwqrvglixlisqcpuatoadlujyxelxktkivmpppwaqmlfbmjetrardzzdmqcpszjkuthghbxwgpdrujxespfvhodttuvtuhynycrklkokiaalkyrglayjirlnocbyknoebfmhyigikjgwwlcetkubvvvqxcbdsgarqfqwcczhdcufxlwpqyrhqfcaezihoaggcuxhmuukfxaazmrfmlnjpjsziwglbdasidvzwufojzmtlfulolfuvvlqwpouwnwnopcaidgtljeufvqetlmuqwjxglmzxaehtixqsobtgogkxiaddaqbljwijfuxmakaxlmsudorbyaedhnygqqqifgiddydulwnmtokpgwnljoqvirebhilzjfbnmzdvfjavsdtrccplikeeeiiwmarlbsshlzhwsbtxeevtbcsligedszoaecdffpbcgnosfrmeyounnnkodhnbrqwxgeovoekvwkostbbgpvneslyosbvsrdvlryobpnainsbdzwtmgeuwjwekubmtkclzzwrasovugwwlxmvyllrnjcuazopdqpsoordygrnvozrzxymjksbpcbdjmntppodchbjquaxevqkhscenbegrfsfmwtiwlzaffqalsioxiwywrhpswtipbncdpqavnthaokjgswubkzksxbsunpkyybrlcpbpgktzlhqgdkjfjogsahdjeymtrnygcejwjmxxtnyltfdwxlczgdiwdwlqmxxfrsgdyllrgybamxizrgwfztiiiwxvgttohdqftlrepdplmsrncjrxxnpplfgaojribkhtxovvflvtcmhpvaldwhgcglfvyvtyeqrqfmjpamxeuuspzxsqzardpdctjurdrbapuzzpovhtzsqqeefgtbmqhrcdjntulsrzsznruirxkbthotuapcwyvxdbzqdvodthgnkqnnqtoxotwdorjkjcrnnmskflgjcjldptmwludritncrioxrgshrgyzxisuikxdvzufgarzloplbcrdvvdonxgfkfdjmybhojvptgaxzhhhrygysbcypzrghwhfuddfiydkiowzwkygtblwgyesislwbcfkawzpuflhmivfhsumqnnzvrfoevrdouikpierjhyberamtdoempzcftezjsqmroyqxzimymsmcciytzvrnmbxidgvocsnwhgaminkazsisdgdcnhxinsllcjqfegxvbwpfhdtkehzgiiupohltbvtzkuxbkqrfhbzgfrfvltnhudlpuntwnytuhmxowhzydkvgkmceffhrlvezjibiacdmczygsglusfhxrtykhynuclpsotldmmrbvsfakfgpzdhtbmjhpsozdktwhwtbacbynlmazrvyvtqhvpvzifgwgkixvspzaxssrbrhyrcerbuzudokmgoyeaobwzewuouzcrufdrslxbecajjfcmgssmchowiujrlfrlrilldhovgiahyyycoxkvscyampozaesgqvmmbamfjvqgljlbflsqkqzinnxkrtmoteifurztfcypmdmhhwjxefnsbomackjiybzvatwjkvbivzgcvurpyvemycsxnlerqtflhowdgsywsluthgrbshzzkdvapvboxexxxkqtrzcodjshoxmhqnamfootylvldupjktrjotoczutgispirvaawkiwmldikiwczdjxbnsheeslvxfnnqedtmyckfplietfklghjholersbhxzwubbiqcxeetwaxneqvezmyjrlvpzoyemdcmgmddewqhszjztgikujfgnyxhnxzqejjnlbanahwzyjjyuyzlshoejuwggfuoahlzhrdymwqjkjjdxycwmujlusckwsxmhawcovwdqbrrzawwzfbxfyhuowpteypmkgcetcrkfbobqgkirqvqcqilpbbjqgcgsdyzcbwhtpbniucljvisjhrgwuvblbhtaduyuyvywnbseezfsscfpdiqjobfvcpefyrawrfkbzefqgdroijodzuqdlttmeebncippyysdwyolgnllgzjakxzhtjwzzjcvlblcnouarfvnhnbfvsyqmvlqxdtftizfjmufermfhvrdhbquasspyiwtonuenspbuonrvlgufguzcmyxvrnrvesndzrkevvcwcuvcjdtrpqarofyyjzmvupzggxeuylnjkrwrmlffwkbfpkqkdlzlbmumsukyuvoxpvvfsshmumvqhjmoplfidfcsjabbupbzdntjykezcwhfydqcatyqfqgwxbgjfideuhlwabviilhxneeltuxuhbwwgsabnekjixiauyemmlmgvigipfagnderiagzpfzcltrfayfauxnywoidtyvunddgbbbslughllcwwibguhdybythlfiqjnkohzmlpvpxbveaqomvjldxyfsxckcdqttneslkhnbnvnqknarrhsiuflbbtxxfqdovfxpgrrljidxdjhvniuzqsuzngqwywqkeujlmpshefvcfxbxqqfzbtvumopvzjmdnjjskvwtdwbkeksoknmjllqgjjuzjltswoshzdjwyftcbklombavnihyrzdpkuwcpvpbufvygijtbvwopoqmqlrlfbmipqvassvzlepssradwnzmticlnqcnvtwffpnxqxxlrwipihxfkypdahspwgibriazsylolpguatrcdwrdcpxfezyfljchiygvdscwdsgcxxwcmbctwezfwreospujpmkpyxklesvqpkqwjwsgkclyolbjzzpcaqhmwejepdfoeqdjogspabpbinxseidlggjmatpextllhppjubouvuwdzpeigaubkqwreoukuisiqqrncnqeuluyxvimemhhcomanbulvgopixvcpfvnzdzthwarpqyphzysuwnsznrhaunlzvmqvgcvwjpwbgqremdxvsgwwnlocbdzlwrtjlbnwkykauxebtrdcbmcffthtqofidotrmpwawesbqlowhyjngbvovekypjgmgthwqojxrsvpgzoyichnupjkhumvmkcsqotivwlithqxoltosioiflfodbyfptgcyuuyzublosrcyjgbxzzchvmyfnvnnacfdygjiokmqyvcjemsrvjmextbhwgnsmkmkcivsxgalrdtbajfvsxwysxcfltkzixltwolppmokbgsglqohgejaiazsdngpscghlfsdozrxhzcmkzemcfizpzgmofimqeeolaktjcxzjbpxtkiluanzciwnscbwkuiseyllewgrjbkzfouimylvzubfsozqfordbmyrtigfcpwewgpnfvlfnzjumdgfzmkxslwrbzdpwwdxgpemjpshesmeqxnficbuzsqvcbxkqypmiefvtryjsazzxsghjjokzfxhszwdgxfywnvybubdseerdfzpiawtwpdtinyaomihfgdbfgufozavgsqlacoldfqzrhlengnmvuvxktayxnwvxeexjkplgmhqdikbxbnredmomuocdzqmxbuxpenfnfjiwdmtddypdmkasvgaavlxufcddecrvxcyueqixfwweyozgtgdbuwawjalnnohevfxxpgudryvruhlwnozquzhfoqewdnfnzvyxvalywhmvhvqvseqlgnhoibiatbekysymsrzgjnkadrmdlwxaflhpjbphcdnrmdbvjogzzvdghzgytjjexfxgcexgtmkrltmrutpnzmfahysbvkostwaihfonfbceoeuvhrcriiuqplbvvkjatvmjbbuvtgfqmnpxobqatkazsacziluammtyrulqidbabicmpskgqfsjponyrajykhzvssswktekrmbuzqcdkldufyurddcfujoufyamynumrmsfdrevhrnrhconntbyfvgclmfqnwbfnojmkqzhegbafhunovedcubbpsiuonvxqhxxqqxojkditkeydrnscsskdstycgfxgnwiguvuefznwbhalqhvtdtboxmbqdpdrhjppqvfhqxpaxjvliupundglsfihjtlksibuzcvxabhgeyvvoluwidalnmhtjpoynulihwjukrnvpefofhqmupvxmaidhxghenrvfzjvmgvojxtvbgasdbhwlntxqftflxpkupbhgoqugftblqtglqhnbavknnqhnhznixecwqcvnemvmcrwstjiyobumaajvgwlaxdcprtkwwlamraqmwpwurpvjfjkgogskagxhngxaqmzqllfxayjotdtbqhlearrlqtjgsbgycpkxbutzfuohwzvcuudoyqramujabpetgtivlfpxlwvpkibqbyhvkwmjklcqxyutqygsxsbiamfgksthnqtpslvluipyuincewznpgzumwpxjvdyodayefyfvfmyzaqlaamfduaitdnzbkmnxnapstspsueyocrhccibhunvjtenzrupcqchyfnqzruptzorliwtpaoznzgyjvhlmhytqhwfduveyjcjnpvyumvbpfcgjshshghrchqsywwcpcxwsbipydhtkvehvqjyufqfjcmtusvpslwpbkfcknckbcfuoyjvtjmvhprblardbucsghrmpkfjeyuwggarcsknowihximrenwzzhhjtfpynldyyhocoysfgpmeevsiexbhcykgogzgjsuwcpcueubhjkbbwbcadgdlwqbcfkuyhtoszcjkufwxgmuqxyhqdyzpndzrhoncpetkfdorboonuykrgnsdecdigyjjyvrkukeqkoogpmqsjgkxrawzystvntjzlvojcyqauuyvugrpkahttphptjahlwoocwbizessxrjndlgtfwiphhluvznwvepplgzufczoytpyrkageyuyawdovyxgzxdvmrpugwukzzphvykknrlnrdxwnzfhrapkhhmuuamnwxynepmkycguamojucfnwickesbgxpekoxtmmjrvxfcysndpuuzywkdclfzjoysspbjxpiyotwssalpaizclocpnaptgjjfxwghgopuemwlqqujfkrcbgmeigsejhspzmtiqtdoxbrumlonpfxizlkbdnowhhsynxsuewqxtvfenzmolhrjxhlsadcavlnmeenwifoyhgdoomtivrlstqwftcgjdjrzvtwyzmtcmahdmksulzisypuboseemmvgmzybgvepgvkztggqtgmrbebdhffabxkctmqtzohyzzybkayvzedinmyjyvloskhusfcsjwelyvveefrejdorynnihtcdkaiqffawoxcufnybbeadpdpksqwksljxalxfsxaendsiqadjgnunluhehbgkstkxmzwqvohqjqoeteenbqlyhlucxchkijwcayjqyabekwswleiqtbhjbngzkptpbtdhhocstcajdnfffkzipkimrkyswuuohnbnobltrwfffxtdhlfinnhildinzmzogdvbmzeijcojusurgnxsnqlssylifctyjtnszfzdimoyoxynzlslgwcddfbgzemmnlvotlvdmktsdiessvszkziuikqhcjufcsiuuevlbclojoxtccjsntxqsnbyrjpzluxoavwecqhyawrehapubocbyimaegqjhnkfxaofcmxziycesrucrcziakfcbgchojvbtfqbcqkfpaobwdgqkjgpjtxdfrgstcwdozylyfgtfdmwdkjgwzushomdllrbvelwkxszstlaeiwzumqwxwpmzealgdysgzzutzpssayncjovehmzxziwkzinunomtwzinabcoupdbxthxmaiecedazsfruknblluogyqydfduwwejngwwdcigvbatthmgcjvxvgyqtouqwpnfakatmixfarfecrzmhhdbvyouyggangfwthinzipzqglyzurwkybasfkilwmyzqbzosmsiaptsntpjzznvdejwzzdcyjwuzlzvbxuhhmfomxrfsageenlrozcfoaxdpmeayllvefioqhmflhwvrlmusougcuuswtstxdxpetloxwpqnanimexdyxjndehqhdqvuazxnneozujaqmbiqbwroyfayrpivztkyxeieygafkjxfzzphcqjoqnrzptknytgkxzchfzgfrflyywtzfyztiymitpyatnlciybywmyfsxmjvmmhjalambgzxiergkjoznseuibyguupkekspdwtlenvkjstoysgyjvhakdofntodrtaskzydputcylppgudwhvlfgupivuulrbvdtqetsgfsopcrnghpomvmueszyfqeipumkmzhbnxxkpubdxwmivvyivjdirqszttfqfliknvnizjwldbehetmqnrwjvqeetmmadirtdupoegwljfnrnesmaavjxhanobcvovrkcatjgqdwvmdikavblqhmdibytthichxlaxwyyoijxibivggkuckcjzgmnvllxcmpomqgwizalstxgkassobxlcmzzuemxctfgzilrkbgmsorpygjfrwtedmgjrfuhniciplgjcgbsctqzxlaqxyrymqmrfqqlkowyebevikquudlezezdshefhrucjssmfetyatfpqwgljtlysagjrsrzalaoypjfurccehapkxvdaezrpapsosigpwkmlgohcgkewcnfjtspnnjbkohtboxiqvevgyjjeckffclzuqcyovhkvzcoddzvhrsgjmvdgogpbkjpxzrdbioadeaianrrhtuorfpdmxkxitrfoekdfvlvxiwzerwkbweljilbhycgjijukyqyfhkuxaprstapvcuqgiusblitayeafehvtherxftyyokyfzobqfryancbkqlfvjmqvqmseyrolsdzgudbteehuteizzxpvempjhcrszeadincuvsohhjvasudrtpuhhjmfddspbihsnstbtqdgqdqxlkdlpxihztnciavbshnzptetrdheivmjqrytcpjssvallfmrgwzwzbvprxohgqckacftrubgronwsnqnmojgbahufxzwyqskbgatjffgktyxhlhjxuxrmwmqyemkyrrwarrkzqfqcakzrtatlvxncnpfcgzlbzqltrwpagcocptqxavtgjvdwzgpaijxpgbopvvutuhtbwscpqfcvkznlngjjhuvru..."

print(palindrome(A,0,len(A)-1))