---
layout: container
name:  "quay.io/biocontainers/salsa2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/salsa2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/salsa2/container.yaml"
updated_at: "2023-04-05 03:09:22.923018"
latest: "2.3--py27h16ec135_1"
container_url: "https://biocontainers.pro/tools/salsa2"
aliases:
 - "RE_sites.py"
 - "break_contigs"
 - "break_contigs_start"
 - "correct.py"
 - "correct_links"
 - "fast_scaled_scores.py"
 - "get_seq.py"
 - "layout_unitigs.py"
 - "make_links.py"
 - "refactor_breaks.py"
 - "run_pipeline.py"
 - "stitch.py"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "2.3--py27h16ec135_1"
description: "shpc-registry automated BioContainers addition for salsa2"
config: {"url": "https://biocontainers.pro/tools/salsa2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for salsa2", "latest": {"2.3--py27h16ec135_1": "sha256:cd6de91db7b2b19d986e25cbb2e047f51b68b7be5ab631fa2547067b6754150c"}, "tags": {"2.3--py27h16ec135_1": "sha256:cd6de91db7b2b19d986e25cbb2e047f51b68b7be5ab631fa2547067b6754150c"}, "docker": "quay.io/biocontainers/salsa2", "aliases": {"RE_sites.py": "/usr/local/bin/RE_sites.py", "break_contigs": "/usr/local/bin/break_contigs", "break_contigs_start": "/usr/local/bin/break_contigs_start", "correct.py": "/usr/local/bin/correct.py", "correct_links": "/usr/local/bin/correct_links", "fast_scaled_scores.py": "/usr/local/bin/fast_scaled_scores.py", "get_seq.py": "/usr/local/bin/get_seq.py", "layout_unitigs.py": "/usr/local/bin/layout_unitigs.py", "make_links.py": "/usr/local/bin/make_links.py", "refactor_breaks.py": "/usr/local/bin/refactor_breaks.py", "run_pipeline.py": "/usr/local/bin/run_pipeline.py", "stitch.py": "/usr/local/bin/stitch.py", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/salsa2.
shpc-registry automated BioContainers addition for salsa2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/salsa2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/salsa2:2.3--py27h16ec135_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/salsa2/2.3--py27h16ec135_1
$ module help quay.io/biocontainers/salsa2/2.3--py27h16ec135_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### salsa2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### salsa2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### salsa2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### salsa2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### salsa2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### salsa2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RE_sites.py

```bash
$ singularity exec <container> /usr/local/bin/RE_sites.py
$ podman run --it --rm --entrypoint /usr/local/bin/RE_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RE_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### break_contigs

```bash
$ singularity exec <container> /usr/local/bin/break_contigs
$ podman run --it --rm --entrypoint /usr/local/bin/break_contigs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/break_contigs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### break_contigs_start

```bash
$ singularity exec <container> /usr/local/bin/break_contigs_start
$ podman run --it --rm --entrypoint /usr/local/bin/break_contigs_start   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/break_contigs_start   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correct.py

```bash
$ singularity exec <container> /usr/local/bin/correct.py
$ podman run --it --rm --entrypoint /usr/local/bin/correct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correct_links

```bash
$ singularity exec <container> /usr/local/bin/correct_links
$ podman run --it --rm --entrypoint /usr/local/bin/correct_links   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correct_links   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast_scaled_scores.py

```bash
$ singularity exec <container> /usr/local/bin/fast_scaled_scores.py
$ podman run --it --rm --entrypoint /usr/local/bin/fast_scaled_scores.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast_scaled_scores.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_seq.py

```bash
$ singularity exec <container> /usr/local/bin/get_seq.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_seq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_seq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### layout_unitigs.py

```bash
$ singularity exec <container> /usr/local/bin/layout_unitigs.py
$ podman run --it --rm --entrypoint /usr/local/bin/layout_unitigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/layout_unitigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_links.py

```bash
$ singularity exec <container> /usr/local/bin/make_links.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_links.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_links.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refactor_breaks.py

```bash
$ singularity exec <container> /usr/local/bin/refactor_breaks.py
$ podman run --it --rm --entrypoint /usr/local/bin/refactor_breaks.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refactor_breaks.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/run_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stitch.py

```bash
$ singularity exec <container> /usr/local/bin/stitch.py
$ podman run --it --rm --entrypoint /usr/local/bin/stitch.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stitch.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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