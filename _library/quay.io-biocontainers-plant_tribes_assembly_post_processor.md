---
layout: container
name:  "quay.io/biocontainers/plant_tribes_assembly_post_processor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plant_tribes_assembly_post_processor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plant_tribes_assembly_post_processor/container.yaml"
updated_at: "2025-04-23 03:51:21.855616"
latest: "1.0.4--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/plant_tribes_assembly_post_processor"
aliases:
 - "AssemblyPostProcessor"
 - "ESTScan"
 - "TransDecoder.LongOrfs"
 - "TransDecoder.Predict"
 - "cap3"
 - "cdna_alignment_orf_to_genome_orf.pl"
 - "compute_base_probs.pl"
 - "exclude_similar_proteins.pl"
 - "fasta_prot_checker.pl"
 - "fetch"
 - "ffindex_resume.pl"
 - "formcon"
 - "gene_list_to_gff.pl"
 - "genometools-config"
 - "get_FL_accs.pl"
 - "get_longest_ORF_per_transcript.pl"
 - "get_top_longest_fasta_entries.pl"
 - "gff3_file_to_bed.pl"
 - "gff3_file_to_proteins.pl"
 - "gff3_gene_to_gtf_format.pl"
 - "gt"
 - "gtf_genome_to_cdna_fasta.pl"
 - "gtf_to_alignment_gff3.pl"
 - "gtf_to_bed.pl"
 - "indexer"
 - "netfetch"
 - "nr_ORFs_gff3.pl"
 - "pfam_runner.pl"
 - "refine_gff3_group_iso_strip_utrs.pl"
 - "refine_hexamer_scores.pl"
 - "remove_eclipsed_ORFs.pl"
 - "score_CDS_likelihood_all_6_frames.pl"
 - "select_best_ORFs_per_transcript.pl"
 - "seq_n_baseprobs_to_loglikelihood_vals.pl"
 - "start_codon_refinement.pl"
 - "train_start_PWM.pl"
 - "uri_unescape.pl"
 - "readal"
 - "statal"
 - "trimal"
 - "db_convert"
 - "mafft-sparsecore.rb"
 - "einsi"
 - "fftns"
 - "fftnsi"
 - "ginsi"
 - "linsi"
versions:
 - "1.0.4--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for plant_tribes_assembly_post_processor"
config: {"url": "https://biocontainers.pro/tools/plant_tribes_assembly_post_processor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plant_tribes_assembly_post_processor", "latest": {"1.0.4--h9ee0642_1": "sha256:af37ba04e0a7a258c8473b35a5bf3fafe3b7f9d464a8c4a089a192b373fa7d07"}, "tags": {"1.0.4--h9ee0642_1": "sha256:af37ba04e0a7a258c8473b35a5bf3fafe3b7f9d464a8c4a089a192b373fa7d07"}, "docker": "quay.io/biocontainers/plant_tribes_assembly_post_processor", "aliases": {"AssemblyPostProcessor": "/usr/local/bin/AssemblyPostProcessor", "ESTScan": "/usr/local/bin/ESTScan", "TransDecoder.LongOrfs": "/usr/local/bin/TransDecoder.LongOrfs", "TransDecoder.Predict": "/usr/local/bin/TransDecoder.Predict", "cap3": "/usr/local/bin/cap3", "cdna_alignment_orf_to_genome_orf.pl": "/usr/local/bin/cdna_alignment_orf_to_genome_orf.pl", "compute_base_probs.pl": "/usr/local/bin/compute_base_probs.pl", "exclude_similar_proteins.pl": "/usr/local/bin/exclude_similar_proteins.pl", "fasta_prot_checker.pl": "/usr/local/bin/fasta_prot_checker.pl", "fetch": "/usr/local/bin/fetch", "ffindex_resume.pl": "/usr/local/bin/ffindex_resume.pl", "formcon": "/usr/local/bin/formcon", "gene_list_to_gff.pl": "/usr/local/bin/gene_list_to_gff.pl", "genometools-config": "/usr/local/bin/genometools-config", "get_FL_accs.pl": "/usr/local/bin/get_FL_accs.pl", "get_longest_ORF_per_transcript.pl": "/usr/local/bin/get_longest_ORF_per_transcript.pl", "get_top_longest_fasta_entries.pl": "/usr/local/bin/get_top_longest_fasta_entries.pl", "gff3_file_to_bed.pl": "/usr/local/bin/gff3_file_to_bed.pl", "gff3_file_to_proteins.pl": "/usr/local/bin/gff3_file_to_proteins.pl", "gff3_gene_to_gtf_format.pl": "/usr/local/bin/gff3_gene_to_gtf_format.pl", "gt": "/usr/local/bin/gt", "gtf_genome_to_cdna_fasta.pl": "/usr/local/bin/gtf_genome_to_cdna_fasta.pl", "gtf_to_alignment_gff3.pl": "/usr/local/bin/gtf_to_alignment_gff3.pl", "gtf_to_bed.pl": "/usr/local/bin/gtf_to_bed.pl", "indexer": "/usr/local/bin/indexer", "netfetch": "/usr/local/bin/netfetch", "nr_ORFs_gff3.pl": "/usr/local/bin/nr_ORFs_gff3.pl", "pfam_runner.pl": "/usr/local/bin/pfam_runner.pl", "refine_gff3_group_iso_strip_utrs.pl": "/usr/local/bin/refine_gff3_group_iso_strip_utrs.pl", "refine_hexamer_scores.pl": "/usr/local/bin/refine_hexamer_scores.pl", "remove_eclipsed_ORFs.pl": "/usr/local/bin/remove_eclipsed_ORFs.pl", "score_CDS_likelihood_all_6_frames.pl": "/usr/local/bin/score_CDS_likelihood_all_6_frames.pl", "select_best_ORFs_per_transcript.pl": "/usr/local/bin/select_best_ORFs_per_transcript.pl", "seq_n_baseprobs_to_loglikelihood_vals.pl": "/usr/local/bin/seq_n_baseprobs_to_loglikelihood_vals.pl", "start_codon_refinement.pl": "/usr/local/bin/start_codon_refinement.pl", "train_start_PWM.pl": "/usr/local/bin/train_start_PWM.pl", "uri_unescape.pl": "/usr/local/bin/uri_unescape.pl", "readal": "/usr/local/bin/readal", "statal": "/usr/local/bin/statal", "trimal": "/usr/local/bin/trimal", "db_convert": "/usr/local/bin/db_convert", "mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns", "fftnsi": "/usr/local/bin/fftnsi", "ginsi": "/usr/local/bin/ginsi", "linsi": "/usr/local/bin/linsi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plant_tribes_assembly_post_processor.
shpc-registry automated BioContainers addition for plant_tribes_assembly_post_processor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plant_tribes_assembly_post_processor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plant_tribes_assembly_post_processor:1.0.4--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plant_tribes_assembly_post_processor/1.0.4--h9ee0642_1
$ module help quay.io/biocontainers/plant_tribes_assembly_post_processor/1.0.4--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plant_tribes_assembly_post_processor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plant_tribes_assembly_post_processor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plant_tribes_assembly_post_processor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plant_tribes_assembly_post_processor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plant_tribes_assembly_post_processor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plant_tribes_assembly_post_processor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AssemblyPostProcessor

```bash
$ singularity exec <container> /usr/local/bin/AssemblyPostProcessor
$ podman run --it --rm --entrypoint /usr/local/bin/AssemblyPostProcessor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AssemblyPostProcessor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESTScan

```bash
$ singularity exec <container> /usr/local/bin/ESTScan
$ podman run --it --rm --entrypoint /usr/local/bin/ESTScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESTScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TransDecoder.LongOrfs

```bash
$ singularity exec <container> /usr/local/bin/TransDecoder.LongOrfs
$ podman run --it --rm --entrypoint /usr/local/bin/TransDecoder.LongOrfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TransDecoder.LongOrfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TransDecoder.Predict

```bash
$ singularity exec <container> /usr/local/bin/TransDecoder.Predict
$ podman run --it --rm --entrypoint /usr/local/bin/TransDecoder.Predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TransDecoder.Predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cap3

```bash
$ singularity exec <container> /usr/local/bin/cap3
$ podman run --it --rm --entrypoint /usr/local/bin/cap3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cap3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdna_alignment_orf_to_genome_orf.pl

```bash
$ singularity exec <container> /usr/local/bin/cdna_alignment_orf_to_genome_orf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cdna_alignment_orf_to_genome_orf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdna_alignment_orf_to_genome_orf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute_base_probs.pl

```bash
$ singularity exec <container> /usr/local/bin/compute_base_probs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compute_base_probs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute_base_probs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exclude_similar_proteins.pl

```bash
$ singularity exec <container> /usr/local/bin/exclude_similar_proteins.pl
$ podman run --it --rm --entrypoint /usr/local/bin/exclude_similar_proteins.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exclude_similar_proteins.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_prot_checker.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta_prot_checker.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_prot_checker.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_prot_checker.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch

```bash
$ singularity exec <container> /usr/local/bin/fetch
$ podman run --it --rm --entrypoint /usr/local/bin/fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffindex_resume.pl

```bash
$ singularity exec <container> /usr/local/bin/ffindex_resume.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ffindex_resume.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffindex_resume.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formcon

```bash
$ singularity exec <container> /usr/local/bin/formcon
$ podman run --it --rm --entrypoint /usr/local/bin/formcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formcon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_list_to_gff.pl

```bash
$ singularity exec <container> /usr/local/bin/gene_list_to_gff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gene_list_to_gff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_list_to_gff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genometools-config

```bash
$ singularity exec <container> /usr/local/bin/genometools-config
$ podman run --it --rm --entrypoint /usr/local/bin/genometools-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genometools-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_FL_accs.pl

```bash
$ singularity exec <container> /usr/local/bin/get_FL_accs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_FL_accs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_FL_accs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_longest_ORF_per_transcript.pl

```bash
$ singularity exec <container> /usr/local/bin/get_longest_ORF_per_transcript.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_longest_ORF_per_transcript.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_longest_ORF_per_transcript.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_top_longest_fasta_entries.pl

```bash
$ singularity exec <container> /usr/local/bin/get_top_longest_fasta_entries.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_top_longest_fasta_entries.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_top_longest_fasta_entries.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_file_to_bed.pl

```bash
$ singularity exec <container> /usr/local/bin/gff3_file_to_bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_file_to_bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_file_to_bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_file_to_proteins.pl

```bash
$ singularity exec <container> /usr/local/bin/gff3_file_to_proteins.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_file_to_proteins.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_file_to_proteins.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_gene_to_gtf_format.pl

```bash
$ singularity exec <container> /usr/local/bin/gff3_gene_to_gtf_format.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_gene_to_gtf_format.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_gene_to_gtf_format.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gt

```bash
$ singularity exec <container> /usr/local/bin/gt
$ podman run --it --rm --entrypoint /usr/local/bin/gt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_genome_to_cdna_fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf_genome_to_cdna_fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_genome_to_cdna_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_genome_to_cdna_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_to_alignment_gff3.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf_to_alignment_gff3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_to_alignment_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_to_alignment_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_to_bed.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf_to_bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_to_bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_to_bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexer

```bash
$ singularity exec <container> /usr/local/bin/indexer
$ podman run --it --rm --entrypoint /usr/local/bin/indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### netfetch

```bash
$ singularity exec <container> /usr/local/bin/netfetch
$ podman run --it --rm --entrypoint /usr/local/bin/netfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/netfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nr_ORFs_gff3.pl

```bash
$ singularity exec <container> /usr/local/bin/nr_ORFs_gff3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/nr_ORFs_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nr_ORFs_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfam_runner.pl

```bash
$ singularity exec <container> /usr/local/bin/pfam_runner.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pfam_runner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfam_runner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refine_gff3_group_iso_strip_utrs.pl

```bash
$ singularity exec <container> /usr/local/bin/refine_gff3_group_iso_strip_utrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/refine_gff3_group_iso_strip_utrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refine_gff3_group_iso_strip_utrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refine_hexamer_scores.pl

```bash
$ singularity exec <container> /usr/local/bin/refine_hexamer_scores.pl
$ podman run --it --rm --entrypoint /usr/local/bin/refine_hexamer_scores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refine_hexamer_scores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_eclipsed_ORFs.pl

```bash
$ singularity exec <container> /usr/local/bin/remove_eclipsed_ORFs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/remove_eclipsed_ORFs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_eclipsed_ORFs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### score_CDS_likelihood_all_6_frames.pl

```bash
$ singularity exec <container> /usr/local/bin/score_CDS_likelihood_all_6_frames.pl
$ podman run --it --rm --entrypoint /usr/local/bin/score_CDS_likelihood_all_6_frames.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/score_CDS_likelihood_all_6_frames.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_best_ORFs_per_transcript.pl

```bash
$ singularity exec <container> /usr/local/bin/select_best_ORFs_per_transcript.pl
$ podman run --it --rm --entrypoint /usr/local/bin/select_best_ORFs_per_transcript.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_best_ORFs_per_transcript.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_n_baseprobs_to_loglikelihood_vals.pl

```bash
$ singularity exec <container> /usr/local/bin/seq_n_baseprobs_to_loglikelihood_vals.pl
$ podman run --it --rm --entrypoint /usr/local/bin/seq_n_baseprobs_to_loglikelihood_vals.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_n_baseprobs_to_loglikelihood_vals.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### start_codon_refinement.pl

```bash
$ singularity exec <container> /usr/local/bin/start_codon_refinement.pl
$ podman run --it --rm --entrypoint /usr/local/bin/start_codon_refinement.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/start_codon_refinement.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train_start_PWM.pl

```bash
$ singularity exec <container> /usr/local/bin/train_start_PWM.pl
$ podman run --it --rm --entrypoint /usr/local/bin/train_start_PWM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train_start_PWM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uri_unescape.pl

```bash
$ singularity exec <container> /usr/local/bin/uri_unescape.pl
$ podman run --it --rm --entrypoint /usr/local/bin/uri_unescape.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uri_unescape.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readal

```bash
$ singularity exec <container> /usr/local/bin/readal
$ podman run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statal

```bash
$ singularity exec <container> /usr/local/bin/statal
$ podman run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimal

```bash
$ singularity exec <container> /usr/local/bin/trimal
$ podman run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_convert

```bash
$ singularity exec <container> /usr/local/bin/db_convert
$ podman run --it --rm --entrypoint /usr/local/bin/db_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-sparsecore.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-sparsecore.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### einsi

```bash
$ singularity exec <container> /usr/local/bin/einsi
$ podman run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftns

```bash
$ singularity exec <container> /usr/local/bin/fftns
$ podman run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftnsi

```bash
$ singularity exec <container> /usr/local/bin/fftnsi
$ podman run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ginsi

```bash
$ singularity exec <container> /usr/local/bin/ginsi
$ podman run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linsi

```bash
$ singularity exec <container> /usr/local/bin/linsi
$ podman run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
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