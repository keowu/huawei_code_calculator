<h1 align="center"> Huawei Code Calculator </h1>
<p align="center">
Universal calculator to calculate security codes for Huawei products, to obtain privileged access.
</p>

<h2 align="center">About the algorithm</h2>
<p align="center">
The algorithm was extracted from Vivo's router firmware, in which it is blocked for personal use, the algorithm was extracted from a router update, and was analyzed using reverse engineering tools, and reconstructed entirely by me using Ghidra 9.2, as this algorithm is possible to release special access on routers and Huawei products for its generation, the calculation is based on the IMEI with an MD5 hash and a table, when using it remember to use your IMEI correctly to obtain the UNLOCK calculation (If you want to unlock) and FLASH (If you want to extract the contents of the microcontroller), hint the firmware is compacted, use tools like binwalk after reading by pinout using the datasheet.
</p>

<h2 align="center">How to run to get your code</h2>
<h3 align="center">With python installed</h3>
<ul align="center">
    <li>1 - Have python installed on your computer, please use version 3.</li>
    <li>2 - Modifique onde possui um comentário dizendo "YOUR IMEI GO HERE"</li>
    <li>3 - To get your IMEI you can look under your router, or if it is a cell phone you can enter the following code on your phone:<strong>*#06#</strong> this is a universal standard used by developers or police to obtain the IMEI unique identification number of your Smartphone / Router.</li>
    <li>4 - After just run normally with (python main.py) and obtain the two keys, the first one from UNLOCK and the second one from Flash.</li>
</ul>
<h3 align="center">Without python installed</h3>
<ul align="center">
    <li>1 - Use an IDE Online, Google is your friend, search for it in the following query "Python 3 IDE ONLINE"</li>
    <li>2 - Copy all content from the main file and paste it into your Online IDE</li>
    <li>3 - To get your IMEI you can look under your router, or if it is a cell phone you can enter the following code on your phone:<strong>*#06#</strong> this is a universal standard used by developers or police to obtain the IMEI unique identification number of your Smartphone / Router.</li>
    <li>4 - After just execute normally pressing the common run button for these types of IDE'S and obtain the two keys, the first one from UNLOCK and the second one from Flash.</li>
</ul>
<h2 align="center">Which devices are compatible with your algorithm?</h2>

| #1  | #2  | #3  | #4  | #5  | #6  |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
|  Huawei E171 | Huawei E188  | Huawei E367  | Huawei E1550  |  Huawei E166G |  Huawei E2010 |
| Huawei E172  |  Huawei E196 | Huawei E368  |  Huawei E1551 | Huawei E1690  |  Huawei S4011 |
| Huawei E173  |  Huawei E216 | Huawei E369  | Huawei E1552  | Huawei E1692  | Huawei E1731  |
|  Huawei E176 | Huawei E219  | Huawei E372  | Huawei E1553  | Huawei E1820  | Huawei E3131  |
|  Huawei E177 |  Huawei E220 | Huawei E392  |  Huawei E155X | Huawei E1823  | Huawei E630+  |
| Huawei E180  |  Huawei E226 | Huawei E397  |  Huawei E156C |  Huawei E182E | Huawei E660  |
| Huawei E181  |  Huawei E22X | Huawei E398  | Huawei E156G  | Huawei E1831  | Huawei K3517  |
| Huawei E182  | Huawei E230  | Huawei E612  | Huawei E156X  |  Huawei E1800 |  Huawei K3520 |
|  Huawei E166 | Huawei E270  |  Huawei E618 | Huawei E1609  | Huawei E1803  |  Huawei K3710 |
|  Huawei E155 | Huawei E271  |  Huawei E620 | Huawei E160E  |  Huawei E180G | Huawei EG162  |
| Huawei E156  | Huawei E272  | Huawei E630  | Huawei E160G  | Huawei E180S  |  Huawei EG602 |
| Huawei E158  | Huawei E303  |  Huawei E660 | Huawei E1612  | Huawei E169G  | Huawei EM770  |
|  Huawei E160 |  Huawei E352 | Huawei E800  | Huawei E1615  | Huawei E170G  | Huawei EG602G  |
|  Huawei E170 | Huawei E353  | Huawei E870  | Huawei E1616  |  Huawei E1780 | Huawei EG162G  |
| Huawei E161  | Huawei E355  |  Huawei E880 |  Huawei E1630 | Huawei E172G  | Huawei UMG181  |
|  Huawei E169 | Huawei E357  |  Huawei E968 |  Huawei E1632 | Huawei E1762  | Huawei HiLink  |
<p align="center">
And many others, please try even if your device / model is not here and if it works open an issue with the name / model to be added to the list.
</p>

<h2 align="center"> How can I contribute?</h2>
<p align="center">Finding more compatible devices and reporting, and leaving a like in my repository and helping with dissemination.</p>

<h2 align="center">Why Python and not C?</h2>
<p align="center">Because I want the algorithm and logic behind it, and I didn't want something big to need to include a good lib of md5 like openssl.</p>

<h2 align="center">I hope this repository is useful for someone with blocking problems, or has been able to exchange knowledge.</h2>

