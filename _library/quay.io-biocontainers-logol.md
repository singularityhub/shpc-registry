---
layout: container
name:  "quay.io/biocontainers/logol"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/logol/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/logol/container.yaml"
updated_at: "2024-05-28 03:02:32.691747"
latest: "1.7.8--2"
container_url: "https://biocontainers.pro/tools/logol"
aliases:
 - "LogolExec.sh"
 - "LogolMultiExec.sh"
 - "cassiopee"
 - "cassiopeeknife"
 - "latex2html"
 - "swipl"
 - "swipl-ld"
 - "swipl-rc"
 - "erb"
 - "gem"
 - "irb"
 - "rake"
 - "rdoc"
 - "ri"
 - "ruby"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
versions:
 - "1.7.8--2"
description: "shpc-registry automated BioContainers addition for logol"
config: {"url": "https://biocontainers.pro/tools/logol", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for logol", "latest": {"1.7.8--2": "sha256:e9bbe6c9bb2fb5bdb5d33afc48cd917b40776b8acfc99af496a3f4ab07d851d5"}, "tags": {"1.7.8--2": "sha256:e9bbe6c9bb2fb5bdb5d33afc48cd917b40776b8acfc99af496a3f4ab07d851d5"}, "docker": "quay.io/biocontainers/logol", "aliases": {"LogolExec.sh": "/usr/local/bin/LogolExec.sh", "LogolMultiExec.sh": "/usr/local/bin/LogolMultiExec.sh", "cassiopee": "/usr/local/bin/cassiopee", "cassiopeeknife": "/usr/local/bin/cassiopeeknife", "latex2html": "/usr/local/bin/latex2html", "swipl": "/usr/local/bin/swipl", "swipl-ld": "/usr/local/bin/swipl-ld", "swipl-rc": "/usr/local/bin/swipl-rc", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "rake": "/usr/local/bin/rake", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri", "ruby": "/usr/local/bin/ruby", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/logol.
shpc-registry automated BioContainers addition for logol
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/logol
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/logol:1.7.8--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/logol/1.7.8--2
$ module help quay.io/biocontainers/logol/1.7.8--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### logol-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### logol-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### logol-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### logol-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### logol-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### logol-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LogolExec.sh

```bash
$ singularity exec <container> /usr/local/bin/LogolExec.sh
$ podman run --it --rm --entrypoint /usr/local/bin/LogolExec.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LogolExec.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LogolMultiExec.sh

```bash
$ singularity exec <container> /usr/local/bin/LogolMultiExec.sh
$ podman run --it --rm --entrypoint /usr/local/bin/LogolMultiExec.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LogolMultiExec.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cassiopee

```bash
$ singularity exec <container> /usr/local/bin/cassiopee
$ podman run --it --rm --entrypoint /usr/local/bin/cassiopee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cassiopee   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cassiopeeknife

```bash
$ singularity exec <container> /usr/local/bin/cassiopeeknife
$ podman run --it --rm --entrypoint /usr/local/bin/cassiopeeknife   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cassiopeeknife   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### latex2html

```bash
$ singularity exec <container> /usr/local/bin/latex2html
$ podman run --it --rm --entrypoint /usr/local/bin/latex2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/latex2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swipl

```bash
$ singularity exec <container> /usr/local/bin/swipl
$ podman run --it --rm --entrypoint /usr/local/bin/swipl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swipl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swipl-ld

```bash
$ singularity exec <container> /usr/local/bin/swipl-ld
$ podman run --it --rm --entrypoint /usr/local/bin/swipl-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swipl-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swipl-rc

```bash
$ singularity exec <container> /usr/local/bin/swipl-rc
$ podman run --it --rm --entrypoint /usr/local/bin/swipl-rc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swipl-rc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb

```bash
$ singularity exec <container> /usr/local/bin/erb
$ podman run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem

```bash
$ singularity exec <container> /usr/local/bin/gem
$ podman run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irb

```bash
$ singularity exec <container> /usr/local/bin/irb
$ podman run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rake

```bash
$ singularity exec <container> /usr/local/bin/rake
$ podman run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdoc

```bash
$ singularity exec <container> /usr/local/bin/rdoc
$ podman run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ri

```bash
$ singularity exec <container> /usr/local/bin/ri
$ podman run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruby

```bash
$ singularity exec <container> /usr/local/bin/ruby
$ podman run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
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