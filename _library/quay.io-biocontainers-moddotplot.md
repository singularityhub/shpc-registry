---
layout: container
name:  "quay.io/biocontainers/moddotplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/moddotplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/moddotplot/container.yaml"
updated_at: "2026-08-25 09:22:51.584260"
latest: "0.9.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/moddotplot"
aliases:
 - "boostchr.pl"
 - "cffi-gen-src"
 - "column_remover.pl.bak"
 - "create_randompairs.pl"
 - "duplicate_header_remover.pl.bak"
 - "fragment_4dnpairs.pl.bak"
 - "juicer_shortform2pairs.pl.bak"
 - "make_tracks_file"
 - "merged_nodup2pairs.pl.bak"
 - "moddotplot"
 - "old_merged_nodup2pairs.pl.bak"
 - "pgt"
 - "plotly"
 - "pyGenomeTracks"
 - "seq_cache_populate.py"
 - "dash-update-components"
 - "cairosvg"
 - "protoc-35.1.0"
 - "protoc-gen-upb-35.1.0"
 - "protoc-gen-upb_minitable-35.1.0"
 - "protoc-gen-upbdefs-35.1.0"
 - "renderer"
 - "dash-generate-components"
 - "cooler"
 - "cpuinfo"
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
 - "process_merged_nodup.sh"
 - "process_old_merged_nodup.sh"
 - "streamer_1d"
 - "gffutils-cli"
 - "plotly_get_chrome"
versions:
 - "0.9.9--pyhdfd78af_0"
description: "singularity registry hpc automated addition for moddotplot"
config: {"url": "https://biocontainers.pro/tools/moddotplot", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for moddotplot", "latest": {"0.9.9--pyhdfd78af_0": "sha256:5b1ebeeba95aecf41509daec7ad2cadc923bfc677e2699c533f5b597904f40f8"}, "tags": {"0.9.9--pyhdfd78af_0": "sha256:5b1ebeeba95aecf41509daec7ad2cadc923bfc677e2699c533f5b597904f40f8"}, "docker": "quay.io/biocontainers/moddotplot", "aliases": {"boostchr.pl": "/usr/local/bin/boostchr.pl", "cffi-gen-src": "/usr/local/bin/cffi-gen-src", "column_remover.pl.bak": "/usr/local/bin/column_remover.pl.bak", "create_randompairs.pl": "/usr/local/bin/create_randompairs.pl", "duplicate_header_remover.pl.bak": "/usr/local/bin/duplicate_header_remover.pl.bak", "fragment_4dnpairs.pl.bak": "/usr/local/bin/fragment_4dnpairs.pl.bak", "juicer_shortform2pairs.pl.bak": "/usr/local/bin/juicer_shortform2pairs.pl.bak", "make_tracks_file": "/usr/local/bin/make_tracks_file", "merged_nodup2pairs.pl.bak": "/usr/local/bin/merged_nodup2pairs.pl.bak", "moddotplot": "/usr/local/bin/moddotplot", "old_merged_nodup2pairs.pl.bak": "/usr/local/bin/old_merged_nodup2pairs.pl.bak", "pgt": "/usr/local/bin/pgt", "plotly": "/usr/local/bin/plotly", "pyGenomeTracks": "/usr/local/bin/pyGenomeTracks", "seq_cache_populate.py": "/usr/local/bin/seq_cache_populate.py", "dash-update-components": "/usr/local/bin/dash-update-components", "cairosvg": "/usr/local/bin/cairosvg", "protoc-35.1.0": "/usr/local/bin/protoc-35.1.0", "protoc-gen-upb-35.1.0": "/usr/local/bin/protoc-gen-upb-35.1.0", "protoc-gen-upb_minitable-35.1.0": "/usr/local/bin/protoc-gen-upb_minitable-35.1.0", "protoc-gen-upbdefs-35.1.0": "/usr/local/bin/protoc-gen-upbdefs-35.1.0", "renderer": "/usr/local/bin/renderer", "dash-generate-components": "/usr/local/bin/dash-generate-components", "cooler": "/usr/local/bin/cooler", "cpuinfo": "/usr/local/bin/cpuinfo", "bam2pairs": "/usr/local/bin/bam2pairs", "column_remover.pl": "/usr/local/bin/column_remover.pl", "duplicate_header_remover.pl": "/usr/local/bin/duplicate_header_remover.pl", "fragment_4dnpairs.pl": "/usr/local/bin/fragment_4dnpairs.pl", "juicer_shortform2pairs.pl": "/usr/local/bin/juicer_shortform2pairs.pl", "merge-pairs.sh": "/usr/local/bin/merge-pairs.sh", "merged_nodup2pairs.pl": "/usr/local/bin/merged_nodup2pairs.pl", "old_merged_nodup2pairs.pl": "/usr/local/bin/old_merged_nodup2pairs.pl", "pairix": "/usr/local/bin/pairix", "pairs_merger": "/usr/local/bin/pairs_merger", "process_merged_nodup.sh": "/usr/local/bin/process_merged_nodup.sh", "process_old_merged_nodup.sh": "/usr/local/bin/process_old_merged_nodup.sh", "streamer_1d": "/usr/local/bin/streamer_1d", "gffutils-cli": "/usr/local/bin/gffutils-cli", "plotly_get_chrome": "/usr/local/bin/plotly_get_chrome"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/moddotplot.
singularity registry hpc automated addition for moddotplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/moddotplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/moddotplot:0.9.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/moddotplot/0.9.9--pyhdfd78af_0
$ module help quay.io/biocontainers/moddotplot/0.9.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### moddotplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### moddotplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### moddotplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### moddotplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### moddotplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### moddotplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### boostchr.pl

```bash
$ singularity exec <container> /usr/local/bin/boostchr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/boostchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/boostchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cffi-gen-src

```bash
$ singularity exec <container> /usr/local/bin/cffi-gen-src
$ podman run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column_remover.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/column_remover.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/column_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### make_tracks_file

```bash
$ singularity exec <container> /usr/local/bin/make_tracks_file
$ podman run --it --rm --entrypoint /usr/local/bin/make_tracks_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_tracks_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merged_nodup2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/merged_nodup2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moddotplot

```bash
$ singularity exec <container> /usr/local/bin/moddotplot
$ podman run --it --rm --entrypoint /usr/local/bin/moddotplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moddotplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### old_merged_nodup2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/old_merged_nodup2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgt

```bash
$ singularity exec <container> /usr/local/bin/pgt
$ podman run --it --rm --entrypoint /usr/local/bin/pgt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly

```bash
$ singularity exec <container> /usr/local/bin/plotly
$ podman run --it --rm --entrypoint /usr/local/bin/plotly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyGenomeTracks

```bash
$ singularity exec <container> /usr/local/bin/pyGenomeTracks
$ podman run --it --rm --entrypoint /usr/local/bin/pyGenomeTracks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyGenomeTracks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.py

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.py
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-update-components

```bash
$ singularity exec <container> /usr/local/bin/dash-update-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cairosvg

```bash
$ singularity exec <container> /usr/local/bin/cairosvg
$ podman run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### renderer

```bash
$ singularity exec <container> /usr/local/bin/renderer
$ podman run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-generate-components

```bash
$ singularity exec <container> /usr/local/bin/dash-generate-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cooler

```bash
$ singularity exec <container> /usr/local/bin/cooler
$ podman run --it --rm --entrypoint /usr/local/bin/cooler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpuinfo

```bash
$ singularity exec <container> /usr/local/bin/cpuinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### process_merged_nodup.sh

```bash
$ singularity exec <container> /usr/local/bin/process_merged_nodup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/process_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_old_merged_nodup.sh

```bash
$ singularity exec <container> /usr/local/bin/process_old_merged_nodup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/process_old_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_old_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamer_1d

```bash
$ singularity exec <container> /usr/local/bin/streamer_1d
$ podman run --it --rm --entrypoint /usr/local/bin/streamer_1d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamer_1d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffutils-cli

```bash
$ singularity exec <container> /usr/local/bin/gffutils-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/plotly_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
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