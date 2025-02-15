---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocbook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocbook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocbook/container.yaml"
updated_at: "2025-02-15 03:21:35.754362"
latest: "1.4.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocbook"
aliases:
 - "deno"
 - "esbuild"
 - "quarto"
 - "quarto.js"
 - "sass"
 - "git2"
 - "pcre2posix_test"
 - "hb-info"
 - "tjbench"
 - "pandoc"
versions:
 - "1.0.0--r43hdfd78af_0"
 - "1.4.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-biocbook"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocbook", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-biocbook", "latest": {"1.4.0--r44hdfd78af_0": "sha256:afc5be3fcfdb19c41a116ca6dd7caea4a7ea402f0f186e7d078232eb106ab43e"}, "tags": {"1.0.0--r43hdfd78af_0": "sha256:6ce697da9b58d4fe8398651285f01ca77f7a82abe37ad0b753c05c9a3df3508f", "1.4.0--r44hdfd78af_0": "sha256:afc5be3fcfdb19c41a116ca6dd7caea4a7ea402f0f186e7d078232eb106ab43e"}, "docker": "quay.io/biocontainers/bioconductor-biocbook", "aliases": {"deno": "/usr/local/bin/deno", "esbuild": "/usr/local/bin/esbuild", "quarto": "/usr/local/bin/quarto", "quarto.js": "/usr/local/bin/quarto.js", "sass": "/usr/local/bin/sass", "git2": "/usr/local/bin/git2", "pcre2posix_test": "/usr/local/bin/pcre2posix_test", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocbook.
singularity registry hpc automated addition for bioconductor-biocbook
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocbook
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocbook:1.4.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocbook/1.4.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocbook/1.4.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocbook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocbook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocbook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocbook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocbook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocbook-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deno

```bash
$ singularity exec <container> /usr/local/bin/deno
$ podman run --it --rm --entrypoint /usr/local/bin/deno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esbuild

```bash
$ singularity exec <container> /usr/local/bin/esbuild
$ podman run --it --rm --entrypoint /usr/local/bin/esbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quarto

```bash
$ singularity exec <container> /usr/local/bin/quarto
$ podman run --it --rm --entrypoint /usr/local/bin/quarto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quarto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quarto.js

```bash
$ singularity exec <container> /usr/local/bin/quarto.js
$ podman run --it --rm --entrypoint /usr/local/bin/quarto.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quarto.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sass

```bash
$ singularity exec <container> /usr/local/bin/sass
$ podman run --it --rm --entrypoint /usr/local/bin/sass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git2

```bash
$ singularity exec <container> /usr/local/bin/git2
$ podman run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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