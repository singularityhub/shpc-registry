---
layout: container
name:  "quay.io/biocontainers/vcf2maf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcf2maf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcf2maf/container.yaml"
updated_at: "2025-10-25 03:45:36.967316"
latest: "1.6.22--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/vcf2maf"
aliases:
 - "crc32"
 - "filter_vep.pl"
 - "maf2maf.pl"
 - "maf2vcf.pl"
 - "variant_effect_predictor.pl"
 - "vcf2maf.pl"
 - "vcf2vcf.pl"
 - "vep_convert_cache.pl"
 - "vep_install.pl"
 - "bp_pairwise_kaks.pl"
 - "bp_search2BSML.pl"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "bp_aacomp.pl"
 - "bp_biofetch_genbank_proxy.pl"
 - "bp_bioflat_index.pl"
 - "bp_biogetseq.pl"
 - "bp_blast2tree.pl"
versions:
 - "1.6.8--0"
 - "1.6.21--hdfd78af_0"
 - "1.6.22--hdfd78af_0"
 - "1.6.22--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for vcf2maf"
config: {"url": "https://biocontainers.pro/tools/vcf2maf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vcf2maf", "latest": {"1.6.22--hdfd78af_1": "sha256:e94b55f6674bdd01a19ba0cbed02b2ba972f1f847faefcf46d38a4ab15c745fc"}, "tags": {"1.6.8--0": "sha256:63acbecadc71f2e26a718c28fcb7994df02c92482e41d98fb4a49b5f0e3249f6", "1.6.21--hdfd78af_0": "sha256:e33def318468ac924bdcc280c4aa8984865709d111cd0df9b0d82c7908b7dd07", "1.6.22--hdfd78af_0": "sha256:0b1d0ddc1082012d096067b9323a208fc9696a3e58a83890e2eafbff08dc26f9", "1.6.22--hdfd78af_1": "sha256:e94b55f6674bdd01a19ba0cbed02b2ba972f1f847faefcf46d38a4ab15c745fc"}, "docker": "quay.io/biocontainers/vcf2maf", "aliases": {"crc32": "/usr/local/bin/crc32", "filter_vep.pl": "/usr/local/bin/filter_vep.pl", "maf2maf.pl": "/usr/local/bin/maf2maf.pl", "maf2vcf.pl": "/usr/local/bin/maf2vcf.pl", "variant_effect_predictor.pl": "/usr/local/bin/variant_effect_predictor.pl", "vcf2maf.pl": "/usr/local/bin/vcf2maf.pl", "vcf2vcf.pl": "/usr/local/bin/vcf2vcf.pl", "vep_convert_cache.pl": "/usr/local/bin/vep_convert_cache.pl", "vep_install.pl": "/usr/local/bin/vep_install.pl", "bp_pairwise_kaks.pl": "/usr/local/bin/bp_pairwise_kaks.pl", "bp_search2BSML.pl": "/usr/local/bin/bp_search2BSML.pl", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "bp_aacomp.pl": "/usr/local/bin/bp_aacomp.pl", "bp_biofetch_genbank_proxy.pl": "/usr/local/bin/bp_biofetch_genbank_proxy.pl", "bp_bioflat_index.pl": "/usr/local/bin/bp_bioflat_index.pl", "bp_biogetseq.pl": "/usr/local/bin/bp_biogetseq.pl", "bp_blast2tree.pl": "/usr/local/bin/bp_blast2tree.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcf2maf.
shpc-registry automated BioContainers addition for vcf2maf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcf2maf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcf2maf:1.6.22--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcf2maf/1.6.22--hdfd78af_1
$ module help quay.io/biocontainers/vcf2maf/1.6.22--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcf2maf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcf2maf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcf2maf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcf2maf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcf2maf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcf2maf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crc32

```bash
$ singularity exec <container> /usr/local/bin/crc32
$ podman run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_vep.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_vep.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_vep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_vep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf2maf.pl

```bash
$ singularity exec <container> /usr/local/bin/maf2maf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/maf2maf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf2maf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf2vcf.pl

```bash
$ singularity exec <container> /usr/local/bin/maf2vcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/maf2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### variant_effect_predictor.pl

```bash
$ singularity exec <container> /usr/local/bin/variant_effect_predictor.pl
$ podman run --it --rm --entrypoint /usr/local/bin/variant_effect_predictor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variant_effect_predictor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2maf.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2maf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2maf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2maf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2vcf.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2vcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep_convert_cache.pl

```bash
$ singularity exec <container> /usr/local/bin/vep_convert_cache.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vep_convert_cache.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep_convert_cache.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep_install.pl

```bash
$ singularity exec <container> /usr/local/bin/vep_install.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vep_install.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep_install.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
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