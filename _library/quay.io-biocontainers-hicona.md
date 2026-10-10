---
layout: container
name:  "quay.io/biocontainers/hicona"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hicona/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hicona/container.yaml"
updated_at: "2026-10-10 19:27:30.274752"
latest: "0.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/hicona"
aliases:
 - "boostchr.pl"
 - "column_remover.pl.bak"
 - "coolbox"
 - "cooltools"
 - "create_randompairs.pl"
 - "duplicate_header_remover.pl.bak"
 - "fragment_4dnpairs.pl.bak"
 - "juicer_shortform2pairs.pl.bak"
 - "jupyter-builder"
 - "merged_nodup2pairs.pl.bak"
 - "mistune"
 - "numpydoc"
 - "old_merged_nodup2pairs.pl.bak"
 - "voila"
 - "websockets"
 - "jlpm"
 - "jupyter-lab"
 - "jupyter-labextension"
 - "jupyter-labhub"
 - "jupyter-events"
 - "pyjson5"
 - "ojph_compress"
 - "ojph_expand"
 - "jupyter-server"
 - "seq_cache_populate.py"
 - "debugpy-adapter"
 - "jupyter-console"
 - "cooler"
 - "debugpy"
 - "cffi-gen-src"
 - "bam2pairs"
 - "column_remover.pl"
 - "duplicate_header_remover.pl"
 - "fragment_4dnpairs.pl"
 - "juicer_shortform2pairs.pl"
 - "merge-pairs.sh"
 - "merged_nodup2pairs.pl"
 - "old_merged_nodup2pairs.pl"
 - "pairix"
 - "pairs_merger"
versions:
 - "0.0.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for hicona"
config: {"url": "https://biocontainers.pro/tools/hicona", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hicona", "latest": {"0.0.2--pyhdfd78af_0": "sha256:d28db6048e2635f2612212c197fc5f7585f2ebf858caa055ba6f4c99fb478114"}, "tags": {"0.0.2--pyhdfd78af_0": "sha256:d28db6048e2635f2612212c197fc5f7585f2ebf858caa055ba6f4c99fb478114"}, "docker": "quay.io/biocontainers/hicona", "aliases": {"boostchr.pl": "/usr/local/bin/boostchr.pl", "column_remover.pl.bak": "/usr/local/bin/column_remover.pl.bak", "coolbox": "/usr/local/bin/coolbox", "cooltools": "/usr/local/bin/cooltools", "create_randompairs.pl": "/usr/local/bin/create_randompairs.pl", "duplicate_header_remover.pl.bak": "/usr/local/bin/duplicate_header_remover.pl.bak", "fragment_4dnpairs.pl.bak": "/usr/local/bin/fragment_4dnpairs.pl.bak", "juicer_shortform2pairs.pl.bak": "/usr/local/bin/juicer_shortform2pairs.pl.bak", "jupyter-builder": "/usr/local/bin/jupyter-builder", "merged_nodup2pairs.pl.bak": "/usr/local/bin/merged_nodup2pairs.pl.bak", "mistune": "/usr/local/bin/mistune", "numpydoc": "/usr/local/bin/numpydoc", "old_merged_nodup2pairs.pl.bak": "/usr/local/bin/old_merged_nodup2pairs.pl.bak", "voila": "/usr/local/bin/voila", "websockets": "/usr/local/bin/websockets", "jlpm": "/usr/local/bin/jlpm", "jupyter-lab": "/usr/local/bin/jupyter-lab", "jupyter-labextension": "/usr/local/bin/jupyter-labextension", "jupyter-labhub": "/usr/local/bin/jupyter-labhub", "jupyter-events": "/usr/local/bin/jupyter-events", "pyjson5": "/usr/local/bin/pyjson5", "ojph_compress": "/usr/local/bin/ojph_compress", "ojph_expand": "/usr/local/bin/ojph_expand", "jupyter-server": "/usr/local/bin/jupyter-server", "seq_cache_populate.py": "/usr/local/bin/seq_cache_populate.py", "debugpy-adapter": "/usr/local/bin/debugpy-adapter", "jupyter-console": "/usr/local/bin/jupyter-console", "cooler": "/usr/local/bin/cooler", "debugpy": "/usr/local/bin/debugpy", "cffi-gen-src": "/usr/local/bin/cffi-gen-src", "bam2pairs": "/usr/local/bin/bam2pairs", "column_remover.pl": "/usr/local/bin/column_remover.pl", "duplicate_header_remover.pl": "/usr/local/bin/duplicate_header_remover.pl", "fragment_4dnpairs.pl": "/usr/local/bin/fragment_4dnpairs.pl", "juicer_shortform2pairs.pl": "/usr/local/bin/juicer_shortform2pairs.pl", "merge-pairs.sh": "/usr/local/bin/merge-pairs.sh", "merged_nodup2pairs.pl": "/usr/local/bin/merged_nodup2pairs.pl", "old_merged_nodup2pairs.pl": "/usr/local/bin/old_merged_nodup2pairs.pl", "pairix": "/usr/local/bin/pairix", "pairs_merger": "/usr/local/bin/pairs_merger"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hicona.
singularity registry hpc automated addition for hicona
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hicona
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hicona:0.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hicona/0.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/hicona/0.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hicona-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hicona-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hicona-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hicona-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hicona-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hicona-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### boostchr.pl

```bash
$ singularity exec <container> /usr/local/bin/boostchr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/boostchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/boostchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column_remover.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/column_remover.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/column_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coolbox

```bash
$ singularity exec <container> /usr/local/bin/coolbox
$ podman run --it --rm --entrypoint /usr/local/bin/coolbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coolbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cooltools

```bash
$ singularity exec <container> /usr/local/bin/cooltools
$ podman run --it --rm --entrypoint /usr/local/bin/cooltools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooltools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_randompairs.pl

```bash
$ singularity exec <container> /usr/local/bin/create_randompairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/create_randompairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_randompairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate_header_remover.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/duplicate_header_remover.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragment_4dnpairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/fragment_4dnpairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer_shortform2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/juicer_shortform2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-builder

```bash
$ singularity exec <container> /usr/local/bin/jupyter-builder
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-builder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-builder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merged_nodup2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/merged_nodup2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mistune

```bash
$ singularity exec <container> /usr/local/bin/mistune
$ podman run --it --rm --entrypoint /usr/local/bin/mistune   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mistune   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpydoc

```bash
$ singularity exec <container> /usr/local/bin/numpydoc
$ podman run --it --rm --entrypoint /usr/local/bin/numpydoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpydoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### old_merged_nodup2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/old_merged_nodup2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### voila

```bash
$ singularity exec <container> /usr/local/bin/voila
$ podman run --it --rm --entrypoint /usr/local/bin/voila   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/voila   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### websockets

```bash
$ singularity exec <container> /usr/local/bin/websockets
$ podman run --it --rm --entrypoint /usr/local/bin/websockets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/websockets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlpm

```bash
$ singularity exec <container> /usr/local/bin/jlpm
$ podman run --it --rm --entrypoint /usr/local/bin/jlpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-lab

```bash
$ singularity exec <container> /usr/local/bin/jupyter-lab
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-lab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-lab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-labextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-labextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-labextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-labextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-labhub

```bash
$ singularity exec <container> /usr/local/bin/jupyter-labhub
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-labhub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-labhub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-events

```bash
$ singularity exec <container> /usr/local/bin/jupyter-events
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyjson5

```bash
$ singularity exec <container> /usr/local/bin/pyjson5
$ podman run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ojph_compress

```bash
$ singularity exec <container> /usr/local/bin/ojph_compress
$ podman run --it --rm --entrypoint /usr/local/bin/ojph_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ojph_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ojph_expand

```bash
$ singularity exec <container> /usr/local/bin/ojph_expand
$ podman run --it --rm --entrypoint /usr/local/bin/ojph_expand   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ojph_expand   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-server

```bash
$ singularity exec <container> /usr/local/bin/jupyter-server
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.py

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.py
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy-adapter

```bash
$ singularity exec <container> /usr/local/bin/debugpy-adapter
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-console

```bash
$ singularity exec <container> /usr/local/bin/jupyter-console
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cooler

```bash
$ singularity exec <container> /usr/local/bin/cooler
$ podman run --it --rm --entrypoint /usr/local/bin/cooler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy

```bash
$ singularity exec <container> /usr/local/bin/debugpy
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cffi-gen-src

```bash
$ singularity exec <container> /usr/local/bin/cffi-gen-src
$ podman run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2pairs

```bash
$ singularity exec <container> /usr/local/bin/bam2pairs
$ podman run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/column_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate_header_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/duplicate_header_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragment_4dnpairs.pl

```bash
$ singularity exec <container> /usr/local/bin/fragment_4dnpairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer_shortform2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/juicer_shortform2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-pairs.sh

```bash
$ singularity exec <container> /usr/local/bin/merge-pairs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merged_nodup2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/merged_nodup2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### old_merged_nodup2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/old_merged_nodup2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairix

```bash
$ singularity exec <container> /usr/local/bin/pairix
$ podman run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairs_merger

```bash
$ singularity exec <container> /usr/local/bin/pairs_merger
$ podman run --it --rm --entrypoint /usr/local/bin/pairs_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairs_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
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