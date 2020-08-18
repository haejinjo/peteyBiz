## Purpose
To help the love of my life out with very cool data analysis.

## You will need
  - a very basic fluency in navigating the command line
  - [Python](https://www.python.org/downloads/) (this tool was tested on Python version 2.7.16)
  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#:~:text=Before%20you%20start%20using%20Git,code%20and%20compile%20it%20yourself.) (usually pre-installed for Mac these days, but you will be prompted to install if not)

## How to Use
1. Open a command line interface using your application of choice (e.g. Terminal or PuTTY)
2. Navigate to the directory that contains your CSV file(s)
    - 🤷‍♂️ Don't know how? You won't need to know much for this tool, so [check out a basic tutorial](https://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855)!
    - **Hint:** `ls`, `cd`, and relative paths are your friends.
3. Clone this repository (repo, for short) once you've made it to your directory containing the relevant CSV file, like so:
    ```
    git clone https://github.com/haejinjo/peteyBiz.git
    ```
    - If you `ls`, you will notice that running this `git` command created a directory that wasn't there before! Let's look into it!
4. Navigate into the newly generated repo directory
    ```
    cd peteyBiz
    ```
5. Once in the repo directory, copy-paste your CSV file from this cloned repo's parent directory like so:
    ```
    cp ../yourFilenameShouldBeHere.csv .
    ```
    - Notice that the `cp` command takes two arguments: A source and a destination filepath.
    - As you might've discovered, `..` means the previous or parent directory and `.` means the current directory, the latter of which serves as the "destination" in this case.
6. Run my program using the `python` command:
    <pre>python addRowCounts.py -i <i>INPUT CSV FILE</i> -c <i>RELEVANT COLUMN NAME</i></pre>
    - **Note on `-i`:** Since you are already in the directory where a copy of your file lives, you can just type the filename itself as an argument
      - Example: `python addRowCounts.py -i someDataset.csv -c MAIDEN_NAMES`
      - Normally, you'd have to write out a relative path
    - **Note on `-c`:** Make sure you reproduce the *exact* name of the column whose counts you want inserted as a new column.
    - **Warning:** If you run this command multiple times on the same input CSV file, the output file will be **overwritten**.
7. If you `ls`, you should now see a CSV file ending in "_counted" that wasn't there before. 👋💩

<br />

🆘 Remember, if you ever forget what the program does or how it works, just run the following command:
```
python addRowCounts.py {-h | --help}
```
<br />

## Development Process

1. Create dummy CSV file data with 100 records based on what I glanced at on Petey's work using [this nifty tool](https://www.convertcsv.com/generate-test-data.htm), given the following inputs:
    - **Keywords:** hash, first, last
    - **Names:** hashed_user_id, first_name, last_name

2. Manually replace certain lines with duplicate rows (could've done this with some `Math.random` thing to automate the process, but I'm lazy and dumb sometimes)
    <details>
      <summary>👁️ Example Dummy CSV Data 👁️</summary>
      <pre>
      hashed_user_id,first_name,last_name
      7355f6711abfe07488b36d89e296e0a271248de4,Louise,Castillo
      6b8085fa5423665fd2a250ce1da7e423aa8ffccb,Cameron,Fletcher
      00d2e06e75391fb0e46d0b90655f40ee83f221a2,Mollie,Reese
      00d2e06e75391fb0e46d0b90655f40ee83f221a2,Mollie,Reese
      d5eff30b51825ea042dd3aed25db9e94bcbf5aaf,Mitchell,Hudson
      f43b4772d4527f43ca880c6b9d9039b5e3f5ffd7,Vera,Scott
      7feef75ac3c189116e69c5dd28e35ea931c84b8b,Patrick,Mack
      58641dba0625ab5617f0f76b255eb3142a7935f9,Hettie,Ward
      b585a94d357b8cd1f86963d3d618f9de0a114360,Minnie,Ramos
      e8480f7a22cba933d2fb014f8c2be92e692ad86f,Andre,Perez
      6c07449a6de00f03fe32a7b2f2114b29197362b5,Lester,Lane
      00d2e06e75391fb0e46d0b90655f40ee83f221a2,Mollie,Reese
      58641dba0625ab5617f0f76b255eb3142a7935f9,Hettie,Ward
      9d61ed249f87685c9e11f096d0c3a799ca0ea48b,Dorothy,Butler
      7d6ed67d85ee64fda624116bec9ae7da9eb64d0c,Leroy,Boone
      8c506576c593141f5fccdf8aaec144a6760a1680,Vincent,Singleton
      7feef75ac3c189116e69c5dd28e35ea931c84b8b,Patrick,Mack
      c63e64513775e93af81ab3839a809d5e8ff1ca77,Francisco,Waters
      3edb4823e792d621215e335715a03cadff8ab3a9,Ernest,Sims
      f4e40992f5cd461e33c77cd856156a88d48799db,Mabel,Vasquez
      35c7b045ea2be5f911a82ed610ac9770e1fa159e,Warren,Dixon
      e0440fc95d8da90a3d6ef8be29945d82cb67a3d8,Dollie,Wilkins
      5adbb03145da3f1e649b29791b1713d385854d51,Sadie,Maldonado
      0eee8c0b7d9baf3752ba6738b9554bd3036f3965,Antonio,Chambers
      52f0a6d9273983c70cebab81fed2543064773366,Leonard,Buchanan
      0edcedff4a55c3adf73342446a55f4bc0951c94f,Julian,Parsons
      2cb4ab1140da07a2a158f70219c593106bbb4799,Flora,Lucas
      7feef75ac3c189116e69c5dd28e35ea931c84b8b,Patrick,Mack
      6f085a70b9d0a4315ac976e35e1e4ddd091ea995,Nelle,Poole
      f90e04d1d2d3cf9d3cc06967eee504152fe02c81,Rosa,Jenkins
      f4e40992f5cd461e33c77cd856156a88d48799db,Mabel,Vasquez
      9adb7dd2541533201533da5f5982b2fd88e07e68,Lucile,Parks
      3ec9a427cc008d7c0aeca5134c38fb7e1ad53bf1,Maud,Harrington
      294195215e4a93c7ab08ddcf1c70f16ffe316fdb,Adele,Bennett
      841a7f7ff82d1504ce101c5c714cd1249e793ef3,Jon,Tran
      568febb6d8929400c4116fa86cbc6fd061e0277e,Julia,Frazier
      39969d39a41111c6810c72ae55a5a80dedda0ad9,Leo,Gomez
      a1ce14e19e4fa00b02912b258e1997f958964b5e,Ida,Morgan
      3cdbdf539d6a1c4573b1432beb0c22defddd54ee,Irene,Spencer
      196dfdef48ab074c6af49ddf8c4c979ef420ef38,Juan,Lowe
      68973378b3211fb1aff7bfa9feb6bd49962bf8ee,Delia,Myers
      b4774cbded39aeb304051fba9a0d7b735c9a3db2,Charlie,Hardy
      89e40a5debc16f5e9a53e5359f2d63b518cad693,Clyde,Shelton
      3b54fb98cc6b6a1f02d4c7de6acfafd189de486e,Virginia,Warner
      a11ab8c0bf8ff15e6d6fe5217f9dfb95143c5b9e,Roger,Tate
      31a4857a1a57690293555793c6a1d525e5ce86f1,Leon,Henry
      5d0e33b618666ad0d21333c03f175f993f6aaf42,Winifred,Burgess
      5b09fd0a564f7af9b76d7733834745481ec9423d,Seth,Roy
      2c26eeab240290ea3232147057cf88cccc726ebe,Edna,West
      eab4bdbb818f2b55b59a0db64326edc8c6a9ea32,Irene,Powers
      416c5d812f55873533e6ef9aac5ddf8a34ad178e,Emily,Cortez
      61bd659b036b79c3df1de83508fbef7d673659cc,Wayne,Webster
      58641dba0625ab5617f0f76b255eb3142a7935f9,Hettie,Ward
      58641dba0625ab5617f0f76b255eb3142a7935f9,Hettie,Ward
      f335fee4e96916b6cfa436e1d31472420482b870,Marian,Wise
      e828571433842e54e92ad2c8914899b079690d14,Fanny,Baker
      61b1b6752deffffcc37c5012ecdec29221ae50c9,Grace,Thompson
      99668d2e5a1403be3ac9d974fc9cf9921aaaf17f,Jeff,Chapman
      eee74b5ba2e378640c1f1744db6e1e10611b969f,William,Myers
      6586f60a7a40ed8706d9eeb9afdd4bdfbd8cd86f,Darrell,Wilkins
      d0618d5882c0e905653000350b3d7097bf576986,Erik,Dawson
      498ffe5b54315931eb6d7b79c2c4ccf03e2b2f39,Timothy,Little
      277f876145316ce20237bf487ab7424f39c40378,Keith,Guzman
      53f8057cd1f3a8edf3bc50666fe1723b1ab97e66,Lucile,Stokes
      a40203f933f354bfbae63dd6886772b2ae31cacd,Jessie,Wade
      4acb511cfbc625f5744dd216485a2922ffb7057a,Mark,Yates
      f8bb2809aaf3835724bbf193bf37138c32b25270,Eleanor,Munoz
      5419069fe539567f847485e8f4ec3fea3787d04b,Annie,Black
      ec1401eff8eb0df7760cad3984289ab357fc3b2c,Chase,Richards
      d54718af65b2850e0ad35b3003ef01c4153c2b95,Maggie,Higgins
      7feef75ac3c189116e69c5dd28e35ea931c84b8b,Patrick,Mack
      1dd1c77de058fbf25bf736b2445a9bf36c67d88c,Luis,Hughes
      7feef75ac3c189116e69c5dd28e35ea931c84b8b,Patrick,Mack
      58641dba0625ab5617f0f76b255eb3142a7935f9,Hettie,Ward
      999a480139259d9cebeced7798199b9fe2fe3ffe,Anthony,Carlson
      4905443a2d4ceb29a67680f18f53d3cca4c2cd96,Frances,Ross
      58641dba0625ab5617f0f76b255eb3142a7935f9,Hettie,Ward
      2029df4d426b57f47d299314a61df7f1ec2ca574,Leon,Baldwin
      8b3ba5832652b7f434e212721dee7b7ed62a52de,Josephine,Bass
      29b45977bc48fdf4ebb2c8aa71ac3724eb7f8873,Marvin,Bailey
      00d2e06e75391fb0e46d0b90655f40ee83f221a2,Mollie,Reese
      8be1358a2441834b1bd4c48f9c5160c0a562eebc,Jack,Watson
      7feef75ac3c189116e69c5dd28e35ea931c84b8b,Patrick,Mack
      b3d41c0b547f5924e4edb3a69ea6a9223b9363b5,Bradley,Harrison
      58641dba0625ab5617f0f76b255eb3142a7935f9,Hettie,Ward
      78ea1f741b3618af9396c637d28d807e9250d6f9,Thomas,Wallace
      00d2e06e75391fb0e46d0b90655f40ee83f221a2,Mollie,Reese
      90f72e91418d6c1fc618a90aed0aa29236539c17,Max,Medina
      1cfc5e74b072e5e50a1423d6c8761fc127fb9a65,Christopher,More
      69e676e6b0774534eba6967cad95e92a64091631,Harriett,Fitz
      7c81b4077cef9ca5ef0e5184bbaef35d05eaf1c0,Vera,Reese
      7feef75ac3c189116e69c5dd28e35ea931c84b8b,Patrick,Mack
      6ea1ceeb4d32f8bb24ac257ede4b770e7d50e9f3,Jay,Curry
      7feef75ac3c189116e69c5dd28e35ea931c84b8b,Patrick,Mack
      f4e40992f5cd461e33c77cd856156a88d48799db,Mabel,Vasquez
      1af4ea10c66dac8b5e5420f583ae6df0a343fbaf,Wayne,Day
      f4e40992f5cd461e33c77cd856156a88d48799db,Mabel,Vasquez
      056dc39a305fe89371841a0e62e1d1fa05ab2fc1,Seth,Beck
      695128a9604c92f4222a3b1de1cd76765ff26359,Sue,Collier
      00d2e06e75391fb0e46d0b90655f40ee83f221a2,Mollie,Reese
      </pre>
    </details>
    
    - Hettie should appear in 7 records
    - Mabel should appear in 4 records
    - Mollie should appear in 6 records
    - Patrick should appear in 8 records

3. Read and process data from an input file using `csv` Python package.

4. Write the data from the input file with 1 new column inserted, using `csv` Python package.
    - This new column should represent the number of instances of the record immediately to its left

4. Enable command line inputs using `argparse` (with auxiliary use of `os` and `sys`) for that sweet UX
    - Path to csv input file
    - Column name in question