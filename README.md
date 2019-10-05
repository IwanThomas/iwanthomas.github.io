### How to Publish to this Blog

1. cd into the blog directory and activate the virtual environment with the command `source <name_of_venv>/bin/activate`
2. In your source branch, place the jupyter notebook in the `content` file.
3. Create an `nbdata` file with the same title as your jupyter notebook. That is `<blog_post_title>.nbdata`. Populate it with the following (note the trailing line is important)

```
Title: Something like this
Slug: 
Date: '2019-01-01'
Category: Experimentation
Tags: Experimentation, Statistics
Author: Iwan Thomas
Summary: 

```

4. From your site directory, run the following command to generate your site: `pelican content`
5. Running the command `make devserver` will enable you to preview the site in your browser at `http://localhost:8000`
6. To get your site out in the world, follow the advice in the [docs](http://docs.getpelican.com/en/3.6.3/tips.html#user-pages). 
```
$ pelican content -o output -s pelicanconf.py
$ ghp-import output
$ git push https://github.com/IwanThomas/iwanthomas.github.io.git gh-pages:master

```
7. You should then be able to access your site at `https://iwanthomas.github.io./`

### Resources
- [Blog Post with a list of useful resources](http://alanzzhao.com/about_the_blog_jupyter_test.html)
- [In-depth Tutorial](http://chdoig.github.io/create-pelican-blog.html)
- [Pelican Docs](http://docs.getpelican.com/en/3.6.3/quickstart.html)