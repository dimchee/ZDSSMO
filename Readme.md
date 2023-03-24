# Bookaton

## Quick Start

You don't need to, but i highly recommend installing [github cli](https://cli.github.com/).
First, create new github repository from [template](https://github.com/dimchee/Bookaton):
```sh
$ gh repo create --public --clone --template https://github.com/dimchee/Bookaton <repo_name>
```
- Now you should have almost empty directory.
- First, we need to modify permissions on created repository: 
  - Navigate to it's page  in browser,
  - Navigate to `Settings` pane, then under `Actions` tab go to `General`.
  - Under `Workflow permissions` select `Read and write permissions`.
  - Check `Allow GitHub Actions to create and approve pull requests` box.
  - Save changes.
  - Navigate back to repository page
- If you don't want to be spamed by notifications, Click on `Unwatch` button and
select `Ignore`
<!-- - You are ready to add Your `.pdf` File to the root of repository, and name -->
<!-- it `Book.pdf`, for example like this: -->
<!-- ```sh -->
<!-- mv <book_name>.pdf <repo_name>/Book.pdf -->
<!-- cd <repo_name> -->
- You are now ready to add your Book. Scaned book should be prepared as *one* directory of `JPEG` images
- To be able to split Book, install [Bookaton Splitter](https://github.com/dimchee/BookatonSplitter). 
    Navigate to it's repository, then follow `Quick Start` instructions.
- Now you should have `Parts` directory with book splitted to several `pdf` files.
- Add `Parts` directory to your repository
```sh
$ mv Parts <repo_name>
$ cd <repo_name>
```
- Now commit changes, and push
```sh
git add Parts/
git commit -m "Add Parts"
git push
```
- Now we should be able to create issues for splitted book
    - Navigate to repository's page in browser
    - Navigate to `Actions` pane, then on left select `Create Issues from Parts` tab
    - On right should be button `Run workflow`, click on it
    - This will take a while, you can track progress in `Actions` tab, or in `Issues` pane directly
- Now you should have everything prepared.
- Commenting LaTeX Code directly to any Issue labeled with LaTeX will 
    add your work to Repo, and automaticaly release final `.pdf`.

## Usage (contributor)
- You can work in any LaTeX editor you like, but it is recomended to use [overleaf](https://www.overleaf.com).
- Navigate to `Issues` pane and from option `Sort` select `Oldest`, then pick an `Issue`
- Comment `Assign me` to assign yourself selected `Issue`
- Select issue with label LaTex, copy this [this template](https://www.overleaf.com/read/yzxzjbfjcxjx), and write some LaTeX
- Or select issue with label Tikz, copy [this template](https://www.overleaf.com/read/pfsyfmmbcfwq), and write some Tikz
- Paste your LaTeX to Issue you were working on, and everything else should happen automagicaly!
- Warning: LaTeX submission comments are detected by `\documentclass{` begining
- Warning: Don't add any definitions in Issues, we are extracting what is between 
`\begin{document}` and `\end{document}`.
- If you don't want to be spamed by notifications, navigate to repository page and click on `Unwatch` button and select `Ignore`


Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
