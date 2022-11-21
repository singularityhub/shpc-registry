---
layout: container
name:  "quay.io/biocontainers/quake"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/quake/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/quake/container.yaml"
updated_at: "2022-11-21 13:53:49.219898"
latest: "0.3.5--py27hed98c23_4"
container_url: "https://biocontainers.pro/tools/quake"
aliases:
 - "build_bithash"
 - "correct"
 - "correct_stats"
 - "count-kmers"
 - "count-qmers"
 - "count_qmers"
 - "cov_model.py"
 - "cov_model.r"
 - "cov_model_qmer.r"
 - "kmer_hist.r"
 - "quake.py"
 - "reduce-kmers"
 - "reduce-qmers"
 - "trim"
 - "jellyfish"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "c89"
 - "c99"
versions:
 - "0.3.5--py27hed98c23_4"
description: "shpc-registry automated BioContainers addition for quake"
config: {"url": "https://biocontainers.pro/tools/quake", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for quake", "latest": {"0.3.5--py27hed98c23_4": "sha256:f0031eb32c61e5e62c2aab2b1e3b3742a674c03024b478cd8e07e7da9b57d36e"}, "tags": {"0.3.5--py27hed98c23_4": "sha256:f0031eb32c61e5e62c2aab2b1e3b3742a674c03024b478cd8e07e7da9b57d36e"}, "docker": "quay.io/biocontainers/quake", "aliases": {"build_bithash": "/usr/local/bin/build_bithash", "correct": "/usr/local/bin/correct", "correct_stats": "/usr/local/bin/correct_stats", "count-kmers": "/usr/local/bin/count-kmers", "count-qmers": "/usr/local/bin/count-qmers", "count_qmers": "/usr/local/bin/count_qmers", "cov_model.py": "/usr/local/bin/cov_model.py", "cov_model.r": "/usr/local/bin/cov_model.r", "cov_model_qmer.r": "/usr/local/bin/cov_model_qmer.r", "kmer_hist.r": "/usr/local/bin/kmer_hist.r", "quake.py": "/usr/local/bin/quake.py", "reduce-kmers": "/usr/local/bin/reduce-kmers", "reduce-qmers": "/usr/local/bin/reduce-qmers", "trim": "/usr/local/bin/trim", "jellyfish": "/usr/local/bin/jellyfish", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/quake.
shpc-registry automated BioContainers addition for quake
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/quake
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/quake:0.3.5--py27hed98c23_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/quake/0.3.5--py27hed98c23_4
$ module help quay.io/biocontainers/quake/0.3.5--py27hed98c23_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quake-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quake-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quake-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quake-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quake-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quake-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### build_bithash

```bash
$ singularity exec <container> /usr/local/bin/build_bithash
$ podman run --it --rm --entrypoint /usr/local/bin/build_bithash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_bithash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correct

```bash
$ singularity exec <container> /usr/local/bin/correct
$ podman run --it --rm --entrypoint /usr/local/bin/correct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correct_stats

```bash
$ singularity exec <container> /usr/local/bin/correct_stats
$ podman run --it --rm --entrypoint /usr/local/bin/correct_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correct_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count-kmers

```bash
$ singularity exec <container> /usr/local/bin/count-kmers
$ podman run --it --rm --entrypoint /usr/local/bin/count-kmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count-kmers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count-qmers

```bash
$ singularity exec <container> /usr/local/bin/count-qmers
$ podman run --it --rm --entrypoint /usr/local/bin/count-qmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count-qmers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count_qmers

```bash
$ singularity exec <container> /usr/local/bin/count_qmers
$ podman run --it --rm --entrypoint /usr/local/bin/count_qmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count_qmers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cov_model.py

```bash
$ singularity exec <container> /usr/local/bin/cov_model.py
$ podman run --it --rm --entrypoint /usr/local/bin/cov_model.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cov_model.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cov_model.r

```bash
$ singularity exec <container> /usr/local/bin/cov_model.r
$ podman run --it --rm --entrypoint /usr/local/bin/cov_model.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cov_model.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cov_model_qmer.r

```bash
$ singularity exec <container> /usr/local/bin/cov_model_qmer.r
$ podman run --it --rm --entrypoint /usr/local/bin/cov_model_qmer.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cov_model_qmer.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer_hist.r

```bash
$ singularity exec <container> /usr/local/bin/kmer_hist.r
$ podman run --it --rm --entrypoint /usr/local/bin/kmer_hist.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer_hist.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quake.py

```bash
$ singularity exec <container> /usr/local/bin/quake.py
$ podman run --it --rm --entrypoint /usr/local/bin/quake.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quake.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reduce-kmers

```bash
$ singularity exec <container> /usr/local/bin/reduce-kmers
$ podman run --it --rm --entrypoint /usr/local/bin/reduce-kmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reduce-kmers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reduce-qmers

```bash
$ singularity exec <container> /usr/local/bin/reduce-qmers
$ podman run --it --rm --entrypoint /usr/local/bin/reduce-qmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reduce-qmers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim

```bash
$ singularity exec <container> /usr/local/bin/trim
$ podman run --it --rm --entrypoint /usr/local/bin/trim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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