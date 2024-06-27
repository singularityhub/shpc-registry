---
layout: container
name:  "quay.io/biocontainers/mlst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mlst/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mlst/container.yaml"
updated_at: "2024-06-27 02:47:15.694338"
latest: "2.23.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/mlst"
aliases:
 - "mlst"
 - "bp_pairwise_kaks.pl"
 - "bp_search2BSML.pl"
 - "bp_aacomp.pl"
 - "bp_biofetch_genbank_proxy.pl"
 - "bp_bioflat_index.pl"
 - "bp_biogetseq.pl"
 - "bp_blast2tree.pl"
 - "bp_bulk_load_gff.pl"
 - "bp_chaos_plot.pl"
 - "bp_classify_hits_kingdom.pl"
versions:
 - "2.9--hec16e2b_4"
 - "2.23.0--hdfd78af_0"
 - "2.22.1--hdfd78af_0"
 - "2.19.0--hdfd78af_1"
 - "2.18.1--0"
 - "2.17.6--1"
 - "2.23.0--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for mlst"
config: {"url": "https://biocontainers.pro/tools/mlst", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mlst", "latest": {"2.23.0--hdfd78af_1": "sha256:5e32de82da1ab6df5ded7b6852178af0b86fa42f0e9c6305ad8cf1b28dd7c08d"}, "tags": {"2.9--hec16e2b_4": "sha256:be2e48b3a98515ac8807941984271e7d90ef686c7188c6f1f481d8efe443b20b", "2.23.0--hdfd78af_0": "sha256:ce4b51e4d41b84a5909010e798b33f3debbc79e6d58063ff1e703c290d5b2bc8", "2.22.1--hdfd78af_0": "sha256:b17bdd43b6835927c4e4e918e757c1cc96f025155b4c130ef2064e27458c4485", "2.19.0--hdfd78af_1": "sha256:b68ba8d74b3de3031c62645e09598e1bde1d0b502478a63cc166a2af03079bd9", "2.18.1--0": "sha256:03a889974e65ea5dd74211e0aa4e1540fdb23154e44a8104de257d42e2e2c794", "2.17.6--1": "sha256:9418ef8a3f591441ed8bec0a2c45ed80c06b969a878980917386613f4218366f", "2.23.0--hdfd78af_1": "sha256:5e32de82da1ab6df5ded7b6852178af0b86fa42f0e9c6305ad8cf1b28dd7c08d"}, "docker": "quay.io/biocontainers/mlst", "aliases": {"mlst": "/usr/local/bin/mlst", "bp_pairwise_kaks.pl": "/usr/local/bin/bp_pairwise_kaks.pl", "bp_search2BSML.pl": "/usr/local/bin/bp_search2BSML.pl", "bp_aacomp.pl": "/usr/local/bin/bp_aacomp.pl", "bp_biofetch_genbank_proxy.pl": "/usr/local/bin/bp_biofetch_genbank_proxy.pl", "bp_bioflat_index.pl": "/usr/local/bin/bp_bioflat_index.pl", "bp_biogetseq.pl": "/usr/local/bin/bp_biogetseq.pl", "bp_blast2tree.pl": "/usr/local/bin/bp_blast2tree.pl", "bp_bulk_load_gff.pl": "/usr/local/bin/bp_bulk_load_gff.pl", "bp_chaos_plot.pl": "/usr/local/bin/bp_chaos_plot.pl", "bp_classify_hits_kingdom.pl": "/usr/local/bin/bp_classify_hits_kingdom.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mlst.
shpc-registry automated BioContainers addition for mlst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mlst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mlst:2.23.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mlst/2.23.0--hdfd78af_1
$ module help quay.io/biocontainers/mlst/2.23.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mlst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mlst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mlst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mlst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mlst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mlst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mlst

```bash
$ singularity exec <container> /usr/local/bin/mlst
$ podman run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_search2BSML.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_search2BSML.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_aacomp.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_aacomp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_aacomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_aacomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biofetch_genbank_proxy.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_biofetch_genbank_proxy.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biofetch_genbank_proxy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biofetch_genbank_proxy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bioflat_index.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_bioflat_index.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biogetseq.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_biogetseq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biogetseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biogetseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_blast2tree.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_blast2tree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_blast2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_blast2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bulk_load_gff.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_bulk_load_gff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bulk_load_gff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bulk_load_gff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_chaos_plot.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_chaos_plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_chaos_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_chaos_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_classify_hits_kingdom.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_classify_hits_kingdom.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_classify_hits_kingdom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_classify_hits_kingdom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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