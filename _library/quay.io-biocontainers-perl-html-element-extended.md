---
layout: container
name:  "quay.io/biocontainers/perl-html-element-extended"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-html-element-extended/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-html-element-extended/container.yaml"
updated_at: "2022-10-27 00:20:25.521374"
latest: "1.18--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-html-element-extended"
aliases:
 - "corelist"
 - "cpan"
 - "enc2xs"
 - "encguess"
 - "h2ph"
 - "h2xs"
 - "htmltree"
 - "instmodsh"
 - "json_pp"
 - "libnetcfg"
 - "perl"
 - "perl5.32.1"
 - "perlbug"
 - "perldoc"
 - "perlivp"
 - "perlthanks"
 - "piconv"
 - "pl2pm"
 - "pod2html"
 - "pod2man"
 - "pod2text"
 - "pod2usage"
 - "podchecker"
 - "prove"
 - "ptar"
versions:
 - "1.18--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-html-element-extended"
config: {"url": "https://biocontainers.pro/tools/perl-html-element-extended", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-html-element-extended", "latest": {"1.18--pl5321hdfd78af_2": "sha256:32bfec5175c4739648cee9eff9362ff169c22f32814448c2c4901ccb8d5bb6ec"}, "tags": {"1.18--pl5321hdfd78af_2": "sha256:32bfec5175c4739648cee9eff9362ff169c22f32814448c2c4901ccb8d5bb6ec"}, "docker": "quay.io/biocontainers/perl-html-element-extended", "aliases": {"corelist": "/usr/local/bin/corelist", "cpan": "/usr/local/bin/cpan", "enc2xs": "/usr/local/bin/enc2xs", "encguess": "/usr/local/bin/encguess", "h2ph": "/usr/local/bin/h2ph", "h2xs": "/usr/local/bin/h2xs", "htmltree": "/usr/local/bin/htmltree", "instmodsh": "/usr/local/bin/instmodsh", "json_pp": "/usr/local/bin/json_pp", "libnetcfg": "/usr/local/bin/libnetcfg", "perl": "/usr/local/bin/perl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "perlbug": "/usr/local/bin/perlbug", "perldoc": "/usr/local/bin/perldoc", "perlivp": "/usr/local/bin/perlivp", "perlthanks": "/usr/local/bin/perlthanks", "piconv": "/usr/local/bin/piconv", "pl2pm": "/usr/local/bin/pl2pm", "pod2html": "/usr/local/bin/pod2html", "pod2man": "/usr/local/bin/pod2man", "pod2text": "/usr/local/bin/pod2text", "pod2usage": "/usr/local/bin/pod2usage", "podchecker": "/usr/local/bin/podchecker", "prove": "/usr/local/bin/prove", "ptar": "/usr/local/bin/ptar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-html-element-extended.
shpc-registry automated BioContainers addition for perl-html-element-extended
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-html-element-extended
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-html-element-extended:1.18--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-html-element-extended/1.18--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-html-element-extended/1.18--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-html-element-extended-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-html-element-extended-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-html-element-extended-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-html-element-extended-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-html-element-extended-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-html-element-extended-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### corelist

```bash
$ singularity exec <container> /usr/local/bin/corelist
$ podman run --it --rm --entrypoint /usr/local/bin/corelist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corelist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpan

```bash
$ singularity exec <container> /usr/local/bin/cpan
$ podman run --it --rm --entrypoint /usr/local/bin/cpan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enc2xs

```bash
$ singularity exec <container> /usr/local/bin/enc2xs
$ podman run --it --rm --entrypoint /usr/local/bin/enc2xs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enc2xs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### encguess

```bash
$ singularity exec <container> /usr/local/bin/encguess
$ podman run --it --rm --entrypoint /usr/local/bin/encguess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/encguess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2ph

```bash
$ singularity exec <container> /usr/local/bin/h2ph
$ podman run --it --rm --entrypoint /usr/local/bin/h2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2xs

```bash
$ singularity exec <container> /usr/local/bin/h2xs
$ podman run --it --rm --entrypoint /usr/local/bin/h2xs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2xs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htmltree

```bash
$ singularity exec <container> /usr/local/bin/htmltree
$ podman run --it --rm --entrypoint /usr/local/bin/htmltree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htmltree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### instmodsh

```bash
$ singularity exec <container> /usr/local/bin/instmodsh
$ podman run --it --rm --entrypoint /usr/local/bin/instmodsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/instmodsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### json_pp

```bash
$ singularity exec <container> /usr/local/bin/json_pp
$ podman run --it --rm --entrypoint /usr/local/bin/json_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/json_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libnetcfg

```bash
$ singularity exec <container> /usr/local/bin/libnetcfg
$ podman run --it --rm --entrypoint /usr/local/bin/libnetcfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libnetcfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl

```bash
$ singularity exec <container> /usr/local/bin/perl
$ podman run --it --rm --entrypoint /usr/local/bin/perl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perlbug

```bash
$ singularity exec <container> /usr/local/bin/perlbug
$ podman run --it --rm --entrypoint /usr/local/bin/perlbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perlbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perldoc

```bash
$ singularity exec <container> /usr/local/bin/perldoc
$ podman run --it --rm --entrypoint /usr/local/bin/perldoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perldoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perlivp

```bash
$ singularity exec <container> /usr/local/bin/perlivp
$ podman run --it --rm --entrypoint /usr/local/bin/perlivp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perlivp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perlthanks

```bash
$ singularity exec <container> /usr/local/bin/perlthanks
$ podman run --it --rm --entrypoint /usr/local/bin/perlthanks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perlthanks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### piconv

```bash
$ singularity exec <container> /usr/local/bin/piconv
$ podman run --it --rm --entrypoint /usr/local/bin/piconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/piconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pl2pm

```bash
$ singularity exec <container> /usr/local/bin/pl2pm
$ podman run --it --rm --entrypoint /usr/local/bin/pl2pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pl2pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pod2html

```bash
$ singularity exec <container> /usr/local/bin/pod2html
$ podman run --it --rm --entrypoint /usr/local/bin/pod2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pod2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pod2man

```bash
$ singularity exec <container> /usr/local/bin/pod2man
$ podman run --it --rm --entrypoint /usr/local/bin/pod2man   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pod2man   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pod2text

```bash
$ singularity exec <container> /usr/local/bin/pod2text
$ podman run --it --rm --entrypoint /usr/local/bin/pod2text   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pod2text   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pod2usage

```bash
$ singularity exec <container> /usr/local/bin/pod2usage
$ podman run --it --rm --entrypoint /usr/local/bin/pod2usage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pod2usage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podchecker

```bash
$ singularity exec <container> /usr/local/bin/podchecker
$ podman run --it --rm --entrypoint /usr/local/bin/podchecker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podchecker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prove

```bash
$ singularity exec <container> /usr/local/bin/prove
$ podman run --it --rm --entrypoint /usr/local/bin/prove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptar

```bash
$ singularity exec <container> /usr/local/bin/ptar
$ podman run --it --rm --entrypoint /usr/local/bin/ptar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptar   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)