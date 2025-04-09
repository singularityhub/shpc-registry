---
layout: container
name:  "quay.io/biocontainers/hifiadapterfilt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hifiadapterfilt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hifiadapterfilt/container.yaml"
updated_at: "2025-04-09 03:40:27.233393"
latest: "3.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hifiadapterfilt"
aliases:
 - "action_report.py"
 - "blast_names_mapping.tsv"
 - "classify_taxonomy.py"
 - "gx"
 - "hifiadapterfilt.bib"
 - "hifiadapterfilt.ris"
 - "hifiadapterfilt.sh"
 - "hifiadapterfiltFCS.sh"
 - "pbadapterfilt.sh"
 - "pv"
 - "rclone"
 - "run_gx.py"
 - "sync_files.py"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "bsmp2info"
 - "fsa2xml"
 - "gbf2info"
 - "just-top-hits"
 - "systematic-mutations"
 - "gunzip"
 - "gzexe"
 - "gzip"
 - "uncompress"
 - "zcat"
 - "zcmp"
 - "zdiff"
 - "zegrep"
 - "zfgrep"
 - "zforce"
 - "zgrep"
 - "zmore"
 - "znew"
 - "egrep"
 - "fgrep"
 - "grep"
versions:
 - "3.0.0--hdfd78af_0"
description: "singularity registry hpc automated addition for hifiadapterfilt"
config: {"url": "https://biocontainers.pro/tools/hifiadapterfilt", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hifiadapterfilt", "latest": {"3.0.0--hdfd78af_0": "sha256:ce791533ef2066f830ace1b7c8e7250e8b36cd809cf3cdb53e5ad6851451d6a3"}, "tags": {"3.0.0--hdfd78af_0": "sha256:ce791533ef2066f830ace1b7c8e7250e8b36cd809cf3cdb53e5ad6851451d6a3"}, "docker": "quay.io/biocontainers/hifiadapterfilt", "aliases": {"action_report.py": "/usr/local/bin/action_report.py", "blast_names_mapping.tsv": "/usr/local/bin/blast_names_mapping.tsv", "classify_taxonomy.py": "/usr/local/bin/classify_taxonomy.py", "gx": "/usr/local/bin/gx", "hifiadapterfilt.bib": "/usr/local/bin/hifiadapterfilt.bib", "hifiadapterfilt.ris": "/usr/local/bin/hifiadapterfilt.ris", "hifiadapterfilt.sh": "/usr/local/bin/hifiadapterfilt.sh", "hifiadapterfiltFCS.sh": "/usr/local/bin/hifiadapterfiltFCS.sh", "pbadapterfilt.sh": "/usr/local/bin/pbadapterfilt.sh", "pv": "/usr/local/bin/pv", "rclone": "/usr/local/bin/rclone", "run_gx.py": "/usr/local/bin/run_gx.py", "sync_files.py": "/usr/local/bin/sync_files.py", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "bsmp2info": "/usr/local/bin/bsmp2info", "fsa2xml": "/usr/local/bin/fsa2xml", "gbf2info": "/usr/local/bin/gbf2info", "just-top-hits": "/usr/local/bin/just-top-hits", "systematic-mutations": "/usr/local/bin/systematic-mutations", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew", "egrep": "/usr/local/bin/egrep", "fgrep": "/usr/local/bin/fgrep", "grep": "/usr/local/bin/grep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hifiadapterfilt.
singularity registry hpc automated addition for hifiadapterfilt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hifiadapterfilt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hifiadapterfilt:3.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hifiadapterfilt/3.0.0--hdfd78af_0
$ module help quay.io/biocontainers/hifiadapterfilt/3.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hifiadapterfilt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hifiadapterfilt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hifiadapterfilt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hifiadapterfilt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hifiadapterfilt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hifiadapterfilt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### action_report.py

```bash
$ singularity exec <container> /usr/local/bin/action_report.py
$ podman run --it --rm --entrypoint /usr/local/bin/action_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/action_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_names_mapping.tsv

```bash
$ singularity exec <container> /usr/local/bin/blast_names_mapping.tsv
$ podman run --it --rm --entrypoint /usr/local/bin/blast_names_mapping.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_names_mapping.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classify_taxonomy.py

```bash
$ singularity exec <container> /usr/local/bin/classify_taxonomy.py
$ podman run --it --rm --entrypoint /usr/local/bin/classify_taxonomy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classify_taxonomy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx

```bash
$ singularity exec <container> /usr/local/bin/gx
$ podman run --it --rm --entrypoint /usr/local/bin/gx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hifiadapterfilt.bib

```bash
$ singularity exec <container> /usr/local/bin/hifiadapterfilt.bib
$ podman run --it --rm --entrypoint /usr/local/bin/hifiadapterfilt.bib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hifiadapterfilt.bib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hifiadapterfilt.ris

```bash
$ singularity exec <container> /usr/local/bin/hifiadapterfilt.ris
$ podman run --it --rm --entrypoint /usr/local/bin/hifiadapterfilt.ris   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hifiadapterfilt.ris   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hifiadapterfilt.sh

```bash
$ singularity exec <container> /usr/local/bin/hifiadapterfilt.sh
$ podman run --it --rm --entrypoint /usr/local/bin/hifiadapterfilt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hifiadapterfilt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hifiadapterfiltFCS.sh

```bash
$ singularity exec <container> /usr/local/bin/hifiadapterfiltFCS.sh
$ podman run --it --rm --entrypoint /usr/local/bin/hifiadapterfiltFCS.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hifiadapterfiltFCS.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbadapterfilt.sh

```bash
$ singularity exec <container> /usr/local/bin/pbadapterfilt.sh
$ podman run --it --rm --entrypoint /usr/local/bin/pbadapterfilt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbadapterfilt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pv

```bash
$ singularity exec <container> /usr/local/bin/pv
$ podman run --it --rm --entrypoint /usr/local/bin/pv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rclone

```bash
$ singularity exec <container> /usr/local/bin/rclone
$ podman run --it --rm --entrypoint /usr/local/bin/rclone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rclone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_gx.py

```bash
$ singularity exec <container> /usr/local/bin/run_gx.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_gx.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_gx.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sync_files.py

```bash
$ singularity exec <container> /usr/local/bin/sync_files.py
$ podman run --it --rm --entrypoint /usr/local/bin/sync_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sync_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsmp2info

```bash
$ singularity exec <container> /usr/local/bin/bsmp2info
$ podman run --it --rm --entrypoint /usr/local/bin/bsmp2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsmp2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fsa2xml

```bash
$ singularity exec <container> /usr/local/bin/fsa2xml
$ podman run --it --rm --entrypoint /usr/local/bin/fsa2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fsa2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2info

```bash
$ singularity exec <container> /usr/local/bin/gbf2info
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### just-top-hits

```bash
$ singularity exec <container> /usr/local/bin/just-top-hits
$ podman run --it --rm --entrypoint /usr/local/bin/just-top-hits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/just-top-hits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### systematic-mutations

```bash
$ singularity exec <container> /usr/local/bin/systematic-mutations
$ podman run --it --rm --entrypoint /usr/local/bin/systematic-mutations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/systematic-mutations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gunzip

```bash
$ singularity exec <container> /usr/local/bin/gunzip
$ podman run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzexe

```bash
$ singularity exec <container> /usr/local/bin/gzexe
$ podman run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzip

```bash
$ singularity exec <container> /usr/local/bin/gzip
$ podman run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uncompress

```bash
$ singularity exec <container> /usr/local/bin/uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcat

```bash
$ singularity exec <container> /usr/local/bin/zcat
$ podman run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcmp

```bash
$ singularity exec <container> /usr/local/bin/zcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zdiff

```bash
$ singularity exec <container> /usr/local/bin/zdiff
$ podman run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zegrep

```bash
$ singularity exec <container> /usr/local/bin/zegrep
$ podman run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfgrep

```bash
$ singularity exec <container> /usr/local/bin/zfgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zforce

```bash
$ singularity exec <container> /usr/local/bin/zforce
$ podman run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zgrep

```bash
$ singularity exec <container> /usr/local/bin/zgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmore

```bash
$ singularity exec <container> /usr/local/bin/zmore
$ podman run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### znew

```bash
$ singularity exec <container> /usr/local/bin/znew
$ podman run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### egrep

```bash
$ singularity exec <container> /usr/local/bin/egrep
$ podman run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fgrep

```bash
$ singularity exec <container> /usr/local/bin/fgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grep

```bash
$ singularity exec <container> /usr/local/bin/grep
$ podman run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
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