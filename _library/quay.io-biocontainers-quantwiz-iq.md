---
layout: container
name:  "quay.io/biocontainers/quantwiz-iq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/quantwiz-iq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/quantwiz-iq/container.yaml"
updated_at: "2024-03-21 04:18:52.875563"
latest: "2.0--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/quantwiz-iq"
aliases:
 - "QuantWiz_IQ"
 - "QuantWiz_IQ.pl"
 - "xml_grep"
 - "xml_merge"
 - "xml_pp"
 - "xml_spellcheck"
 - "xml_split"
 - "webtidy"
 - "tidyp"
 - "htmltree"
 - "perl5.26.2"
 - "podselect"
versions:
 - "2.0--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for quantwiz-iq"
config: {"url": "https://biocontainers.pro/tools/quantwiz-iq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for quantwiz-iq", "latest": {"2.0--hdfd78af_2": "sha256:d5b12485860188b99f3e9453ed933dcad30fe733759d1766401a1769af7eac94"}, "tags": {"2.0--hdfd78af_2": "sha256:d5b12485860188b99f3e9453ed933dcad30fe733759d1766401a1769af7eac94"}, "docker": "quay.io/biocontainers/quantwiz-iq", "aliases": {"QuantWiz_IQ": "/usr/local/bin/QuantWiz_IQ", "QuantWiz_IQ.pl": "/usr/local/bin/QuantWiz_IQ.pl", "xml_grep": "/usr/local/bin/xml_grep", "xml_merge": "/usr/local/bin/xml_merge", "xml_pp": "/usr/local/bin/xml_pp", "xml_spellcheck": "/usr/local/bin/xml_spellcheck", "xml_split": "/usr/local/bin/xml_split", "webtidy": "/usr/local/bin/webtidy", "tidyp": "/usr/local/bin/tidyp", "htmltree": "/usr/local/bin/htmltree", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/quantwiz-iq.
shpc-registry automated BioContainers addition for quantwiz-iq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/quantwiz-iq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/quantwiz-iq:2.0--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/quantwiz-iq/2.0--hdfd78af_2
$ module help quay.io/biocontainers/quantwiz-iq/2.0--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quantwiz-iq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quantwiz-iq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quantwiz-iq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quantwiz-iq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quantwiz-iq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quantwiz-iq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### QuantWiz_IQ

```bash
$ singularity exec <container> /usr/local/bin/QuantWiz_IQ
$ podman run --it --rm --entrypoint /usr/local/bin/QuantWiz_IQ   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/QuantWiz_IQ   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### QuantWiz_IQ.pl

```bash
$ singularity exec <container> /usr/local/bin/QuantWiz_IQ.pl
$ podman run --it --rm --entrypoint /usr/local/bin/QuantWiz_IQ.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/QuantWiz_IQ.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### htmltree

```bash
$ singularity exec <container> /usr/local/bin/htmltree
$ podman run --it --rm --entrypoint /usr/local/bin/htmltree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htmltree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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