---
title: Creating a Jekyll documentation skeleton template for the Southeast Fisheries Science Center
summary: A technical overview of customizing the theme, creating the skeleton template, and merging the two together
tags: [getting_started, about, overview]
toc: false
search: exclude
---

# About this project

This page is for informational purposes only. It's technical. It captures the process to create the GitHub Pages [SEFSC-FATES-documentation-jekyll-skeleton](https://mattgrossi-noaa.github.io/SEFSC-FATES-documentation-jekyll-skeleton/index.html){:target="_blank" rel="noopener"} repository template for use within the NOAA Fisheries Southeast Fisheries Science Center. Nothing herein needs to be repeated to create a specific documentation page in a GitHub repository. These steps are *only necessary if one desires to create a new **template*** of the same format and functionality – for example, if a different Financial Management Center (FMC) desires to create their own custom template. Instructions for creating an actual documentation page using the theme are provided in [Getting started with SEFSC Jekyll Documentation Theme Skeleton](https://mattgrossi-noaa.github.io/SEFSC-FATES-documentation-jekyll-skeleton/howto.html){:target="_blank" rel="noopener"}.

The [NOAA Fisheries](https://www.fisheries.noaa.gov/){:target="_blank" rel="noopener"} [Southeast Fisheries Science Center (SEFSC)](https://www.fisheries.noaa.gov/about/southeast-fisheries-science-center){:target="_blank" rel="noopener"} [Fisheries Assessment, Technology, and Engineering Support (FATES) Division](https://www.fisheries.noaa.gov/about/fisheries-assessment-technology-engineering-support){:target="_blank" rel="noopener"} is actively developing a suite of new, innovative machine learning models designed to increase data processing efficiencies across the Center’s mission portfolio. These projects include, but are not limited to, automating the processing of Gulf and South Atlantic video survey data to derive species counts, automating aging of Gulf and Atlantic menhaden and red snapper, and automating the derivation of fish lengths from stereo video. These models were developed in Python using open-source libraries (e.g., PyTorch, cudatoolkit, Torchvision, and scikit-learn) by partners through the [NOAA Northern Gulf Institute (NGI)](https://www.northerngulfinstitute.org/){:target="_blank" rel="noopener"} and the [Cooperative Institute for Climate, Ocean, and Ecosystem Studies (CICOES)](https://cicoes.uw.edu/){:target="_blank" rel="noopener"} and are or will be maintained on the [SEFSC Organization GitHub account](https://github.com/SEFSC){:target="_blank" rel="noopener"}.

Introducing new computer models into the Center’s data processing procedures necessitates adequate documentation so that the end users will know how to install and execute the models in operational use. Indeed, all computer models and software should be documented by the developers before being released to the intended end user. In the absence of a universally accepted documentation template for use within the SEFSC, NOAA Fisheries, or even NOAA at large, staff across NOAA have established their own approaches and templates of varying degrees of complexity based on their immediate needs. Some examples of these solutions are summarized in Table 1 along with notable strengths and weaknesses of each.

Several features were prioritized when selecting a platform for SEFSC FATES documentation:
1. Content version control
2. Documentation existing alongside the model source code
3. Minimal learning curve for populating and maintaining content
4. Layout and formatting customization to align with agency visual branding requirements  

<table style="font-size:small; width:75%; align:center; margin-left:auto; margin-right:auto;">
  <caption style="text-align:left"><hr><b>Table 1:</b> A variety of resources have been used across NOAA for documenting procedures or applications, each having its own advantages and disadvantages. In the absence of guidance or directives, users currently select the approach best suited to their needs. This non-exhaustive list provides some examples of documentation solutions.</caption>
  <tbody>
    <tr>
      <th style="text-align:center">DOCUMENTATION SOLUTION</th>
      <th style="text-align:center">ADVANTAGES</th>
      <th style="text-align:center">DISADVANTAGES</th>
    </tr>
    <tr>
      <td valign="top"><b>Microsoft Word</b> or <b>Google Doc</b></td>
      <td valign="top">
        <ul>
          <li>Creation is straightforward</li>
          <li>Easily converted to PDF</li>
          <li>Software readily available to NOAA staff</li>
        </ul>
      </td>
      <td valign="top">
        <ul>
          <li>Not co-located with software</li>
          <li>Document owner often retains ownership</li>
          <li>Difficult to share publicly</li>
          <li>No version control</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td valign="top"><b>Quarto webpage made with R</b> <br><br> Example: <a href="https://nmfs-opensci.github.io/NOAA-quarto-book/">Quarto webpage with book layout</a></td>
      <td valign="top">
        <ul>
          <li>Consistent formatting across implementations</li>
          <li>Hosted on GitHub Pages (gh-pages) alongside the software itself</li>
          <li>GitHub version controlled</li>
          <li>Template and setup guidance available via NOAA Fisheries Open Science initiative</li>
        </ul>
      </td>
      <td valign="top">
        <ul>
          <li>Learning curve with Markdown and HTML to populate content</li>
          <li>Learning curve with R and RStudio to develop content locally</li>
          <li>Learning curve with GitHub Pages and GitHub Actions if customization is needed</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td valign="top"><b>GitHub respository Wiki</b> <br><br> Example: NOAA IOOS <a href="https://github.com/ioos/ioosngdac/wiki/DAC-Documentation">National Glider Data Assembly Center (NGDAC) Documentation</a> (<i>archived</i>)</td>
      <td valign="top">
        <ul>
          <li>Consistent formatting across all GitHub repositories (repos)</li>
          <li>Connected to the repo in which application is hosted</li>
          <li>Public accessibility follows repo settings</li>
          <li>No local software requirements</li>
        </ul>
      </td>
      <td valign="top">
        <ul>
          <li>Limited functionality</li>
          <li>No ability to customize appearances, layouts, etc.</li>
          <li>Limited version control</li>
          <li>Learning curve with Markdown and HTML to populate content</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td valign="top"><b>GitHub Pages webpage</b> <br><br> Example: NOAA <a href="https://ioos.github.io/">IOOS Documentation Portal</a></td>
      <td valign="top">
        <ul>
          <li>Consistent formatting across implementations</li>
          <li>Can be customized for the organization with optional centralized format control</li>
          <li>Easily templated to minimize learning curves</li>
          <li>Hosted on gh-pages within the repo in which the application is hosted</li>
          <li>Full GitHub version control</li>
          <li>Template and setup guidance created by IOOS</li>
        </ul>
      </td>
      <td valign="top">
        <ul>
          <li>Learning curve with Markdown and HTML to populate content</li>
          <li>Advanced customization requires knowledge of gh-pages, GitHub Actions, CSS, and other languages</li>
          <li>Initial setup can be challenging</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>





Google Docs, though straightforward to create and widely used across NOAA, present too many challenges. File ownership is a perpetual problem, with the original author often retaining ownership and files getting lost in staffing changes. Without preserving documents’ URLs, sharing access permissions, and transferring ownership when needed, these files often get lost or are not known to exist by new staff. There is also a tendency for documents to perpetually stay in “draft” version, which casts doubt on the accuracy of the content and whether or not a final version exists. A far better solution is one that is connected to GitHub where the model code itself is hosted and maintained. One option is [GitHub Wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis){:target="_blank" rel="noopener"}, which can be created for any repository and have been widely used by [NOAA Integrated Ocean Observing System (IOOS)](https://ioos.noaa.gov/){:target="_blank" rel="noopener"} programs, such as the [original National Glider Data Assembly Center documentation](https://github.com/ioos/ioosngdac/wiki/DAC-Documentation){:target="_blank" rel="noopener"} page. Yet these Wikis offer limited version control and customization aside from the actual content. [GitHub Pages](https://pages.github.com/){:target="_blank" rel="noopener"}, a service that allows a project website to be freely hosted for any repository, offers a more comprehensive assortment of options and flexibilities including customizable themes that can be tailored to agency visual branding, the ability to control this theme in one repository and use it across any number of documents, full version control, and the option of creating a [template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository){:target="_blank" rel="noopener"} that can be easily duplicated and integrated into new projects.

# Custom SEFSC Theme for GitHub Pages Documentation Sites

The decision to use GitHub Pages (gh-pages) for SEFSC FATES documentation was inspired by its widespread use within IOOS. Correspondence with an IOOS data management analyst revealed that all IOOS documentation pages are either already utilizing GitHub Pages (gh-pages) or are in the process of migrating to it because of the strengths listed in Table 1. IOOS hosts a [Documentation Portal](https://ioos.github.io/){:target="_blank" rel="noopener"} within their organizational GitHub account to compile all products and projects documentation in one central location.

IOOS maintains consistent formatting, appearance, and functionality across all pages by using a single [Jekyll theme](https://jekyllrb.com/){:target="_blank" rel="noopener"} for all page builds. The selected theme is a [Jekyll Documentation Theme](https://idratherbewriting.com/documentation-theme-jekyll/){:target="_blank" rel="noopener"} forked from the [source repo](https://github.com/tomjoht/documentation-theme-jekyll){:target="_blank" rel="noopener"} and customized by IOOS. Some of the most noticeable modifications include:

- IOOS header logo added and colors changed in accordance with branding guidelines
- Page footer with appropriate links and contact information
- Common horizontal navigation bar with IOOS-related links and resources
- “Behind the scenes” configurations that govern how the website works

This theme is simply a GitHub repository containing the necessary configuration files, scripts, and visual branding to provide the underlying structure of a documentation web page. IOOS implements this theme in all documentation pages through the use of [GitHub submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules){:target="_blank" rel="noopener"}, the details of which are beyond the scope of this document but, in short, allow *theme files* to be contained in their own repository and then embedded into a separate repository that contains the *content files* for the web page. There are several advantages to this. First, it means that individuals seeking to write documentation do not need to worry about creating a website. The “guts” already exist. Second, the same theme repository can be embedded into an infinite number of documentation repositories, providing a consistent look and feel across all of them. Finally, the theme can be modified at any time by the owner (for example, the IOOS Program Office) and those changes can easily be propagated through to every other site that uses the theme by simply pulling the changes into each of the respective repositories.

A new “[documentation-theme-jekyll](https://github.com/MattGrossi-NOAA/documentation-theme-jekyll){:target="_blank" rel="noopener"}” repository was created for SEFSC FATES by forking the IOOS version and adapting the appearance to the Center’s needs. Colors were modified to align with NOAA Fisheries Brand Standards and the IOOS logos were replaced with NOAA Fisheries and Southeast Fisheries Science Center branding. The navigation bar and configuration files were updated as appropriate and mentions or connections to IOOS were edited and redirected to SEFSC. By forking this repository from IOOS (instead of cloning it), it retains its lineage to the original source repo and can therefore easily incorporate future changes made anywhere upstream. In this way, consistency can exist between IOOS and SEFSC documentation pages while the appearances remain tailored to the respective organizations. The sequential steps taken to create this theme repository are described next.

## Creating and setting up a custom “documentation-theme-jekyll” repository

### Step 1: Fork the IOOS repository

This is done on the GitHub website and assumes the user already has a GitHub account and is signed in. These steps will duplicate the IOOS repository (repo) into that user’s account.

1. Navigate to the [ioos/documentation-theme-jekyll](https://github.com/ioos/documentation-theme-jekyll){:target="_blank" rel="noopener"} repo in a web browser

2. Click the triangular down arrow next to the “Fork” button at the top right of the page and select “Create a new fork”

3. Select an owner for the new repo from the dropdown list, if available. If you belong to a GitHub organization, such as SEFSC, you will have the option of assigning ownership of the repo to the organization or owning it yourself.

4. Keep the repo name the same (“documentation-theme-jekyll”) –- *recommended to more easily trace lineage history, but not necessary*

5. Modify the description, if desired. The recommendation is to specify what the repo is (in one or two sentences at most) and where it was forked from. For example:

    > *A Jekyll-based theme designed for documentation and help systems. Forked from NOAA IOOS (https://github.com/ioos/documentation-theme-jekyll), which itself was forked from source repo: https://github.com/tomjohnson1492/documentation-theme-jekyll for IOOS DMAC documentation use.*

6. Unselect “Copy the main branch only” box. This repo currently has two branches: the **main** branch contains the bulk of the theme, and a second **navbars** branch controls the horizontal navigation bar. Both are needed and more may be added in the future.

7. Click “Create fork”

### Step 2. Clone the repository locally for easier editing (optional)

Cloning the repository onto your local machine can make editing files easier, especially formatted script and configuration files for which GitHub has only limited built-in dynamic formatting capabilities. The following steps assume [GitHub](https://desktop.github.com/){:target="_blank" rel="noopener"} and [Git Command Line Interface (CLI)](https://cli.github.com/){:target="_blank" rel="noopener"} are installed locally.

1. Create a directory on your local machine where the contents of the repo will be downloaded. For example:

   ```bash
   .
   └── Documents/
    └── gh-pages/    
   ```

2. In the web browser, navigate to the repo you just created

3. Click the green “< > Code” button and copy the web URL of the repo

4. Back on your local machine, open a terminal window or Command Prompt, navigate to where the repo is to be downloaded, and type

   ```bash
   git clone <URL>
   ```
   where <URL> is the web URL from step 3.

5. Press enter. The repo will now be downloaded to your local machine.

Alternatively, after step 1, either use the “Open with GitHub Desktop” or the  “Download ZIP” options shown above to download the repo. Be sure to unzip it if you retrieve it this way.

### Step 3: Customize the navbar

First, customize the navigation bar because it will be needed later. This is the horizontal banner across the top of the page with drop down menus containing external links, resources, etc.

1. Switch to the **navbars** branch on your local computer:
   
   ```bash
   git checkout navbars
   ```
   
   The theme files should now disappear and there will be only one file, `topnav_ioos.yml`

2. Rename this file replacing “ioos” as appropriate. For example, `topnav_sefsc.yml`. Remember this new filename, as it will be needed later. Commit the changes, *e.g.*:
   
   ```bash
   git commit -m "Rename for SEFSC"
   ```

3. Open this yml file in a text or code editor and change the drop down menus and links *being careful to retain file formatting, indentation, and syntax*. Ignore the first top level “title” field (“Topnav dropdowns” in the sample below). The next “title” field immediately following the “folders” call controls the name of the drop down menu. Under this, the “folderitems” are the links within that menu, with “title” setting the readable text that will be displayed and “external_url” specifying the web address of the hyperlink. These blocks of fields are repeated as needed.

   ```yml
   #Topnav dropdowns
   topnav_dropdowns:
   - title: Topnav dropdowns
     folders:
       - title: IOOS Resources
         folderitems:
          - title: IOOS Homepage
            external_url: https://ioos.noaa.gov
          - title: IOOS.us National Data Portal
            external_url: https://ioos.us
          - title: Data Standards & Requirements for IOOS Grantees
            external_url: https://ioos.noaa.gov/data/data-standards
   ```

   Note that each menu can contain as many links as desired, and, theoretically, the page can contain as many drop down menus as desired. Keep in mind, however, that there is limited space on a computer screen, so the number of menus is best limited to four or five, depending on how long the names are. This may require some trial and error.

### Step 4: Push the changes back to GitHub

Once all the changes above have been made, you are ready to push them up to the remote repo on GitHub so that they will be available for use in a documentation page. (Note: This page is not a GitHub tutorial. Many resources for Git exist online, if needed.)

1. Add the changes to commit

   ```bash
   git add <navbar_filename>.yml   
   ```

   where `<navbar_filename>` is the file name assigned in [Step 2](#step-2-clone-the-repository-locally-for-easier-editing-optional) above.

2. Commit the changes using a descriptive commit message

   ```bash
   git commit -m "Customize navbar for SEFSC"
   ```

3. Push to remote navbars branch on GitHub

   ```bash
   git push origin navbars
   ```

### Step 5: Customize the theme as needed

A number of changes were made to adapt the custom IOOS theme to SEFSC. The list that follows is not exhaustive, nor are all of the steps spelled out for each task. This is because much of this customization was accomplished through repeated trial and error. For more details, see the [commit history entry](https://github.com/MattGrossi-NOAA/documentation-theme-jekyll/commit/15209a9711dbf9be6e4566f8d9e585eb0bab48c5){:target="_blank" rel="noopener"} that captured most of these changes. Comments were added to the files in many places, but not as faithfully as it should have been done. Note that these changes can theoretically be done in any order.

1. First, return to the **main** branch of the repository
   
   ```bash
   git checkout main
   ```

2. In the `css` subdirectory, rename `theme-ioos.css` to `theme-sefsc.css`

3. Upload NOAA Fisheries logos to `images` subdirectory

4. Upload “favicon.png” image to use as an icon in the web browser tab.

5. Customize the page footer in `_includes/footer.html`:

   a. Update the external URLs. Opted to replace

    1. https://ioos.noaa.gov → https://noaa.gov
    2. https://ioos.us → https://fisheries.noaa.gov 
    3. Add URL for SEFSC
   
   b. Update Social Media URLs

   c. Update address and phone number with SEFSC Headquarters info
   
   d. Update “mailto” email address for “Contact Us” button

6. In `_includes/head.html`, change the theme CSS file to be used

   a. `…/theme/css/theme-ioos.css` → `.../theme/css/theme-sefsc.css`

   b. `.../theme/images/favicon.ico` → `../theme/images/favicon.png`

7. Customize the site header in `_includes/topnav.html`

   a. Add a new “avatar-container-layout” container to create a two-column header

   b. Change hyperlink URL from IOOS to NOAA Fisheries

   c. Change icon to be used:

      1. `.../theme/images/IOOS_Emblem_Tertiary_B_RGB.png` → `.../theme/images/NOAA_FISHERIES_logoH.png`
      2. Add “NOAA Fisheries” as alternative text if header logo cannot be found

   d. Add “Southeast Fisheries Science Center” text with hyperlink to header (note that this may be replaced with an image logo in the future)

8. Customize website colors in `css/customstyles.css` to align with NOAA Fisheries Brand Standards

9. In `css/lavish-bootstrap.css`:

   a. Add CSS code for new “avatar-container-layout” container to support two-column header
   
   b. Add CSS code to support text in header

   c. Adjust and set sizes, display settings, paddings, *etc.* to set the position of all header bar components including logos and text

### Step 6: Push the changes back to GitHub

Follow the same procedure as in [Step 4](#step-4-push-the-changes-back-to-github) above but be sure to push to the **main** branch this time. (Note that it is best practice to make many small commits rather than fewer large commits, like this. Commit as often as you see fit while carrying out the steps above.)

   ```bash
   git add .
   git commit -m "Customize theme files for SEFSC"
   git push origin main
   ```
## What this theme repository provides
The repo just created provides the layout and formatting customization that allows all documentation pages to have the same look and feel while aligning with agency visual branding requirements. This is one of the biggest advantages of using gh-pages for documentation. This repo is also key to minimizing the learning curve needed to actually create a documentation page because the creator of a new documentation page does not need to modify anything outlined above. In fact, this author *should not* make any changes to these theme files. The theme itself should be managed by a single person (or team of people) responsible for making decisions about how the pages should appear and function. And, as has been seen, everything in the repo is version controlled by virtue of being a GitHub repository.

# GitHub Pages Documentation Template

The next step is to create another repository to serve as a template repo for all documentation pages moving forward. NOAA IOOS again provides a starting point for this, a repo called “[ioos-documentation-jekyll-skeleton](https://github.com/ioos/ioos-documentation-jekyll-skeleton){:target="_blank" rel="noopener"}” that also [demonstrates the web page](https://ioos.github.io/ioos-documentation-jekyll-skeleton/){:target="_blank" rel="noopener"} and explains how to use the template. This repo contains one or more Markdown (.md) files that contains the content of the page. The user need only replace the placeholder text with the necessary sections, headers, and narratives. In the case of a model source code already hosted on GitHub, this template can be added to the existing repo as its own branch. As with the theme files, everything in this skeleton repo is fully version controlled. The creation and customization of the IOOS documentation skeleton repo for SEFSC Fates is discussed next. Note that there is more than one way to do this – even shorter methods requiring fewer steps – but the procedure below is what was followed in this particular instance.

## Creating a documentation skeleton repository

### Step 1: Clone the IOOS skeleton repository locally

This is done on the GitHub website and assumes the user already has a GitHub account and is signed in. These steps will duplicate the IOOS repository (repo) into that user’s account.

1. Navigate to the [ioos/ioos-documentation-jekyll-skeleton](https://github.com/ioos/ioos-documentation-jekyll-skeleton){:target="_blank" rel="noopener"} repo in a web browser

2. Click the green “< > Code” button and copy the web URL of the repo

3. Create a directory on your local machine where the contents of the repo will be downloaded. This can be the same directory to which the theme repo was cloned, but do not clone it *within* the theme repo. For example, your local file structure might look like:

```bash
.
└── Documents/
    └── gh-pages/
        ├── documentation-theme-jekyll/
        │   └── ...all theme subdirectories and files
        └── ioos-documentation-jekyll-skeleton/
            └── ...all template subdirectories and files
```
But *not*:

```bash
.
└── Documents/
    └── gh-pages/
        └── documentation-theme-jekyll/
            ├── ...all theme subdirectories and files
            └── ioos-documentation-jekyll-skeleton/
                └── ...all template subdirectories and files
```

   Notice that both repos are downloaded in a designated `gh-pages` local folder (can be called anything), but that the two repos *are not nested within each other*.

4. In a terminal window or Command Prompt, navigate to where the repo is to be downloaded, and type

   ```bash
   git clone <URL>
   ```

   where <URL> is the web URL from step 3.

5. Press enter. The repo will now be downloaded to your local machine.

Alternatively, after step 1, either use the “Open with GitHub Desktop” or the  “Download ZIP” options shown above to download the repo. Be sure to unzip it if you retrieve it this way.

6. Navigate into the new repository in terminal or Command Prompt

7. Remove the Git tracking files associated with the original IOOS repository (we do not care about the commit history prior to this point):
   
   ```bash
   rm -rf .git*
   ```

   This now ceases to be a local git repository. We will restore this shortly but with a fresh commit history.

### Step 2: Create a new remote repository

1. Back in the web browser on the GitHub page, create a new remote repository where this template will reside by clicking the “Repositories” tab at the top left. Then click the green “New” button at the top right of the page that opens.

2. Select an owner for the new repo from the dropdown list, if available. If you belong to a GitHub organization, such as SEFSC, you will have the option of assigning ownership of the repo to the organization or owning it yourself.

3. Rename the repo. If creating the repo in an organizational account, be sure to follow any repo naming conventions of that organization. To adhere to the current SEFSC GitHub Standard Operating Procedure, this new repo for SEFSC FATES has been named “[SEFSC-FATES-documentation-jekyll-skeleton](https://github.com/MattGrossi-NOAA/SEFSC-FATES-documentation-jekyll-skeleton){:target="_blank" rel="noopener"}” where “ioos” has been replaced by “SEFSC-FATES” and the remainder of the name has been retained. Note that this name could change in the future (*e.g.*, if the template is adapted more broadly across SEFSC, then “-FATES” will be removed.) See screenshot on next page.

4. Add a description. The recommendation is to specify what the repo is (in one or two sentences at most) and where it was forked from. For example:

   > *A GitHub Pages documentation template for SEFSC FATES based on the ioos-documentation-jekyll-skeleton repo.*

5. Click “Create repository”

6. Click the green “< > Code” button and copy the web URL of the repo. We’ll need this shortly.

### Step 3. Create a new local repository

1. Back in the directory created in [Step 1](#step-1-clone-the-ioos-skeleton-repository-locally).3, create a new directory that will contain the new custom template repository. For convenience, it is recommended that it be named the same as the remote repository created in [Step 2](#step-2-create-a-new-remote-repository).3, but this is not a necessity, since this is the local copy only. It can be named according to whatever naming convention you prefer. For example:

```bash
.
└── Documents/
    └── gh-pages/
        ├── documentation-theme-jekyll/
        │   └── ...all theme subdirectories & files
        └── ioos-documentation-jekyll-skeleton/
            └── ...original template subdirectories & files
        └── SEFSC-FATES-documentation-jekyll-skeleton/
            └── ...all new template subdirectories & files   
```

2. Navigate into that directory in the Terminal or Command Prompt

3. Create a `README.md` file. This can contain anything, but for now, let’s just put the name of the repository:

   ```bash
   echo "# SEFSC-FATES-documentation-jekyll-skeleton" >> README.md
   ```

4. Initiate a new Git repository and commit this file to the main branch

   ```bash
   git init
   git add README.md
   git commit -m "Initial commit"
   git branch -M main
   ```
5. Link this local repo to the remote repo made earlier using the URL copied in [Step 2](#step-2-create-a-new-remote-repository).6, which will have the following form:

   ```bash
   git remote add origin https://github.com/repo-owner/new-repo-name.git
   git push -u origin main
   ```

### Step 4. Create a new orphan branch for GitHub Pages

An orphan branch on GitHub is one whose commit history is independent of all other branches in the repo. The details are beyond the scope of this document, but the steps that follow will set one up. Orphan branches used for GitHub Pages are customarily called “gh-pages”.

1. Inside the GitHub repository, create a new orphan branch and remove the Git commit history, since by default, this will include the history of the main branch.

   ```bash
   git checkout --orphan gh-pages
   git rm -rf .
   rm .gitignore
   ```

2. Create a `README.md` file for this branch and commit to the new branch

   ```bash
   echo "# Name of Repo" > README.md
   git add README.md
   git commit -a -m "Initial commit"
   git push origin gh-pages
   ```

3. Copy the contents of the original IOOS repository into this new gh-pages branch

4. Commit the changes to GitHub as usual

The new repo now contains a duplicate, yet isolated, copy of the “ioos-documentation-jekyll- skeleton” repo. *Duplicated*, meaning that it contains all of the same files and subdirectories used to create the IOOS Documentation site; *isolated* in the sense that the new repo has its own version control history that is no longer linked to the original repository. You can now delete the “ioos-documentation-jekyll-skeleton” directory and its content from your local computer if you want, although it may be helpful to retain it as a backup until everything is configured properly.

### Step 5. Link the theme and skeleton repositories

This is where the theme created [above](#custom-sefsc-theme-for-github-pages-documentation-sites) gets added to the [documentation skeleton](#github-pages-documentation-template) being created now. This can be done using [GitHub submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules){:target="_blank" rel="noopener"}, which allow *theme files* to be contained in their own repository and then embedded into a separate repository that contains the *content files* for the web page. Recall that the “[documentation-theme-jekyll](https://github.com/MattGrossi-NOAA/documentation-theme-jekyll){:target="_blank" rel="noopener"}” repository has two branches, **main** and **navbars**. Each of these branches will be connected to the documentation repository as a separate submodule.

1. In a web browser, navigate to the documentation-theme-jekyll repository created above. Click the green “< > Code” button and copy the HTTPS web URL of the repository.

2. In a local terminal or Command Prompt, connect the **main** branch using the URL copied above

   ```bash
   git submodule add --name documentation-theme-jekyll https://github.com/ghuser/documentation-theme-jekyll theme   
   ```

   This did four things (along with some other magic behind the scenes):
      1. Created a submodule named “documentation-theme-jekyll” (where we have used the name of the repository for convenience)
      2. Created a directory, or path, named “theme” inside the current repository
      3. Mapped that path to the theme repo using the URL
      4. Created a new file `.gitmodules` in the repository that shows all of this. Check for yourself and verify that it worked. The file should look like this:

      ```
      [submodule "documentation-theme-jekyll"]
          path = theme
          url = https://github.com/ghuser/documentation-theme-jekyll
      ```

3. Connect the **topnav** branch using the URL copied above

   ```bash
   git submodule add --name _data/navbars_theme --branch navbars https://github.com/ghuser/documentation-theme-jekyll _data/navbars
   ```

   This does the same things as before, except we have specified the “navbars” branch be used instead. The `.gitmodules` file should now look like this:

    ```
    [submodule "documentation-theme-jekyll"]
        path = theme
        url = https://github.com/ghuser/documentation-theme-jekyll
    [submodule "_data/navbars_theme"]
        path = _data/navbars
        url = https://github.com/ghuser/documentation-theme-jekyll
        branch = navbars
    ```

4. In the web browser, on the “SEFSC-FATES-documentation-jekyll-skeleton” repo landing page, click the “Settings” tab. Then, from the sidebar, “Actions” → “General”

 5. Under “Workflow permissions” select “Read and write permissions” to allow GitHub Actions to update the submodules (which is a write action). Click “Save” when done.

The “SEFSC-FATES-documentation-jekyll-skeleton” repo now contains a new directory called `theme @ xxxxxxx`, where *xxxxxxx* is the most most recent commit identifier on the “main” branch of “documentation-theme-jekyll”. Inside this new directory are all of the theme files customized above. Also, in the `_data` directory, there is a new `navbars @ yyyyyyy`, where *yyyyyyy* is the most recent commit identifier on the “navbars” branch of “documentation-theme-jekyll”. In this file is the `topnav` yml file created earlier. More on this later.

### Step 6. Set up local machine for local editing (optional)

Editing the site locally is often easier than making the changes on GitHub, especially for formatted script and configuration files for which GitHub has only limited built-in dynamic formatting capabilities. To do this, however, Jekyll and Ruby need to be installed. If these are already installed, or if you do not intend to edit locally, skip to [Step 7](#step-7-configure-the-new-documentation-template-repository). From the [Jekyll Documentation Theme Getting Started documentation](https://idratherbewriting.com/documentation-theme-jekyll){:target="_blank" rel="noopener"}:

1. [Install Ruby](https://idratherbewriting.com/documentation-theme-jekyll/mydoc_install_jekyll_on_windows.html){:target="_blank" rel="noopener"}:

   a. [Download](https://rubyinstaller.org/downloads/){:target="_blank" rel="noopener"} the latest RubyInstaller with Devkit

   b. Double-click the downloaded file to install

   c. Run “ridk install” on the last step of the installation wizard

2. Open new command prompt window or Git Bash session

3. Install Jekyll gem
   
   ```bash
   gem install jekyll
   ```

4. Install Jekyll theme dependencies:

   a. Navigate to the directory containing the Jekyll documentation theme repo
   
   b. Update bundle

   ```bash
   bundle update
   ```
   
   (This terminated with an error on the first try, simply rerunning it worked.)

   c. If Ruby version is 3.0 or higher, [“webrick” will need to be manually installed](https://github.com/jekyll/jekyll/issues/8523){:target="_blank" rel="noopener"} in order for this particular theme to work:

   ```bash
   bundle add webrick
   ```

5. The site can now be run locally in Jekyll, as discussed in [Getting started with IOOS Jekyll Documentation Theme Skeleton](https://ioos.github.io/ioos-documentation-jekyll-skeleton/howto.html){:target="_blank" rel="noopener"}:

   ```bash
   bundle exec jekyll serve --config _config.yml,_config_dev.yml --watch --verbose --incremental
   ```

   The local site will be available at http://localhost:4000/SEFSC-FATES-documentation-jekyll-skeleton/ once configuration below is completed.

### Step 7. Configure the new documentation template repository

We are now ready to customize the new documentation repository and make it into a template repo. If done locally, any changes can be viewed at any time at the local site above by refreshing the page (be sure to first save the changes in whatever file you’re working in.) The following steps can theoretically be completed in any order.

1. In `_data/sidebars`, rename `sidebar_ioos.yml` using the same naming convention used in [Step 3](#step-3-customize-the-navbar).2 above for `topnav_ioos.yml`. Inside this document, change the title “HOWTO - …” at approximately Line 54.

2. Change the “baseurl” the `_config_dev.yml` file, which contains settings for local development, to match the name of the new repository. This will make the localhost URL above work. Commit when finished.

3. Update the `_config.yml` file to replace any references to IOOS with SEFSC-FATES, including in commented lines, being sure to change the following elements:

   a. “site_title”

   b. “company_name”

   c. “feedback_email”

   d. Values for “sidebar” and “topnav” in all four places.

    1. Set the value for “topnav” to be the new name of the `topnav` yml file set in [Step 3](#step-3-customize-the-navbar).2 above (e.g., topnav_ioos → topnav_sefsc).
    2. Set the value for “sidebar” to be the new name of the `sidebar` yml file from [Step 7](#step-7-configure-the-new-documentation-template-repository).1 (e.g., sidebar_ioos → sidebar_sefsc).

   e. “description”

   f. “url”

   g. “baseurl”

   h. “repository”

   i. “github_editme_path”

   j. Any comments throughout the file

   Note: Do not change placeholder text such as “Insert Your Documentation Site Name”, as this will be replaced with actual content for individual documentation pages.  Commit when finished.

4. Update the `README.md` file. Commit when finished.

   a. Remove any references to IOOS, replacing with SEFSC-FATES

   b. Update all URLs including all basenames (e.g., https://ioos.github.io → https://sefsc.github.io) and repository names (e.g., ioos-documentation-jekyll-skeleton → SEFSC-FATES-documentation-jekyll-skeleton)

5. Update the `_docs/howto.md` file. Commit when finished.

   a. Remove any references to IOOS, replacing with SEFSC-FATES

   b. Update all URLs including all basenames (e.g., https://ioos.github.io → https://sefsc.github.io) and repository names (e.g., ioos-documentation-jekyll-skeleton → SEFSC-FATES-documentation-jekyll-skeleton)

6. Update the `_docs/index.md` file. Commit when finished.

   a. Remove any references to IOOS, replacing with SEFSC-FATES

   b. Update all URLs including all basenames (e.g., https://ioos.github.io → https://sefsc.github.io) and repository names (e.g., ioos-documentation-jekyll-skeleton → SEFSC-FATES-documentation-jekyll-skeleton)

   c. Add mandatory and/or optional headers and subheaders to be used when creating software or model documentation

7. Push all changes to gh-pages branch. It will take a few minutes for GitHub to build the site, but if everything was done correctly, the new template site should look like the original IOOS template but customized for SEFSC FATES.

8. Finally, navigate to the SEFSC-FATES-documentation-jekyll-skeleton repo in a web browser. Click “Settings” at the top and select “Template repository” to allow this new repo to be used as a starting point for future projects.

# Conclusion

This page walked through the creation of two new GitHub repositories: a documentation skeleton template repository, which can be duplicated and populated with headers and text to create document a model, source code, or any other project; and a second theme repository that contains the behind-the-scenes configurations, branding, etc. to control the look and functionality of the site. These two repositories were linked together using GitHub submodules allowing the theme repo to be managed separately from all documentation repos while ensuring that all documentation repos share the same look and feel. This is particularly important for adhering to organizational branding requirements.

Separating the website theme files from the content repository also minimizes the learning curve to creating a new site because there is no need to re-create or configure any back-end settings. This means there is no need to know or learn HTML, CSS, JavaScript, or any other languages used to generate the site itself. And by templating the Markdown files containing the actual content of the documentation site, next to no knowledge of Markdown is needed either: the user can essentially replace the placeholder text with the appropriate narrative. Instructions on how to proceed in creating a new repo using the template are contained in a HowTo page with the template itself. This template can also be easily added to an existing repo containing, for example, source code, allowing the documentation to live alongside the code itself. Importantly, because all of this is done in GitHub, every component is completely version controlled.

We hope this page provides guidance for others within NOAA interested in creating their own template. These can either be forked from IOOS directly, as the steps describe, or from the SEFSC repos created herein. The latter may be particularly beneficial for other FMCs within NOAA Fisheries, as this SEFSC template may be closer to what such a user would want.

