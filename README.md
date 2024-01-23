# SEFSC-FATES-documentation-jekyll-skeleton

A template/skeleton repository that can be used as a starting point to create a new SEFSC FATES GitHub Documentation Site for deployment to https://sefsc.github.io/.

### Getting Started

See online documentation for working with this repository at: https://mattgrossi-noaa.github.io/SEFSC-FATES-documentation-jekyll-skeleton/howto.html 

_Delete the 'SEFSC-FATES-documentation-jekyll-skeleton' heading above, delete this comment and the remaining text above, modify the remaining README content below to be relevant to your documentation site, and make sure to change the Jekyll site configuration files according to the instructions in the HOWTO/documentation. Once your site content looks ready to go, it can be pushed to the [SEFSC GitHub Organization](https://github.com/sefsc){:target="_blank" rel="noopener"} to be deployed._

# SEFSC FATES Documentation Site: ___________

**Site URL:** https://mattgrossi-noaa.github.io/SEFSC-FATES-documentation-jekyll-skeleton or https://sefsc.github.io/SEFSC-FATES-documentation-jekyll-skeleton

### Deploying site locally
Requirements:
* Ruby
* bundle
* Jekyll

Clone this repository:
```commandline
git clone https://github.com/MattGrossi-NOAA/SEFSC-FATES-documentation-jekyll-skeleton.git
```
Rename the resulting `SEFSC-FATES-documentation-jekyll-skeleton` directory to a name of your choice, and follow further [Getting Started](https://mattgrossi-noaa.github.io/SEFSC-FATES-documentation-jekyll-skeleton/howto.html#getting-started) section in the HOWTO documentation.

To build the site, in your local renamed repo directory, run:
```commandline
bundle exec jekyll serve --config _config.yml --watch --verbose --incremental
```
This will deploy a website at: http://127.0.0.1:4000/SEFSC-FATES-documentation-jekyll-skeleton/.

Further instructions for modifying and configuring your site can be found in the  [Editing and configuring your documentation site](https://mattgrossi-noaa.github.io/SEFSC-FATES-documentation-jekyll-skeleton/howto.html#editing-and-configuring-your-documentation-site){:target="_blank" rel="noopener"} section of the HOWTO.

#### Editing site content

Make edits to the appropriate Markdown files in `_docs/`. 

If changing headers and menus, stop the running server by entering `ctrl-c` in the terminal. Then run:
```commandline
bundle exec jekyll clean
```
Then build the site again:
```commandline
bundle exec jekyll serve --config _config.yml --watch --verbose --incremental
```
And review at http://127.0.0.1:4000/SEFSC-FATES-documentation-jekyll-skeleton/

More settings changes, including renaming the site URL to match your new repository name and replacing "SEFSC-FATES-documentation-jekyll-skeleton", should be made by editing the `_config.yml` and `_config_dev.yml` files in the repository root. See the [Edit Your Site Content](https://mattgrossi-noaa.github.io/SEFSC-FATES-documentation-jekyll-skeleton/howto.html#step-2-edit-your-documentation-site-content){:target="_blank" rel="noopener"} section of the HOWTO.