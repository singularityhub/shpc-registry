---
layout: container
name:  "quay.io/biocontainers/rainbow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rainbow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rainbow/container.yaml"
updated_at: "2025-12-31 03:40:22.107594"
latest: "2.0.4--pl5321h7b50bb2_11"
container_url: "https://biocontainers.pro/tools/rainbow"
aliases:
 - "rainbow"
 - "select_all_rbcontig.pl"
 - "select_all_rbcontig.pl.bak"
 - "select_best_rbcontig.pl"
 - "select_best_rbcontig.pl.bak"
 - "select_best_rbcontig_plus_read1.pl"
 - "select_best_rbcontig_plus_read1.pl.bak"
 - "select_sec_rbcontig.pl"
 - "select_sec_rbcontig.pl.bak"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.0.4--hec16e2b_7"
 - "2.0.4--hec16e2b_8"
 - "2.0.4--h031d066_9"
 - "2.0.4--h7b50bb2_10"
 - "2.0.4--pl5321h7b50bb2_11"
description: "shpc-registry automated BioContainers addition for rainbow"
config: {"url": "https://biocontainers.pro/tools/rainbow", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rainbow", "latest": {"2.0.4--pl5321h7b50bb2_11": "sha256:3b4fafbbf81ffb8499f64968ef69b591a81b4a59f94bc7d441b70e1771195e1f"}, "tags": {"2.0.4--hec16e2b_7": "sha256:66f491eaf1d8e5ce24a464416e9a66f02906153f34ca07073384ef24b32af1ee", "2.0.4--hec16e2b_8": "sha256:0bd2804b17910687a7fddd43e23edf4191de4705e3b56fd5a5c4098945da3359", "2.0.4--h031d066_9": "sha256:bff87c7c17b5d87a0b33858c7136b595a45a1477f49e4069a7ce4d9dde28d7c9", "2.0.4--h7b50bb2_10": "sha256:c0ae2b78768d1c222a1235dd8c08bcf942fdd2d692ff6d85d90a1de4a88ff817", "2.0.4--pl5321h7b50bb2_11": "sha256:3b4fafbbf81ffb8499f64968ef69b591a81b4a59f94bc7d441b70e1771195e1f"}, "docker": "quay.io/biocontainers/rainbow", "aliases": {"rainbow": "/usr/local/bin/rainbow", "select_all_rbcontig.pl": "/usr/local/bin/select_all_rbcontig.pl", "select_all_rbcontig.pl.bak": "/usr/local/bin/select_all_rbcontig.pl.bak", "select_best_rbcontig.pl": "/usr/local/bin/select_best_rbcontig.pl", "select_best_rbcontig.pl.bak": "/usr/local/bin/select_best_rbcontig.pl.bak", "select_best_rbcontig_plus_read1.pl": "/usr/local/bin/select_best_rbcontig_plus_read1.pl", "select_best_rbcontig_plus_read1.pl.bak": "/usr/local/bin/select_best_rbcontig_plus_read1.pl.bak", "select_sec_rbcontig.pl": "/usr/local/bin/select_sec_rbcontig.pl", "select_sec_rbcontig.pl.bak": "/usr/local/bin/select_sec_rbcontig.pl.bak", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rainbow.
shpc-registry automated BioContainers addition for rainbow
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rainbow
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rainbow:2.0.4--pl5321h7b50bb2_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rainbow/2.0.4--pl5321h7b50bb2_11
$ module help quay.io/biocontainers/rainbow/2.0.4--pl5321h7b50bb2_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rainbow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rainbow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rainbow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rainbow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rainbow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rainbow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rainbow

```bash
$ singularity exec <container> /usr/local/bin/rainbow
$ podman run --it --rm --entrypoint /usr/local/bin/rainbow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rainbow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_all_rbcontig.pl

```bash
$ singularity exec <container> /usr/local/bin/select_all_rbcontig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/select_all_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_all_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_all_rbcontig.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/select_all_rbcontig.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/select_all_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_all_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_best_rbcontig.pl

```bash
$ singularity exec <container> /usr/local/bin/select_best_rbcontig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_best_rbcontig.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/select_best_rbcontig.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_best_rbcontig_plus_read1.pl

```bash
$ singularity exec <container> /usr/local/bin/select_best_rbcontig_plus_read1.pl
$ podman run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig_plus_read1.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig_plus_read1.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_best_rbcontig_plus_read1.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/select_best_rbcontig_plus_read1.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig_plus_read1.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig_plus_read1.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_sec_rbcontig.pl

```bash
$ singularity exec <container> /usr/local/bin/select_sec_rbcontig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/select_sec_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_sec_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_sec_rbcontig.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/select_sec_rbcontig.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/select_sec_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_sec_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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