---
layout: container
name:  "quay.io/biocontainers/arcsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arcsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arcsv/container.yaml"
updated_at: "2024-04-11 03:03:42.120770"
latest: "1.0.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/arcsv"
aliases:
 - "ArcSV"
 - "BKinCheck.pl"
 - "BKinCheck_len.pl"
 - "bed2pos"
 - "createClip.sh"
 - "extractBK_bam.sh"
 - "extractSoftclipped"
 - "fastqToBKS.pl"
 - "filter_PopSpec_AF.sh"
 - "find_record.sh"
 - "format_header.txt"
 - "gen_pop_bed.sh"
 - "generateBKSinArc.sh"
 - "generateBKSinArc_each.sh"
 - "generateBKSinBam.pl"
 - "generateBKSinBam.sh"
 - "generateBKSinBam_each.sh"
 - "getSoftclippedAndNearbySeq.py"
 - "getfastq.sh"
 - "pos2bed"
 - "transDeepMEI2BK.sh"
 - "gff2gff.py"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
 - "build_env_setup.sh"
 - "shiftBed"
 - "conda_build.sh"
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
versions:
 - "1.0.2--hdfd78af_0"
description: "singularity registry hpc automated addition for arcsv"
config: {"url": "https://biocontainers.pro/tools/arcsv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for arcsv", "latest": {"1.0.2--hdfd78af_0": "sha256:5d41245ef7eb2687bea9b2e604ee89a9696b9889370b35069a976ea42da15540"}, "tags": {"1.0.2--hdfd78af_0": "sha256:5d41245ef7eb2687bea9b2e604ee89a9696b9889370b35069a976ea42da15540"}, "docker": "quay.io/biocontainers/arcsv", "aliases": {"ArcSV": "/usr/local/bin/ArcSV", "BKinCheck.pl": "/usr/local/bin/BKinCheck.pl", "BKinCheck_len.pl": "/usr/local/bin/BKinCheck_len.pl", "bed2pos": "/usr/local/bin/bed2pos", "createClip.sh": "/usr/local/bin/createClip.sh", "extractBK_bam.sh": "/usr/local/bin/extractBK_bam.sh", "extractSoftclipped": "/usr/local/bin/extractSoftclipped", "fastqToBKS.pl": "/usr/local/bin/fastqToBKS.pl", "filter_PopSpec_AF.sh": "/usr/local/bin/filter_PopSpec_AF.sh", "find_record.sh": "/usr/local/bin/find_record.sh", "format_header.txt": "/usr/local/bin/format_header.txt", "gen_pop_bed.sh": "/usr/local/bin/gen_pop_bed.sh", "generateBKSinArc.sh": "/usr/local/bin/generateBKSinArc.sh", "generateBKSinArc_each.sh": "/usr/local/bin/generateBKSinArc_each.sh", "generateBKSinBam.pl": "/usr/local/bin/generateBKSinBam.pl", "generateBKSinBam.sh": "/usr/local/bin/generateBKSinBam.sh", "generateBKSinBam_each.sh": "/usr/local/bin/generateBKSinBam_each.sh", "getSoftclippedAndNearbySeq.py": "/usr/local/bin/getSoftclippedAndNearbySeq.py", "getfastq.sh": "/usr/local/bin/getfastq.sh", "pos2bed": "/usr/local/bin/pos2bed", "transDeepMEI2BK.sh": "/usr/local/bin/transDeepMEI2BK.sh", "gff2gff.py": "/usr/local/bin/gff2gff.py", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "shiftBed": "/usr/local/bin/shiftBed", "conda_build.sh": "/usr/local/bin/conda_build.sh", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "closestBed": "/usr/local/bin/closestBed", "clusterBed": "/usr/local/bin/clusterBed", "complementBed": "/usr/local/bin/complementBed", "coverageBed": "/usr/local/bin/coverageBed", "expandCols": "/usr/local/bin/expandCols", "fastaFromBed": "/usr/local/bin/fastaFromBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arcsv.
singularity registry hpc automated addition for arcsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arcsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arcsv:1.0.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arcsv/1.0.2--hdfd78af_0
$ module help quay.io/biocontainers/arcsv/1.0.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arcsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arcsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arcsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arcsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arcsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arcsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ArcSV

```bash
$ singularity exec <container> /usr/local/bin/ArcSV
$ podman run --it --rm --entrypoint /usr/local/bin/ArcSV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ArcSV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BKinCheck.pl

```bash
$ singularity exec <container> /usr/local/bin/BKinCheck.pl
$ podman run --it --rm --entrypoint /usr/local/bin/BKinCheck.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BKinCheck.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BKinCheck_len.pl

```bash
$ singularity exec <container> /usr/local/bin/BKinCheck_len.pl
$ podman run --it --rm --entrypoint /usr/local/bin/BKinCheck_len.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BKinCheck_len.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed2pos

```bash
$ singularity exec <container> /usr/local/bin/bed2pos
$ podman run --it --rm --entrypoint /usr/local/bin/bed2pos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2pos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createClip.sh

```bash
$ singularity exec <container> /usr/local/bin/createClip.sh
$ podman run --it --rm --entrypoint /usr/local/bin/createClip.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createClip.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractBK_bam.sh

```bash
$ singularity exec <container> /usr/local/bin/extractBK_bam.sh
$ podman run --it --rm --entrypoint /usr/local/bin/extractBK_bam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractBK_bam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractSoftclipped

```bash
$ singularity exec <container> /usr/local/bin/extractSoftclipped
$ podman run --it --rm --entrypoint /usr/local/bin/extractSoftclipped   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractSoftclipped   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqToBKS.pl

```bash
$ singularity exec <container> /usr/local/bin/fastqToBKS.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fastqToBKS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqToBKS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_PopSpec_AF.sh

```bash
$ singularity exec <container> /usr/local/bin/filter_PopSpec_AF.sh
$ podman run --it --rm --entrypoint /usr/local/bin/filter_PopSpec_AF.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_PopSpec_AF.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_record.sh

```bash
$ singularity exec <container> /usr/local/bin/find_record.sh
$ podman run --it --rm --entrypoint /usr/local/bin/find_record.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_record.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### format_header.txt

```bash
$ singularity exec <container> /usr/local/bin/format_header.txt
$ podman run --it --rm --entrypoint /usr/local/bin/format_header.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/format_header.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gen_pop_bed.sh

```bash
$ singularity exec <container> /usr/local/bin/gen_pop_bed.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gen_pop_bed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gen_pop_bed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generateBKSinArc.sh

```bash
$ singularity exec <container> /usr/local/bin/generateBKSinArc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/generateBKSinArc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generateBKSinArc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generateBKSinArc_each.sh

```bash
$ singularity exec <container> /usr/local/bin/generateBKSinArc_each.sh
$ podman run --it --rm --entrypoint /usr/local/bin/generateBKSinArc_each.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generateBKSinArc_each.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generateBKSinBam.pl

```bash
$ singularity exec <container> /usr/local/bin/generateBKSinBam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/generateBKSinBam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generateBKSinBam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generateBKSinBam.sh

```bash
$ singularity exec <container> /usr/local/bin/generateBKSinBam.sh
$ podman run --it --rm --entrypoint /usr/local/bin/generateBKSinBam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generateBKSinBam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generateBKSinBam_each.sh

```bash
$ singularity exec <container> /usr/local/bin/generateBKSinBam_each.sh
$ podman run --it --rm --entrypoint /usr/local/bin/generateBKSinBam_each.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generateBKSinBam_each.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getSoftclippedAndNearbySeq.py

```bash
$ singularity exec <container> /usr/local/bin/getSoftclippedAndNearbySeq.py
$ podman run --it --rm --entrypoint /usr/local/bin/getSoftclippedAndNearbySeq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getSoftclippedAndNearbySeq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfastq.sh

```bash
$ singularity exec <container> /usr/local/bin/getfastq.sh
$ podman run --it --rm --entrypoint /usr/local/bin/getfastq.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfastq.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pos2bed

```bash
$ singularity exec <container> /usr/local/bin/pos2bed
$ podman run --it --rm --entrypoint /usr/local/bin/pos2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pos2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transDeepMEI2BK.sh

```bash
$ singularity exec <container> /usr/local/bin/transDeepMEI2BK.sh
$ podman run --it --rm --entrypoint /usr/local/bin/transDeepMEI2BK.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transDeepMEI2BK.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_env_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/build_env_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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