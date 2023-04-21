---
layout: container
name:  "quay.io/biocontainers/protgraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/protgraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/protgraph/container.yaml"
updated_at: "2023-04-21 02:51:24.195286"
latest: "0.3.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/protgraph"
aliases:
 - "geomet"
 - "protgraph"
 - "protgraph_compact_fasta"
 - "protgraph_generate_fasta_decoys"
 - "protgraph_pepsqlite_to_fasta"
 - "protgraph_print_sums"
 - "protgraph_replace_fasta_header"
 - "igraph"
 - "cmpfillin"
 - "gpmetis"
 - "graphchk"
 - "m2gmetis"
 - "mpmetis"
 - "ndmetis"
 - "glpsol"
 - "protoc"
 - "normalizer"
versions:
 - "0.3.4--pyhdfd78af_0"
 - "0.3.8--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for protgraph"
config: {"url": "https://biocontainers.pro/tools/protgraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for protgraph", "latest": {"0.3.8--pyhdfd78af_0": "sha256:0854c9a39a18474bb568abe9c4625c90f5a0490cf5c5e4300c3854d4774bf3c8"}, "tags": {"0.3.4--pyhdfd78af_0": "sha256:85a8697b47b0c2b3a3b2f6507586f6f55c35801c3c79ddf42fa944d5fd311f8d", "0.3.8--pyhdfd78af_0": "sha256:0854c9a39a18474bb568abe9c4625c90f5a0490cf5c5e4300c3854d4774bf3c8"}, "docker": "quay.io/biocontainers/protgraph", "aliases": {"geomet": "/usr/local/bin/geomet", "protgraph": "/usr/local/bin/protgraph", "protgraph_compact_fasta": "/usr/local/bin/protgraph_compact_fasta", "protgraph_generate_fasta_decoys": "/usr/local/bin/protgraph_generate_fasta_decoys", "protgraph_pepsqlite_to_fasta": "/usr/local/bin/protgraph_pepsqlite_to_fasta", "protgraph_print_sums": "/usr/local/bin/protgraph_print_sums", "protgraph_replace_fasta_header": "/usr/local/bin/protgraph_replace_fasta_header", "igraph": "/usr/local/bin/igraph", "cmpfillin": "/usr/local/bin/cmpfillin", "gpmetis": "/usr/local/bin/gpmetis", "graphchk": "/usr/local/bin/graphchk", "m2gmetis": "/usr/local/bin/m2gmetis", "mpmetis": "/usr/local/bin/mpmetis", "ndmetis": "/usr/local/bin/ndmetis", "glpsol": "/usr/local/bin/glpsol", "protoc": "/usr/local/bin/protoc", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/protgraph.
shpc-registry automated BioContainers addition for protgraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/protgraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/protgraph:0.3.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/protgraph/0.3.8--pyhdfd78af_0
$ module help quay.io/biocontainers/protgraph/0.3.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### protgraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### protgraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### protgraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### protgraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### protgraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### protgraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geomet

```bash
$ singularity exec <container> /usr/local/bin/geomet
$ podman run --it --rm --entrypoint /usr/local/bin/geomet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geomet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protgraph

```bash
$ singularity exec <container> /usr/local/bin/protgraph
$ podman run --it --rm --entrypoint /usr/local/bin/protgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protgraph_compact_fasta

```bash
$ singularity exec <container> /usr/local/bin/protgraph_compact_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/protgraph_compact_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protgraph_compact_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protgraph_generate_fasta_decoys

```bash
$ singularity exec <container> /usr/local/bin/protgraph_generate_fasta_decoys
$ podman run --it --rm --entrypoint /usr/local/bin/protgraph_generate_fasta_decoys   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protgraph_generate_fasta_decoys   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protgraph_pepsqlite_to_fasta

```bash
$ singularity exec <container> /usr/local/bin/protgraph_pepsqlite_to_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/protgraph_pepsqlite_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protgraph_pepsqlite_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protgraph_print_sums

```bash
$ singularity exec <container> /usr/local/bin/protgraph_print_sums
$ podman run --it --rm --entrypoint /usr/local/bin/protgraph_print_sums   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protgraph_print_sums   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protgraph_replace_fasta_header

```bash
$ singularity exec <container> /usr/local/bin/protgraph_replace_fasta_header
$ podman run --it --rm --entrypoint /usr/local/bin/protgraph_replace_fasta_header   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protgraph_replace_fasta_header   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igraph

```bash
$ singularity exec <container> /usr/local/bin/igraph
$ podman run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpfillin

```bash
$ singularity exec <container> /usr/local/bin/cmpfillin
$ podman run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpmetis

```bash
$ singularity exec <container> /usr/local/bin/gpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphchk

```bash
$ singularity exec <container> /usr/local/bin/graphchk
$ podman run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m2gmetis

```bash
$ singularity exec <container> /usr/local/bin/m2gmetis
$ podman run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpmetis

```bash
$ singularity exec <container> /usr/local/bin/mpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ndmetis

```bash
$ singularity exec <container> /usr/local/bin/ndmetis
$ podman run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc

```bash
$ singularity exec <container> /usr/local/bin/protoc
$ podman run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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