---
layout: container
name:  "quay.io/biocontainers/covsonar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/covsonar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/covsonar/container.yaml"
updated_at: "2024-08-22 03:17:41.804972"
latest: "2.0.0a1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/covsonar"
aliases:
 - "mpire-dashboard"
 - "sonar"
 - "xmlget"
 - "xmltext"
 - "aaindexextract"
 - "abiview"
 - "acdc"
 - "acdgalaxy"
 - "acdlog"
 - "acdpretty"
 - "acdtable"
 - "acdtrace"
 - "acdvalid"
 - "aligncopy"
 - "aligncopypair"
 - "antigenic"
 - "assemblyget"
 - "backtranambig"
 - "backtranseq"
 - "banana"
 - "biosed"
 - "btwisted"
 - "cachedas"
 - "cachedbfetch"
 - "cacheebeyesearch"
 - "cacheensembl"
 - "chaos"
versions:
 - "2.0.0a1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for covsonar"
config: {"url": "https://biocontainers.pro/tools/covsonar", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for covsonar", "latest": {"2.0.0a1--pyhdfd78af_0": "sha256:f0383915785463e27f8f543c6b09388ef90258ff6d6450b2f0fa7c8e44c723dd"}, "tags": {"2.0.0a1--pyhdfd78af_0": "sha256:f0383915785463e27f8f543c6b09388ef90258ff6d6450b2f0fa7c8e44c723dd"}, "docker": "quay.io/biocontainers/covsonar", "aliases": {"mpire-dashboard": "/usr/local/bin/mpire-dashboard", "sonar": "/usr/local/bin/sonar", "xmlget": "/usr/local/bin/xmlget", "xmltext": "/usr/local/bin/xmltext", "aaindexextract": "/usr/local/bin/aaindexextract", "abiview": "/usr/local/bin/abiview", "acdc": "/usr/local/bin/acdc", "acdgalaxy": "/usr/local/bin/acdgalaxy", "acdlog": "/usr/local/bin/acdlog", "acdpretty": "/usr/local/bin/acdpretty", "acdtable": "/usr/local/bin/acdtable", "acdtrace": "/usr/local/bin/acdtrace", "acdvalid": "/usr/local/bin/acdvalid", "aligncopy": "/usr/local/bin/aligncopy", "aligncopypair": "/usr/local/bin/aligncopypair", "antigenic": "/usr/local/bin/antigenic", "assemblyget": "/usr/local/bin/assemblyget", "backtranambig": "/usr/local/bin/backtranambig", "backtranseq": "/usr/local/bin/backtranseq", "banana": "/usr/local/bin/banana", "biosed": "/usr/local/bin/biosed", "btwisted": "/usr/local/bin/btwisted", "cachedas": "/usr/local/bin/cachedas", "cachedbfetch": "/usr/local/bin/cachedbfetch", "cacheebeyesearch": "/usr/local/bin/cacheebeyesearch", "cacheensembl": "/usr/local/bin/cacheensembl", "chaos": "/usr/local/bin/chaos"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/covsonar.
singularity registry hpc automated addition for covsonar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/covsonar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/covsonar:2.0.0a1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/covsonar/2.0.0a1--pyhdfd78af_0
$ module help quay.io/biocontainers/covsonar/2.0.0a1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### covsonar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### covsonar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### covsonar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### covsonar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### covsonar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### covsonar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mpire-dashboard

```bash
$ singularity exec <container> /usr/local/bin/mpire-dashboard
$ podman run --it --rm --entrypoint /usr/local/bin/mpire-dashboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpire-dashboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sonar

```bash
$ singularity exec <container> /usr/local/bin/sonar
$ podman run --it --rm --entrypoint /usr/local/bin/sonar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sonar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmlget

```bash
$ singularity exec <container> /usr/local/bin/xmlget
$ podman run --it --rm --entrypoint /usr/local/bin/xmlget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmltext

```bash
$ singularity exec <container> /usr/local/bin/xmltext
$ podman run --it --rm --entrypoint /usr/local/bin/xmltext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmltext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aaindexextract

```bash
$ singularity exec <container> /usr/local/bin/aaindexextract
$ podman run --it --rm --entrypoint /usr/local/bin/aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abiview

```bash
$ singularity exec <container> /usr/local/bin/abiview
$ podman run --it --rm --entrypoint /usr/local/bin/abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdc

```bash
$ singularity exec <container> /usr/local/bin/acdc
$ podman run --it --rm --entrypoint /usr/local/bin/acdc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdgalaxy

```bash
$ singularity exec <container> /usr/local/bin/acdgalaxy
$ podman run --it --rm --entrypoint /usr/local/bin/acdgalaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdgalaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdlog

```bash
$ singularity exec <container> /usr/local/bin/acdlog
$ podman run --it --rm --entrypoint /usr/local/bin/acdlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdpretty

```bash
$ singularity exec <container> /usr/local/bin/acdpretty
$ podman run --it --rm --entrypoint /usr/local/bin/acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdtable

```bash
$ singularity exec <container> /usr/local/bin/acdtable
$ podman run --it --rm --entrypoint /usr/local/bin/acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdtrace

```bash
$ singularity exec <container> /usr/local/bin/acdtrace
$ podman run --it --rm --entrypoint /usr/local/bin/acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdvalid

```bash
$ singularity exec <container> /usr/local/bin/acdvalid
$ podman run --it --rm --entrypoint /usr/local/bin/acdvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aligncopy

```bash
$ singularity exec <container> /usr/local/bin/aligncopy
$ podman run --it --rm --entrypoint /usr/local/bin/aligncopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aligncopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aligncopypair

```bash
$ singularity exec <container> /usr/local/bin/aligncopypair
$ podman run --it --rm --entrypoint /usr/local/bin/aligncopypair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aligncopypair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### antigenic

```bash
$ singularity exec <container> /usr/local/bin/antigenic
$ podman run --it --rm --entrypoint /usr/local/bin/antigenic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/antigenic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assemblyget

```bash
$ singularity exec <container> /usr/local/bin/assemblyget
$ podman run --it --rm --entrypoint /usr/local/bin/assemblyget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assemblyget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### backtranambig

```bash
$ singularity exec <container> /usr/local/bin/backtranambig
$ podman run --it --rm --entrypoint /usr/local/bin/backtranambig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/backtranambig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### backtranseq

```bash
$ singularity exec <container> /usr/local/bin/backtranseq
$ podman run --it --rm --entrypoint /usr/local/bin/backtranseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/backtranseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### banana

```bash
$ singularity exec <container> /usr/local/bin/banana
$ podman run --it --rm --entrypoint /usr/local/bin/banana   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/banana   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biosed

```bash
$ singularity exec <container> /usr/local/bin/biosed
$ podman run --it --rm --entrypoint /usr/local/bin/biosed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biosed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### btwisted

```bash
$ singularity exec <container> /usr/local/bin/btwisted
$ podman run --it --rm --entrypoint /usr/local/bin/btwisted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/btwisted   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cachedas

```bash
$ singularity exec <container> /usr/local/bin/cachedas
$ podman run --it --rm --entrypoint /usr/local/bin/cachedas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cachedas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cachedbfetch

```bash
$ singularity exec <container> /usr/local/bin/cachedbfetch
$ podman run --it --rm --entrypoint /usr/local/bin/cachedbfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cachedbfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacheebeyesearch

```bash
$ singularity exec <container> /usr/local/bin/cacheebeyesearch
$ podman run --it --rm --entrypoint /usr/local/bin/cacheebeyesearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacheebeyesearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacheensembl

```bash
$ singularity exec <container> /usr/local/bin/cacheensembl
$ podman run --it --rm --entrypoint /usr/local/bin/cacheensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacheensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chaos

```bash
$ singularity exec <container> /usr/local/bin/chaos
$ podman run --it --rm --entrypoint /usr/local/bin/chaos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chaos   -v ${PWD} -w ${PWD} <container> -c " $@"
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