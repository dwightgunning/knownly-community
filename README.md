# knownly-community

The Knownly Community website.

This respository contains the source code behind the Knownly Community at https://www.knownly.net/community

The source is made available to everybody for several reasons:
- The ambition is to make the Knownly Community as open and inclusive as possible.
- The hope is that the site will be built through collaboration between our community of artists, creatives, copywriters, designers, developers, growth hackers and marketeers.
- The community site offers great demonstrations of what's possible with a Knownly website.
- The community site is a great testing ground for sharing advanced Knownly features with they community while they're being worked on and after they're all polished up.

## Getting involved

There are any number of ways to get involved. If you have an idea for a [guide], Most important, just make your ideas known.

### Reach out anyway you like

You'll catch us via [Email](community@knownly.net), Twitter [Knownly_net](https://twitter.com/Knownly_net), or [Facebook](https://www.facebook.com/knownly.net/). Let us know what you have created or have in mind and we'll figure it out from there.

### Submit a Pull Request

Pull requests to this repository are the simplest way for us to handle your contributions.

For now there are no strict guidelines. Watch this space.

See below for more details on how the site is built and how you can get setup to run it on your own machine.

## How the site is built

The Knownly Community website is pure HTML, CSS, Javascript. It's built using software called Cactus which is easy no matter what your level of programming experience.

## Getting setup

If you're not yet comfortable with the command-line, git and a splash of Python then we suggest the __basic__ steps. If you're fine with those then feel free to go with the __advanced__ steps.

### Basic

Cactus is nice because if you're a not too comfortable with the command-line, there's a free [OS X app](http://www.cactusformac.com) (sorry Windows peeps - drop me an [email](community@knownly.net) and I'll help you get setup).

If you're fine with the command line, or want to give it a crack, grab the [Cactus source](https://github.com/koenbok/Cactus).

Once you've got Cactus installed, you can download a copy of the site or use git to clone the repo.

### Advanced

1. Install the cactus python package (we recommend using a virtualenv):

```
pip install cactus
```

2. Fork the community-site repo

   <iframe src="https://ghbtns.com/github-btn.html?user=knownly&repo=knownly-community&type=fork" frameborder="0" scrolling="0" width="170px" height="20px"></iframe>

3. Clone your fork

```
git clone https://github.com/<< YOUR USERNAME >>/knownly-community.git
```

4. Change directory into the knownly-community website root

5. Run the Cactus development server

```
cactus serve
```

6. Note the shell output and grab the URL from which Cactus is serving the website. Point web browser at it.

7. Bingo!

## License

This content of this work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. The underlying source code used to format and display that content is licensed under the MIT License. These are set out in the [license statement](../master/LICENSE.md).
