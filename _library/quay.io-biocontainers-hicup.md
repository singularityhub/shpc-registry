---
layout: container
name:  "quay.io/biocontainers/hicup"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hicup/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hicup/container.yaml"
updated_at: "2025-11-25 03:31:24.978076"
latest: "0.9.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/hicup"
aliases:
 - "find_common_fragment_interactions.pl"
 - "hicup"
 - "hicup2fithic"
 - "hicup2gothic"
 - "hicup2hicpipe"
 - "hicup2homer"
 - "hicup2juicer"
 - "hicup_capture"
 - "hicup_checker"
 - "hicup_deduplicator"
 - "hicup_digester"
 - "hicup_filter"
 - "hicup_mapper"
 - "hicup_module.pm"
 - "hicup_reporter"
 - "hicup_truncater"
 - "make_hic_array.pl"
 - "pandoc-server"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
versions:
 - "0.8.3--hdfd78af_1"
 - "0.9.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for hicup"
config: {"url": "https://biocontainers.pro/tools/hicup", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hicup", "latest": {"0.9.2--hdfd78af_1": "sha256:1b32f21ff1e4da217a1ed48495afad26d465301d6714f2fc3bb84648a4fb02bf"}, "tags": {"0.8.3--hdfd78af_1": "sha256:6c69771af7a01e414b71e69776e28ad7e801ecff962974a11106fd708b18012e", "0.9.2--hdfd78af_1": "sha256:1b32f21ff1e4da217a1ed48495afad26d465301d6714f2fc3bb84648a4fb02bf"}, "docker": "quay.io/biocontainers/hicup", "aliases": {"find_common_fragment_interactions.pl": "/usr/local/bin/find_common_fragment_interactions.pl", "hicup": "/usr/local/bin/hicup", "hicup2fithic": "/usr/local/bin/hicup2fithic", "hicup2gothic": "/usr/local/bin/hicup2gothic", "hicup2hicpipe": "/usr/local/bin/hicup2hicpipe", "hicup2homer": "/usr/local/bin/hicup2homer", "hicup2juicer": "/usr/local/bin/hicup2juicer", "hicup_capture": "/usr/local/bin/hicup_capture", "hicup_checker": "/usr/local/bin/hicup_checker", "hicup_deduplicator": "/usr/local/bin/hicup_deduplicator", "hicup_digester": "/usr/local/bin/hicup_digester", "hicup_filter": "/usr/local/bin/hicup_filter", "hicup_mapper": "/usr/local/bin/hicup_mapper", "hicup_module.pm": "/usr/local/bin/hicup_module.pm", "hicup_reporter": "/usr/local/bin/hicup_reporter", "hicup_truncater": "/usr/local/bin/hicup_truncater", "make_hic_array.pl": "/usr/local/bin/make_hic_array.pl", "pandoc-server": "/usr/local/bin/pandoc-server", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hicup.
shpc-registry automated BioContainers addition for hicup
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hicup
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hicup:0.9.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hicup/0.9.2--hdfd78af_1
$ module help quay.io/biocontainers/hicup/0.9.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hicup-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hicup-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hicup-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hicup-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hicup-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hicup-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### find_common_fragment_interactions.pl

```bash
$ singularity exec <container> /usr/local/bin/find_common_fragment_interactions.pl
$ podman run --it --rm --entrypoint /usr/local/bin/find_common_fragment_interactions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_common_fragment_interactions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup

```bash
$ singularity exec <container> /usr/local/bin/hicup
$ podman run --it --rm --entrypoint /usr/local/bin/hicup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup2fithic

```bash
$ singularity exec <container> /usr/local/bin/hicup2fithic
$ podman run --it --rm --entrypoint /usr/local/bin/hicup2fithic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup2fithic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup2gothic

```bash
$ singularity exec <container> /usr/local/bin/hicup2gothic
$ podman run --it --rm --entrypoint /usr/local/bin/hicup2gothic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup2gothic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup2hicpipe

```bash
$ singularity exec <container> /usr/local/bin/hicup2hicpipe
$ podman run --it --rm --entrypoint /usr/local/bin/hicup2hicpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup2hicpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup2homer

```bash
$ singularity exec <container> /usr/local/bin/hicup2homer
$ podman run --it --rm --entrypoint /usr/local/bin/hicup2homer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup2homer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup2juicer

```bash
$ singularity exec <container> /usr/local/bin/hicup2juicer
$ podman run --it --rm --entrypoint /usr/local/bin/hicup2juicer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup2juicer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup_capture

```bash
$ singularity exec <container> /usr/local/bin/hicup_capture
$ podman run --it --rm --entrypoint /usr/local/bin/hicup_capture   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup_capture   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup_checker

```bash
$ singularity exec <container> /usr/local/bin/hicup_checker
$ podman run --it --rm --entrypoint /usr/local/bin/hicup_checker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup_checker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup_deduplicator

```bash
$ singularity exec <container> /usr/local/bin/hicup_deduplicator
$ podman run --it --rm --entrypoint /usr/local/bin/hicup_deduplicator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup_deduplicator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup_digester

```bash
$ singularity exec <container> /usr/local/bin/hicup_digester
$ podman run --it --rm --entrypoint /usr/local/bin/hicup_digester   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup_digester   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup_filter

```bash
$ singularity exec <container> /usr/local/bin/hicup_filter
$ podman run --it --rm --entrypoint /usr/local/bin/hicup_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup_mapper

```bash
$ singularity exec <container> /usr/local/bin/hicup_mapper
$ podman run --it --rm --entrypoint /usr/local/bin/hicup_mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup_mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup_module.pm

```bash
$ singularity exec <container> /usr/local/bin/hicup_module.pm
$ podman run --it --rm --entrypoint /usr/local/bin/hicup_module.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup_module.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup_reporter

```bash
$ singularity exec <container> /usr/local/bin/hicup_reporter
$ podman run --it --rm --entrypoint /usr/local/bin/hicup_reporter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup_reporter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicup_truncater

```bash
$ singularity exec <container> /usr/local/bin/hicup_truncater
$ podman run --it --rm --entrypoint /usr/local/bin/hicup_truncater   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicup_truncater   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_hic_array.pl

```bash
$ singularity exec <container> /usr/local/bin/make_hic_array.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_hic_array.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_hic_array.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
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