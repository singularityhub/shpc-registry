---
layout: container
name:  "quay.io/biocontainers/bioconductor-snphood"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-snphood/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-snphood/container.yaml"
updated_at: "2024-08-18 02:50:52.093064"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-snphood"
aliases:
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
 - "wget"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-snphood"
config: {"url": "https://biocontainers.pro/tools/bioconductor-snphood", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-snphood", "latest": {"1.32.0--r43hdfd78af_0": "sha256:fb2590c7cf6cd14e009756847130c6836327b89b81276af828fa7caf4b8ce964"}, "tags": {"1.8.0--r3.4.1_0": "sha256:1e3fff017b03e86a4ce8cc284e3f6e00e3af3ffe70bd304d2e5d7ae4218ae402", "1.28.0--r42hdfd78af_0": "sha256:2586b9e8fde8ac16a2de3e76fca98599b8c7cd40a25e796fa0e5900d125a691e", "1.24.0--r41hdfd78af_0": "sha256:447bc2771528506c19c0774bd5e9456d737746a2dc86aadcda8fb3179c167103", "1.22.0--r41hdfd78af_0": "sha256:4f5b88f8fe6f2fbb20bf3178b9abc5d4df2831a369b97fc4250e8aac6a4041ea", "1.20.0--r40hdfd78af_1": "sha256:fd7c9f60b77499af3375a132e8d6bbe7a13c49ba5df96b41d52f5fe69ab370a6", "1.18.0--r40_0": "sha256:278ed5a3467f8993b848a8401671454a4af8558c3245f769c370901884b5ce94", "1.30.0--r43hdfd78af_0": "sha256:a794e29547dacc86d7c35362a94792e330173db2a2c698f8c6267e1c40b7ebf8", "1.32.0--r43hdfd78af_0": "sha256:fb2590c7cf6cd14e009756847130c6836327b89b81276af828fa7caf4b8ce964"}, "docker": "quay.io/biocontainers/bioconductor-snphood", "aliases": {"my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror", "wget": "/usr/local/bin/wget", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-snphood.
shpc-registry automated BioContainers addition for bioconductor-snphood
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-snphood
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-snphood:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-snphood/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-snphood/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-snphood-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snphood-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snphood-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-snphood-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-snphood-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-snphood-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config

```bash
$ singularity exec <container> /usr/local/bin/mysql_config
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perror

```bash
$ singularity exec <container> /usr/local/bin/perror
$ podman run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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