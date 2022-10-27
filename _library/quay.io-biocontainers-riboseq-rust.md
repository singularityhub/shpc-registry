---
layout: container
name:  "quay.io/biocontainers/riboseq-rust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/riboseq-rust/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/riboseq-rust/container.yaml"
updated_at: "2022-10-27 01:16:06.015340"
latest: "1.2--1"
container_url: "https://biocontainers.pro/tools/riboseq-rust"
aliases:
 - "rust_amino"
 - "rust_amino.bak"
 - "rust_codon"
 - "rust_codon.bak"
 - "rust_dipeptide"
 - "rust_dipeptide.bak"
 - "rust_nucleotide"
 - "rust_nucleotide.bak"
 - "rust_plot_transcript"
 - "rust_plot_transcript.bak"
 - "rust_predict_profiles"
 - "rust_predict_profiles.bak"
 - "rust_synergy"
 - "rust_synergy.bak"
 - "rust_tripeptide"
 - "rust_tripeptide.bak"
versions:
 - "1.2--1"
description: "shpc-registry automated BioContainers addition for riboseq-rust"
config: {"url": "https://biocontainers.pro/tools/riboseq-rust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for riboseq-rust", "latest": {"1.2--1": "sha256:3a9e734199068aac1756ce7764f3787a47f3e0a9d46e157621c05013914b98ba"}, "tags": {"1.2--1": "sha256:3a9e734199068aac1756ce7764f3787a47f3e0a9d46e157621c05013914b98ba"}, "docker": "quay.io/biocontainers/riboseq-rust", "aliases": {"rust_amino": "/usr/local/bin/rust_amino", "rust_amino.bak": "/usr/local/bin/rust_amino.bak", "rust_codon": "/usr/local/bin/rust_codon", "rust_codon.bak": "/usr/local/bin/rust_codon.bak", "rust_dipeptide": "/usr/local/bin/rust_dipeptide", "rust_dipeptide.bak": "/usr/local/bin/rust_dipeptide.bak", "rust_nucleotide": "/usr/local/bin/rust_nucleotide", "rust_nucleotide.bak": "/usr/local/bin/rust_nucleotide.bak", "rust_plot_transcript": "/usr/local/bin/rust_plot_transcript", "rust_plot_transcript.bak": "/usr/local/bin/rust_plot_transcript.bak", "rust_predict_profiles": "/usr/local/bin/rust_predict_profiles", "rust_predict_profiles.bak": "/usr/local/bin/rust_predict_profiles.bak", "rust_synergy": "/usr/local/bin/rust_synergy", "rust_synergy.bak": "/usr/local/bin/rust_synergy.bak", "rust_tripeptide": "/usr/local/bin/rust_tripeptide", "rust_tripeptide.bak": "/usr/local/bin/rust_tripeptide.bak"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/riboseq-rust.
shpc-registry automated BioContainers addition for riboseq-rust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/riboseq-rust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/riboseq-rust:1.2--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/riboseq-rust/1.2--1
$ module help quay.io/biocontainers/riboseq-rust/1.2--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### riboseq-rust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### riboseq-rust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### riboseq-rust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### riboseq-rust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### riboseq-rust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### riboseq-rust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rust_amino

```bash
$ singularity exec <container> /usr/local/bin/rust_amino
$ podman run --it --rm --entrypoint /usr/local/bin/rust_amino   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_amino   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_amino.bak

```bash
$ singularity exec <container> /usr/local/bin/rust_amino.bak
$ podman run --it --rm --entrypoint /usr/local/bin/rust_amino.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_amino.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_codon

```bash
$ singularity exec <container> /usr/local/bin/rust_codon
$ podman run --it --rm --entrypoint /usr/local/bin/rust_codon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_codon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_codon.bak

```bash
$ singularity exec <container> /usr/local/bin/rust_codon.bak
$ podman run --it --rm --entrypoint /usr/local/bin/rust_codon.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_codon.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_dipeptide

```bash
$ singularity exec <container> /usr/local/bin/rust_dipeptide
$ podman run --it --rm --entrypoint /usr/local/bin/rust_dipeptide   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_dipeptide   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_dipeptide.bak

```bash
$ singularity exec <container> /usr/local/bin/rust_dipeptide.bak
$ podman run --it --rm --entrypoint /usr/local/bin/rust_dipeptide.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_dipeptide.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_nucleotide

```bash
$ singularity exec <container> /usr/local/bin/rust_nucleotide
$ podman run --it --rm --entrypoint /usr/local/bin/rust_nucleotide   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_nucleotide   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_nucleotide.bak

```bash
$ singularity exec <container> /usr/local/bin/rust_nucleotide.bak
$ podman run --it --rm --entrypoint /usr/local/bin/rust_nucleotide.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_nucleotide.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_plot_transcript

```bash
$ singularity exec <container> /usr/local/bin/rust_plot_transcript
$ podman run --it --rm --entrypoint /usr/local/bin/rust_plot_transcript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_plot_transcript   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_plot_transcript.bak

```bash
$ singularity exec <container> /usr/local/bin/rust_plot_transcript.bak
$ podman run --it --rm --entrypoint /usr/local/bin/rust_plot_transcript.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_plot_transcript.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_predict_profiles

```bash
$ singularity exec <container> /usr/local/bin/rust_predict_profiles
$ podman run --it --rm --entrypoint /usr/local/bin/rust_predict_profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_predict_profiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_predict_profiles.bak

```bash
$ singularity exec <container> /usr/local/bin/rust_predict_profiles.bak
$ podman run --it --rm --entrypoint /usr/local/bin/rust_predict_profiles.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_predict_profiles.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_synergy

```bash
$ singularity exec <container> /usr/local/bin/rust_synergy
$ podman run --it --rm --entrypoint /usr/local/bin/rust_synergy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_synergy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_synergy.bak

```bash
$ singularity exec <container> /usr/local/bin/rust_synergy.bak
$ podman run --it --rm --entrypoint /usr/local/bin/rust_synergy.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_synergy.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_tripeptide

```bash
$ singularity exec <container> /usr/local/bin/rust_tripeptide
$ podman run --it --rm --entrypoint /usr/local/bin/rust_tripeptide   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_tripeptide   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust_tripeptide.bak

```bash
$ singularity exec <container> /usr/local/bin/rust_tripeptide.bak
$ podman run --it --rm --entrypoint /usr/local/bin/rust_tripeptide.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust_tripeptide.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
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