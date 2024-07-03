---
layout: container
name:  "quay.io/biocontainers/arb-bio-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arb-bio-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arb-bio-tools/container.yaml"
updated_at: "2024-07-03 03:19:54.693501"
latest: "6.0.6--haa8b8d8_8"
container_url: "https://biocontainers.pro/tools/arb-bio-tools"
aliases:
 - "arb_2_ascii"
 - "arb_2_bin"
 - "arb_a2ps"
 - "arb_consensus_tree"
 - "arb_convert_aln"
 - "arb_db_server"
 - "arb_dnarates"
 - "arb_export_rates"
 - "arb_export_tree"
 - "arb_flush_mem"
 - "arb_gene_probe"
 - "arb_help2xml"
 - "arb_message"
 - "arb_naligner"
 - "arb_name_server"
 - "arb_notify"
 - "arb_primer"
 - "arb_probe"
 - "arb_proto_2_xsub"
 - "arb_pt_server"
 - "arb_read_tree"
 - "arb_readseq"
 - "arb_replace"
 - "arb_rnacma"
 - "arb_treegen"
 - "gio-launch-desktop"
versions:
 - "6.0.6--haa8b8d8_8"
description: "shpc-registry automated BioContainers addition for arb-bio-tools"
config: {"url": "https://biocontainers.pro/tools/arb-bio-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for arb-bio-tools", "latest": {"6.0.6--haa8b8d8_8": "sha256:af8a779cf8f62461557598eb1cdc3985e8c1f98c1f53fafe4d5a7f5805192546"}, "tags": {"6.0.6--haa8b8d8_8": "sha256:af8a779cf8f62461557598eb1cdc3985e8c1f98c1f53fafe4d5a7f5805192546"}, "docker": "quay.io/biocontainers/arb-bio-tools", "aliases": {"arb_2_ascii": "/usr/local/bin/arb_2_ascii", "arb_2_bin": "/usr/local/bin/arb_2_bin", "arb_a2ps": "/usr/local/bin/arb_a2ps", "arb_consensus_tree": "/usr/local/bin/arb_consensus_tree", "arb_convert_aln": "/usr/local/bin/arb_convert_aln", "arb_db_server": "/usr/local/bin/arb_db_server", "arb_dnarates": "/usr/local/bin/arb_dnarates", "arb_export_rates": "/usr/local/bin/arb_export_rates", "arb_export_tree": "/usr/local/bin/arb_export_tree", "arb_flush_mem": "/usr/local/bin/arb_flush_mem", "arb_gene_probe": "/usr/local/bin/arb_gene_probe", "arb_help2xml": "/usr/local/bin/arb_help2xml", "arb_message": "/usr/local/bin/arb_message", "arb_naligner": "/usr/local/bin/arb_naligner", "arb_name_server": "/usr/local/bin/arb_name_server", "arb_notify": "/usr/local/bin/arb_notify", "arb_primer": "/usr/local/bin/arb_primer", "arb_probe": "/usr/local/bin/arb_probe", "arb_proto_2_xsub": "/usr/local/bin/arb_proto_2_xsub", "arb_pt_server": "/usr/local/bin/arb_pt_server", "arb_read_tree": "/usr/local/bin/arb_read_tree", "arb_readseq": "/usr/local/bin/arb_readseq", "arb_replace": "/usr/local/bin/arb_replace", "arb_rnacma": "/usr/local/bin/arb_rnacma", "arb_treegen": "/usr/local/bin/arb_treegen", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arb-bio-tools.
shpc-registry automated BioContainers addition for arb-bio-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arb-bio-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arb-bio-tools:6.0.6--haa8b8d8_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arb-bio-tools/6.0.6--haa8b8d8_8
$ module help quay.io/biocontainers/arb-bio-tools/6.0.6--haa8b8d8_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arb-bio-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arb-bio-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arb-bio-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arb-bio-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arb-bio-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arb-bio-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arb_2_ascii

```bash
$ singularity exec <container> /usr/local/bin/arb_2_ascii
$ podman run --it --rm --entrypoint /usr/local/bin/arb_2_ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_2_ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_2_bin

```bash
$ singularity exec <container> /usr/local/bin/arb_2_bin
$ podman run --it --rm --entrypoint /usr/local/bin/arb_2_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_2_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_a2ps

```bash
$ singularity exec <container> /usr/local/bin/arb_a2ps
$ podman run --it --rm --entrypoint /usr/local/bin/arb_a2ps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_a2ps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_consensus_tree

```bash
$ singularity exec <container> /usr/local/bin/arb_consensus_tree
$ podman run --it --rm --entrypoint /usr/local/bin/arb_consensus_tree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_consensus_tree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_convert_aln

```bash
$ singularity exec <container> /usr/local/bin/arb_convert_aln
$ podman run --it --rm --entrypoint /usr/local/bin/arb_convert_aln   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_convert_aln   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_db_server

```bash
$ singularity exec <container> /usr/local/bin/arb_db_server
$ podman run --it --rm --entrypoint /usr/local/bin/arb_db_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_db_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_dnarates

```bash
$ singularity exec <container> /usr/local/bin/arb_dnarates
$ podman run --it --rm --entrypoint /usr/local/bin/arb_dnarates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_dnarates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_export_rates

```bash
$ singularity exec <container> /usr/local/bin/arb_export_rates
$ podman run --it --rm --entrypoint /usr/local/bin/arb_export_rates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_export_rates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_export_tree

```bash
$ singularity exec <container> /usr/local/bin/arb_export_tree
$ podman run --it --rm --entrypoint /usr/local/bin/arb_export_tree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_export_tree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_flush_mem

```bash
$ singularity exec <container> /usr/local/bin/arb_flush_mem
$ podman run --it --rm --entrypoint /usr/local/bin/arb_flush_mem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_flush_mem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_gene_probe

```bash
$ singularity exec <container> /usr/local/bin/arb_gene_probe
$ podman run --it --rm --entrypoint /usr/local/bin/arb_gene_probe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_gene_probe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_help2xml

```bash
$ singularity exec <container> /usr/local/bin/arb_help2xml
$ podman run --it --rm --entrypoint /usr/local/bin/arb_help2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_help2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_message

```bash
$ singularity exec <container> /usr/local/bin/arb_message
$ podman run --it --rm --entrypoint /usr/local/bin/arb_message   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_message   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_naligner

```bash
$ singularity exec <container> /usr/local/bin/arb_naligner
$ podman run --it --rm --entrypoint /usr/local/bin/arb_naligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_naligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_name_server

```bash
$ singularity exec <container> /usr/local/bin/arb_name_server
$ podman run --it --rm --entrypoint /usr/local/bin/arb_name_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_name_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_notify

```bash
$ singularity exec <container> /usr/local/bin/arb_notify
$ podman run --it --rm --entrypoint /usr/local/bin/arb_notify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_notify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_primer

```bash
$ singularity exec <container> /usr/local/bin/arb_primer
$ podman run --it --rm --entrypoint /usr/local/bin/arb_primer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_primer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_probe

```bash
$ singularity exec <container> /usr/local/bin/arb_probe
$ podman run --it --rm --entrypoint /usr/local/bin/arb_probe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_probe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_proto_2_xsub

```bash
$ singularity exec <container> /usr/local/bin/arb_proto_2_xsub
$ podman run --it --rm --entrypoint /usr/local/bin/arb_proto_2_xsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_proto_2_xsub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_pt_server

```bash
$ singularity exec <container> /usr/local/bin/arb_pt_server
$ podman run --it --rm --entrypoint /usr/local/bin/arb_pt_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_pt_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_read_tree

```bash
$ singularity exec <container> /usr/local/bin/arb_read_tree
$ podman run --it --rm --entrypoint /usr/local/bin/arb_read_tree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_read_tree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_readseq

```bash
$ singularity exec <container> /usr/local/bin/arb_readseq
$ podman run --it --rm --entrypoint /usr/local/bin/arb_readseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_readseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_replace

```bash
$ singularity exec <container> /usr/local/bin/arb_replace
$ podman run --it --rm --entrypoint /usr/local/bin/arb_replace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_replace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_rnacma

```bash
$ singularity exec <container> /usr/local/bin/arb_rnacma
$ podman run --it --rm --entrypoint /usr/local/bin/arb_rnacma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_rnacma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arb_treegen

```bash
$ singularity exec <container> /usr/local/bin/arb_treegen
$ podman run --it --rm --entrypoint /usr/local/bin/arb_treegen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arb_treegen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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