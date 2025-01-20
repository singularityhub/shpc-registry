---
layout: container
name:  "quay.io/biocontainers/targqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/targqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/targqc/container.yaml"
updated_at: "2025-01-20 03:13:57.150458"
latest: "1.8.1--pyh5ca1d4c_1"
container_url: "https://biocontainers.pro/tools/targqc"
aliases:
 - "annotate_bed.py"
 - "cols"
 - "ipcluster"
 - "ipcontroller"
 - "ipengine"
 - "ldc-build-runtime"
 - "ldc-profdata"
 - "ldc-prune-cache"
 - "ldc2"
 - "ldmd2"
 - "qualimap"
 - "tabutils"
 - "targqc"
 - "tsv"
 - "sambamba"
 - "coverage"
 - "gffutils-cli"
 - "intersection_matrix.py"
 - "intron_exon_reads.py"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
 - "jupyter-run"
 - "nosetests"
 - "pbt_plotting_example.py"
versions:
 - "1.8.1--pyh5ca1d4c_1"
description: "shpc-registry automated BioContainers addition for targqc"
config: {"url": "https://biocontainers.pro/tools/targqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for targqc", "latest": {"1.8.1--pyh5ca1d4c_1": "sha256:9ce968510525b18152e6826cca6d5b2d50712a7747119a0175b4ef75a29d66f5"}, "tags": {"1.8.1--pyh5ca1d4c_1": "sha256:9ce968510525b18152e6826cca6d5b2d50712a7747119a0175b4ef75a29d66f5"}, "docker": "quay.io/biocontainers/targqc", "aliases": {"annotate_bed.py": "/usr/local/bin/annotate_bed.py", "cols": "/usr/local/bin/cols", "ipcluster": "/usr/local/bin/ipcluster", "ipcontroller": "/usr/local/bin/ipcontroller", "ipengine": "/usr/local/bin/ipengine", "ldc-build-runtime": "/usr/local/bin/ldc-build-runtime", "ldc-profdata": "/usr/local/bin/ldc-profdata", "ldc-prune-cache": "/usr/local/bin/ldc-prune-cache", "ldc2": "/usr/local/bin/ldc2", "ldmd2": "/usr/local/bin/ldmd2", "qualimap": "/usr/local/bin/qualimap", "tabutils": "/usr/local/bin/tabutils", "targqc": "/usr/local/bin/targqc", "tsv": "/usr/local/bin/tsv", "sambamba": "/usr/local/bin/sambamba", "coverage": "/usr/local/bin/coverage", "gffutils-cli": "/usr/local/bin/gffutils-cli", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec", "jupyter-run": "/usr/local/bin/jupyter-run", "nosetests": "/usr/local/bin/nosetests", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/targqc.
shpc-registry automated BioContainers addition for targqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/targqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/targqc:1.8.1--pyh5ca1d4c_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/targqc/1.8.1--pyh5ca1d4c_1
$ module help quay.io/biocontainers/targqc/1.8.1--pyh5ca1d4c_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### targqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### targqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### targqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### targqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### targqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### targqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annotate_bed.py

```bash
$ singularity exec <container> /usr/local/bin/annotate_bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cols

```bash
$ singularity exec <container> /usr/local/bin/cols
$ podman run --it --rm --entrypoint /usr/local/bin/cols   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cols   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcluster

```bash
$ singularity exec <container> /usr/local/bin/ipcluster
$ podman run --it --rm --entrypoint /usr/local/bin/ipcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcontroller

```bash
$ singularity exec <container> /usr/local/bin/ipcontroller
$ podman run --it --rm --entrypoint /usr/local/bin/ipcontroller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcontroller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipengine

```bash
$ singularity exec <container> /usr/local/bin/ipengine
$ podman run --it --rm --entrypoint /usr/local/bin/ipengine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipengine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-build-runtime

```bash
$ singularity exec <container> /usr/local/bin/ldc-build-runtime
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-build-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-build-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-profdata

```bash
$ singularity exec <container> /usr/local/bin/ldc-profdata
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-profdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-profdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-prune-cache

```bash
$ singularity exec <container> /usr/local/bin/ldc-prune-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-prune-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-prune-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc2

```bash
$ singularity exec <container> /usr/local/bin/ldc2
$ podman run --it --rm --entrypoint /usr/local/bin/ldc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldmd2

```bash
$ singularity exec <container> /usr/local/bin/ldmd2
$ podman run --it --rm --entrypoint /usr/local/bin/ldmd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldmd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualimap

```bash
$ singularity exec <container> /usr/local/bin/qualimap
$ podman run --it --rm --entrypoint /usr/local/bin/qualimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabutils

```bash
$ singularity exec <container> /usr/local/bin/tabutils
$ podman run --it --rm --entrypoint /usr/local/bin/tabutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### targqc

```bash
$ singularity exec <container> /usr/local/bin/targqc
$ podman run --it --rm --entrypoint /usr/local/bin/targqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/targqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv

```bash
$ singularity exec <container> /usr/local/bin/tsv
$ podman run --it --rm --entrypoint /usr/local/bin/tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sambamba

```bash
$ singularity exec <container> /usr/local/bin/sambamba
$ podman run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage

```bash
$ singularity exec <container> /usr/local/bin/coverage
$ podman run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffutils-cli

```bash
$ singularity exec <container> /usr/local/bin/gffutils-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersection_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/intersection_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron_exon_reads.py

```bash
$ singularity exec <container> /usr/local/bin/intron_exon_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernelspec

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernelspec
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-run

```bash
$ singularity exec <container> /usr/local/bin/jupyter-run
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests

```bash
$ singularity exec <container> /usr/local/bin/nosetests
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbt_plotting_example.py

```bash
$ singularity exec <container> /usr/local/bin/pbt_plotting_example.py
$ podman run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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