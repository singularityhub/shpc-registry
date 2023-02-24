---
layout: container
name:  "quay.io/biocontainers/pbipa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbipa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbipa/container.yaml"
updated_at: "2023-02-24 03:08:03.718283"
latest: "1.8.0--hbd632db_1"
container_url: "https://biocontainers.pro/tools/pbipa"
aliases:
 - "falconc"
 - "ipa"
 - "ipa2-task"
 - "ipa2_graph_to_contig"
 - "ipa2_ovlp_to_graph"
 - "ipa_purge_dups"
 - "ipa_purge_dups_calcuts"
 - "ipa_purge_dups_get_seqs"
 - "ipa_purge_dups_ngscstat"
 - "ipa_purge_dups_pbcstat"
 - "ipa_purge_dups_split_fa"
 - "nighthawk"
 - "pancake"
 - "pblayout"
 - "plac_runner.py"
 - "yte"
 - "racon"
 - "rampler"
 - "racon_wrapper"
 - "pulptest"
 - "cbc"
 - "clp"
 - "snakemake"
 - "snakemake-bash-completion"
versions:
 - "1.8.0--hbd632db_1"
description: "shpc-registry automated BioContainers addition for pbipa"
config: {"url": "https://biocontainers.pro/tools/pbipa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbipa", "latest": {"1.8.0--hbd632db_1": "sha256:bccb1909c5acb769b5cdd6173d406f3da45b695150099d451c17d6dfd1f26395"}, "tags": {"1.8.0--hbd632db_1": "sha256:bccb1909c5acb769b5cdd6173d406f3da45b695150099d451c17d6dfd1f26395"}, "docker": "quay.io/biocontainers/pbipa", "aliases": {"falconc": "/usr/local/bin/falconc", "ipa": "/usr/local/bin/ipa", "ipa2-task": "/usr/local/bin/ipa2-task", "ipa2_graph_to_contig": "/usr/local/bin/ipa2_graph_to_contig", "ipa2_ovlp_to_graph": "/usr/local/bin/ipa2_ovlp_to_graph", "ipa_purge_dups": "/usr/local/bin/ipa_purge_dups", "ipa_purge_dups_calcuts": "/usr/local/bin/ipa_purge_dups_calcuts", "ipa_purge_dups_get_seqs": "/usr/local/bin/ipa_purge_dups_get_seqs", "ipa_purge_dups_ngscstat": "/usr/local/bin/ipa_purge_dups_ngscstat", "ipa_purge_dups_pbcstat": "/usr/local/bin/ipa_purge_dups_pbcstat", "ipa_purge_dups_split_fa": "/usr/local/bin/ipa_purge_dups_split_fa", "nighthawk": "/usr/local/bin/nighthawk", "pancake": "/usr/local/bin/pancake", "pblayout": "/usr/local/bin/pblayout", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "racon": "/usr/local/bin/racon", "rampler": "/usr/local/bin/rampler", "racon_wrapper": "/usr/local/bin/racon_wrapper", "pulptest": "/usr/local/bin/pulptest", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbipa.
shpc-registry automated BioContainers addition for pbipa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbipa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbipa:1.8.0--hbd632db_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbipa/1.8.0--hbd632db_1
$ module help quay.io/biocontainers/pbipa/1.8.0--hbd632db_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbipa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbipa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbipa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbipa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbipa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbipa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### falconc

```bash
$ singularity exec <container> /usr/local/bin/falconc
$ podman run --it --rm --entrypoint /usr/local/bin/falconc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/falconc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipa

```bash
$ singularity exec <container> /usr/local/bin/ipa
$ podman run --it --rm --entrypoint /usr/local/bin/ipa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipa2-task

```bash
$ singularity exec <container> /usr/local/bin/ipa2-task
$ podman run --it --rm --entrypoint /usr/local/bin/ipa2-task   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipa2-task   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipa2_graph_to_contig

```bash
$ singularity exec <container> /usr/local/bin/ipa2_graph_to_contig
$ podman run --it --rm --entrypoint /usr/local/bin/ipa2_graph_to_contig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipa2_graph_to_contig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipa2_ovlp_to_graph

```bash
$ singularity exec <container> /usr/local/bin/ipa2_ovlp_to_graph
$ podman run --it --rm --entrypoint /usr/local/bin/ipa2_ovlp_to_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipa2_ovlp_to_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipa_purge_dups

```bash
$ singularity exec <container> /usr/local/bin/ipa_purge_dups
$ podman run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipa_purge_dups_calcuts

```bash
$ singularity exec <container> /usr/local/bin/ipa_purge_dups_calcuts
$ podman run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups_calcuts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups_calcuts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipa_purge_dups_get_seqs

```bash
$ singularity exec <container> /usr/local/bin/ipa_purge_dups_get_seqs
$ podman run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups_get_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups_get_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipa_purge_dups_ngscstat

```bash
$ singularity exec <container> /usr/local/bin/ipa_purge_dups_ngscstat
$ podman run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups_ngscstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups_ngscstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipa_purge_dups_pbcstat

```bash
$ singularity exec <container> /usr/local/bin/ipa_purge_dups_pbcstat
$ podman run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups_pbcstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups_pbcstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipa_purge_dups_split_fa

```bash
$ singularity exec <container> /usr/local/bin/ipa_purge_dups_split_fa
$ podman run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups_split_fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipa_purge_dups_split_fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nighthawk

```bash
$ singularity exec <container> /usr/local/bin/nighthawk
$ podman run --it --rm --entrypoint /usr/local/bin/nighthawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nighthawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pancake

```bash
$ singularity exec <container> /usr/local/bin/pancake
$ podman run --it --rm --entrypoint /usr/local/bin/pancake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pancake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pblayout

```bash
$ singularity exec <container> /usr/local/bin/pblayout
$ podman run --it --rm --entrypoint /usr/local/bin/pblayout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pblayout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon

```bash
$ singularity exec <container> /usr/local/bin/racon
$ podman run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rampler

```bash
$ singularity exec <container> /usr/local/bin/rampler
$ podman run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon_wrapper

```bash
$ singularity exec <container> /usr/local/bin/racon_wrapper
$ podman run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake-bash-completion

```bash
$ singularity exec <container> /usr/local/bin/snakemake-bash-completion
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
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