---
layout: container
name:  "quay.io/biocontainers/perl-graphviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-graphviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-graphviz/container.yaml"
updated_at: "2025-10-09 04:38:44.436858"
latest: "2.26--pl5321h46c88eb_0"
container_url: "https://biocontainers.pro/tools/perl-graphviz"
aliases:
 - "xpath"
 - "xml_grep"
 - "xml_merge"
 - "xml_pp"
 - "xml_spellcheck"
 - "xml_split"
 - "webtidy"
 - "tidyp"
 - "diffimg"
 - "delaunay"
versions:
 - "2.24--pl5321h4b32bfc_1"
 - "2.26--pl5321h46c88eb_0"
 - "2.25--pl5321h46c88eb_0"
description: "shpc-registry automated BioContainers addition for perl-graphviz"
config: {"url": "https://biocontainers.pro/tools/perl-graphviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-graphviz", "latest": {"2.26--pl5321h46c88eb_0": "sha256:f9383b1ff4569c3084a9105459faf17cdb7c14d3678e1dfcc30e2e0805dfe22d"}, "tags": {"2.24--pl5321h4b32bfc_1": "sha256:62fa3078740dbabce88120f32bd6e0e21da5adf50b25d4c660eec8cd482ef8fe", "2.26--pl5321h46c88eb_0": "sha256:f9383b1ff4569c3084a9105459faf17cdb7c14d3678e1dfcc30e2e0805dfe22d", "2.25--pl5321h46c88eb_0": "sha256:c6d0123941dae64641809dec5efec5bf0b1f59095a7d43feeec3e6d3b9705a04"}, "docker": "quay.io/biocontainers/perl-graphviz", "aliases": {"xpath": "/usr/local/bin/xpath", "xml_grep": "/usr/local/bin/xml_grep", "xml_merge": "/usr/local/bin/xml_merge", "xml_pp": "/usr/local/bin/xml_pp", "xml_spellcheck": "/usr/local/bin/xml_spellcheck", "xml_split": "/usr/local/bin/xml_split", "webtidy": "/usr/local/bin/webtidy", "tidyp": "/usr/local/bin/tidyp", "diffimg": "/usr/local/bin/diffimg", "delaunay": "/usr/local/bin/delaunay"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-graphviz.
shpc-registry automated BioContainers addition for perl-graphviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-graphviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-graphviz:2.26--pl5321h46c88eb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-graphviz/2.26--pl5321h46c88eb_0
$ module help quay.io/biocontainers/perl-graphviz/2.26--pl5321h46c88eb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-graphviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-graphviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-graphviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-graphviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-graphviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-graphviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xpath

```bash
$ singularity exec <container> /usr/local/bin/xpath
$ podman run --it --rm --entrypoint /usr/local/bin/xpath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xpath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_grep

```bash
$ singularity exec <container> /usr/local/bin/xml_grep
$ podman run --it --rm --entrypoint /usr/local/bin/xml_grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_merge

```bash
$ singularity exec <container> /usr/local/bin/xml_merge
$ podman run --it --rm --entrypoint /usr/local/bin/xml_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_pp

```bash
$ singularity exec <container> /usr/local/bin/xml_pp
$ podman run --it --rm --entrypoint /usr/local/bin/xml_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_spellcheck

```bash
$ singularity exec <container> /usr/local/bin/xml_spellcheck
$ podman run --it --rm --entrypoint /usr/local/bin/xml_spellcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_spellcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_split

```bash
$ singularity exec <container> /usr/local/bin/xml_split
$ podman run --it --rm --entrypoint /usr/local/bin/xml_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### webtidy

```bash
$ singularity exec <container> /usr/local/bin/webtidy
$ podman run --it --rm --entrypoint /usr/local/bin/webtidy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/webtidy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tidyp

```bash
$ singularity exec <container> /usr/local/bin/tidyp
$ podman run --it --rm --entrypoint /usr/local/bin/tidyp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tidyp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diffimg

```bash
$ singularity exec <container> /usr/local/bin/diffimg
$ podman run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delaunay

```bash
$ singularity exec <container> /usr/local/bin/delaunay
$ podman run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
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