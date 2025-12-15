---
layout: container
name:  "quay.io/biocontainers/strvctvre"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strvctvre/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strvctvre/container.yaml"
updated_at: "2025-12-15 04:28:22.576599"
latest: "1.10--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/strvctvre"
aliases:
 - "StrVCTVRE.py"
 - "StrVCTVRE.py.bak"
 - "annotationFinalForStrVCTVRE.py"
 - "annotationFinalForStrVCTVRE.py.bak"
 - "liftover_hg19_to_hg38_public.py"
 - "liftover_hg19_to_hg38_public.py.bak"
 - "test_StrVCTVRE.py"
 - "test_StrVCTVRE.py.bak"
 - "test_StrVCTVRE_GRCh37.py"
 - "test_StrVCTVRE_GRCh37.py.bak"
 - "ref-cache"
 - "cyvcf2"
 - "coloredlogs"
 - "annot-tsv"
 - "humanfriendly"
 - "numpy-config"
 - "shiftBed"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
 - "closestBed"
 - "clusterBed"
 - "complementBed"
 - "coverageBed"
 - "expandCols"
 - "fastaFromBed"
 - "flankBed"
 - "genomeCoverageBed"
 - "getOverlap"
 - "groupBy"
versions:
 - "1.10--pyh7e72e81_0"
description: "singularity registry hpc automated addition for strvctvre"
config: {"url": "https://biocontainers.pro/tools/strvctvre", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for strvctvre", "latest": {"1.10--pyh7e72e81_0": "sha256:1bed1537e076c5099752e1e5cb1996bdb808ee18f23f815a1ee6d9e285dc4ff4"}, "tags": {"1.10--pyh7e72e81_0": "sha256:1bed1537e076c5099752e1e5cb1996bdb808ee18f23f815a1ee6d9e285dc4ff4"}, "docker": "quay.io/biocontainers/strvctvre", "aliases": {"StrVCTVRE.py": "/usr/local/bin/StrVCTVRE.py", "StrVCTVRE.py.bak": "/usr/local/bin/StrVCTVRE.py.bak", "annotationFinalForStrVCTVRE.py": "/usr/local/bin/annotationFinalForStrVCTVRE.py", "annotationFinalForStrVCTVRE.py.bak": "/usr/local/bin/annotationFinalForStrVCTVRE.py.bak", "liftover_hg19_to_hg38_public.py": "/usr/local/bin/liftover_hg19_to_hg38_public.py", "liftover_hg19_to_hg38_public.py.bak": "/usr/local/bin/liftover_hg19_to_hg38_public.py.bak", "test_StrVCTVRE.py": "/usr/local/bin/test_StrVCTVRE.py", "test_StrVCTVRE.py.bak": "/usr/local/bin/test_StrVCTVRE.py.bak", "test_StrVCTVRE_GRCh37.py": "/usr/local/bin/test_StrVCTVRE_GRCh37.py", "test_StrVCTVRE_GRCh37.py.bak": "/usr/local/bin/test_StrVCTVRE_GRCh37.py.bak", "ref-cache": "/usr/local/bin/ref-cache", "cyvcf2": "/usr/local/bin/cyvcf2", "coloredlogs": "/usr/local/bin/coloredlogs", "annot-tsv": "/usr/local/bin/annot-tsv", "humanfriendly": "/usr/local/bin/humanfriendly", "numpy-config": "/usr/local/bin/numpy-config", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "closestBed": "/usr/local/bin/closestBed", "clusterBed": "/usr/local/bin/clusterBed", "complementBed": "/usr/local/bin/complementBed", "coverageBed": "/usr/local/bin/coverageBed", "expandCols": "/usr/local/bin/expandCols", "fastaFromBed": "/usr/local/bin/fastaFromBed", "flankBed": "/usr/local/bin/flankBed", "genomeCoverageBed": "/usr/local/bin/genomeCoverageBed", "getOverlap": "/usr/local/bin/getOverlap", "groupBy": "/usr/local/bin/groupBy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strvctvre.
singularity registry hpc automated addition for strvctvre
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strvctvre
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strvctvre:1.10--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strvctvre/1.10--pyh7e72e81_0
$ module help quay.io/biocontainers/strvctvre/1.10--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strvctvre-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strvctvre-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strvctvre-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strvctvre-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strvctvre-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strvctvre-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### StrVCTVRE.py

```bash
$ singularity exec <container> /usr/local/bin/StrVCTVRE.py
$ podman run --it --rm --entrypoint /usr/local/bin/StrVCTVRE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StrVCTVRE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StrVCTVRE.py.bak

```bash
$ singularity exec <container> /usr/local/bin/StrVCTVRE.py.bak
$ podman run --it --rm --entrypoint /usr/local/bin/StrVCTVRE.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StrVCTVRE.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotationFinalForStrVCTVRE.py

```bash
$ singularity exec <container> /usr/local/bin/annotationFinalForStrVCTVRE.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotationFinalForStrVCTVRE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotationFinalForStrVCTVRE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotationFinalForStrVCTVRE.py.bak

```bash
$ singularity exec <container> /usr/local/bin/annotationFinalForStrVCTVRE.py.bak
$ podman run --it --rm --entrypoint /usr/local/bin/annotationFinalForStrVCTVRE.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotationFinalForStrVCTVRE.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### liftover_hg19_to_hg38_public.py

```bash
$ singularity exec <container> /usr/local/bin/liftover_hg19_to_hg38_public.py
$ podman run --it --rm --entrypoint /usr/local/bin/liftover_hg19_to_hg38_public.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/liftover_hg19_to_hg38_public.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### liftover_hg19_to_hg38_public.py.bak

```bash
$ singularity exec <container> /usr/local/bin/liftover_hg19_to_hg38_public.py.bak
$ podman run --it --rm --entrypoint /usr/local/bin/liftover_hg19_to_hg38_public.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/liftover_hg19_to_hg38_public.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_StrVCTVRE.py

```bash
$ singularity exec <container> /usr/local/bin/test_StrVCTVRE.py
$ podman run --it --rm --entrypoint /usr/local/bin/test_StrVCTVRE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_StrVCTVRE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_StrVCTVRE.py.bak

```bash
$ singularity exec <container> /usr/local/bin/test_StrVCTVRE.py.bak
$ podman run --it --rm --entrypoint /usr/local/bin/test_StrVCTVRE.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_StrVCTVRE.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_StrVCTVRE_GRCh37.py

```bash
$ singularity exec <container> /usr/local/bin/test_StrVCTVRE_GRCh37.py
$ podman run --it --rm --entrypoint /usr/local/bin/test_StrVCTVRE_GRCh37.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_StrVCTVRE_GRCh37.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_StrVCTVRE_GRCh37.py.bak

```bash
$ singularity exec <container> /usr/local/bin/test_StrVCTVRE_GRCh37.py.bak
$ podman run --it --rm --entrypoint /usr/local/bin/test_StrVCTVRE_GRCh37.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_StrVCTVRE_GRCh37.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### closestBed

```bash
$ singularity exec <container> /usr/local/bin/closestBed
$ podman run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterBed

```bash
$ singularity exec <container> /usr/local/bin/clusterBed
$ podman run --it --rm --entrypoint /usr/local/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complementBed

```bash
$ singularity exec <container> /usr/local/bin/complementBed
$ podman run --it --rm --entrypoint /usr/local/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverageBed

```bash
$ singularity exec <container> /usr/local/bin/coverageBed
$ podman run --it --rm --entrypoint /usr/local/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### expandCols

```bash
$ singularity exec <container> /usr/local/bin/expandCols
$ podman run --it --rm --entrypoint /usr/local/bin/expandCols   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/expandCols   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaFromBed

```bash
$ singularity exec <container> /usr/local/bin/fastaFromBed
$ podman run --it --rm --entrypoint /usr/local/bin/fastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flankBed

```bash
$ singularity exec <container> /usr/local/bin/flankBed
$ podman run --it --rm --entrypoint /usr/local/bin/flankBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flankBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomeCoverageBed

```bash
$ singularity exec <container> /usr/local/bin/genomeCoverageBed
$ podman run --it --rm --entrypoint /usr/local/bin/genomeCoverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomeCoverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getOverlap

```bash
$ singularity exec <container> /usr/local/bin/getOverlap
$ podman run --it --rm --entrypoint /usr/local/bin/getOverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getOverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groupBy

```bash
$ singularity exec <container> /usr/local/bin/groupBy
$ podman run --it --rm --entrypoint /usr/local/bin/groupBy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groupBy   -v ${PWD} -w ${PWD} <container> -c " $@"
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