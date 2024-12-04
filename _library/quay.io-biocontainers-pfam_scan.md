---
layout: container
name:  "quay.io/biocontainers/pfam_scan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pfam_scan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pfam_scan/container.yaml"
updated_at: "2024-12-04 03:27:36.380264"
latest: "1.6--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/pfam_scan"
aliases:
 - "pfam_scan.pl"
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
 - "1.6--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for pfam_scan"
config: {"url": "https://biocontainers.pro/tools/pfam_scan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pfam_scan", "latest": {"1.6--hdfd78af_4": "sha256:ff78ea49eb3192839c04f865891cff54e1fe7f3a3f19f28eaf28505ba6bade7d"}, "tags": {"1.6--hdfd78af_4": "sha256:ff78ea49eb3192839c04f865891cff54e1fe7f3a3f19f28eaf28505ba6bade7d"}, "docker": "quay.io/biocontainers/pfam_scan", "aliases": {"pfam_scan.pl": "/usr/local/bin/pfam_scan.pl", "bp_pairwise_kaks.pl": "/usr/local/bin/bp_pairwise_kaks.pl", "bp_search2BSML.pl": "/usr/local/bin/bp_search2BSML.pl", "bp_aacomp.pl": "/usr/local/bin/bp_aacomp.pl", "bp_biofetch_genbank_proxy.pl": "/usr/local/bin/bp_biofetch_genbank_proxy.pl", "bp_bioflat_index.pl": "/usr/local/bin/bp_bioflat_index.pl", "bp_biogetseq.pl": "/usr/local/bin/bp_biogetseq.pl", "bp_blast2tree.pl": "/usr/local/bin/bp_blast2tree.pl", "bp_bulk_load_gff.pl": "/usr/local/bin/bp_bulk_load_gff.pl", "bp_chaos_plot.pl": "/usr/local/bin/bp_chaos_plot.pl", "bp_classify_hits_kingdom.pl": "/usr/local/bin/bp_classify_hits_kingdom.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pfam_scan.
shpc-registry automated BioContainers addition for pfam_scan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pfam_scan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pfam_scan:1.6--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pfam_scan/1.6--hdfd78af_4
$ module help quay.io/biocontainers/pfam_scan/1.6--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pfam_scan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pfam_scan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pfam_scan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pfam_scan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pfam_scan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pfam_scan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pfam_scan.pl

```bash
$ singularity exec <container> /usr/local/bin/pfam_scan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pfam_scan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfam_scan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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