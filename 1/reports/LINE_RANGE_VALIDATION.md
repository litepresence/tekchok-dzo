# MDZOD Line Range Validation Report

**Generated:** 2026-02-19
**Scope:** All .txt files in /home/opencode/MDZOD/1/text/

## Validation Criteria

1. **Sequential validation:** Start lines must increase monotonically within each file
2. **Format validation:** Must match pattern [digits-digits]
3. **Consistency validation:** No duplicate ranges
4. **Boundary validation:** End line >= Start line for all ranges

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Files Scanned | 1465 |
| Files with Valid Ranges | 781 |
| Files with Invalid Ranges | 684 |
| Validation Rate | 53.31% |

## Files with Errors

The following 684 file(s) contain range errors:

- dynamic/commentary/01-01-01-01.txt
- dynamic/commentary/01-01-03-01.txt
- dynamic/commentary/01-02-01-05.txt
- dynamic/commentary/01-02-02-01.txt
- dynamic/commentary/01-03-01-01.txt
- dynamic/commentary/01-03-02-01.txt
- dynamic/commentary/01-03-03-01.txt
- dynamic/commentary/01-04-01-01.txt
- dynamic/commentary/01-04-02-01.txt
- dynamic/commentary/01-04-03-01.txt
- dynamic/commentary/01-04-04-01.txt
- dynamic/commentary/01-04-05-01.txt
- dynamic/commentary/01-04-06-01.txt
- dynamic/commentary/01-04-07-01.txt
- dynamic/commentary/01-04-08-01.txt
- dynamic/commentary/01-04-09-01.txt
- dynamic/commentary/01-04-10-01.txt
- dynamic/commentary/01-04-11-01.txt
- dynamic/commentary/01-04-12-01.txt
- dynamic/commentary/01-04-14-01.txt
- dynamic/commentary/01-04-15-01.txt
- dynamic/commentary/01-04-16-01.txt
- dynamic/commentary/01-04-18-01.txt
- dynamic/commentary/01-04-18-02.txt
- dynamic/commentary/01-05-02-01.txt
- dynamic/commentary/01-05-03-01.txt
- dynamic/commentary/01-05-04-01.txt
- dynamic/commentary/01-05-04-02.txt
- dynamic/commentary/01-05-04-03.txt
- dynamic/commentary/01-05-04-04.txt
- dynamic/commentary/01-05-04-05.txt
- dynamic/commentary/01-05-04-06.txt
- dynamic/commentary/01-05-05-01.txt
- dynamic/commentary/01-06-01-01.txt
- dynamic/commentary/01-06-02-01.txt
- dynamic/commentary/01-06-04-01.txt
- dynamic/commentary/01-06-05-01.txt
- dynamic/commentary/01-06-05-02.txt
- dynamic/commentary/01-06-05-03.txt
- dynamic/commentary/01-06-05-04.txt
- dynamic/commentary/01-06-05-05.txt
- dynamic/commentary/01-06-06-01.txt
- dynamic/commentary/01-06-07-01.txt
- dynamic/commentary/01-06-07-02.txt
- dynamic/commentary/01-06-07-03.txt
- dynamic/commentary/01-06-10-01.txt
- dynamic/commentary/01-06-12-01.txt
- dynamic/commentary/01-06-14-01.txt
- dynamic/commentary/01-07-01-01.txt
- dynamic/commentary/01-07-02-01.txt
- dynamic/commentary/01-07-03-01.txt
- dynamic/commentary/01-07-04-01.txt
- dynamic/commentary/01-07-05-01.txt
- dynamic/commentary/01-08-01-01.txt
- dynamic/commentary/01-08-04-01.txt
- dynamic/commentary/01-08-04-02.txt
- dynamic/commentary/01-08-06-01.txt
- dynamic/commentary/01-08-07-01.txt
- dynamic/commentary/01-08-08-01.txt
- dynamic/commentary/01-09-01-01.txt
- dynamic/commentary/01-10-01-01.txt
- dynamic/commentary/01-11-01-01.txt
- dynamic/commentary/01-12-01-01.txt
- dynamic/commentary/01-12-02-01.txt
- dynamic/commentary/01-12-05-01.txt
- dynamic/commentary/01-12-05-02.txt
- dynamic/commentary/01-12-06-01.txt
- dynamic/commentary/01-12-07-01.txt
- dynamic/commentary/01-13-01-01.txt
- dynamic/commentary/01-13-03-01.txt
- dynamic/commentary/01-13-04-01.txt
- dynamic/commentary/01-13-05-01.txt
- dynamic/commentary/01-14-01-01.txt
- dynamic/commentary/01-14-02-01.txt
- dynamic/commentary/01-14-04-01.txt
- dynamic/commentary/01-14-05-01.txt
- dynamic/commentary/01-14-06-01.txt
- dynamic/commentary/01-14-07-01.txt
- dynamic/commentary/01-14-07-02.txt
- dynamic/commentary/01-14-07-03.txt
- dynamic/commentary/01-14-08-01.txt
- dynamic/commentary/01-14-09-01.txt
- dynamic/commentary/01-14-10-01.txt
- dynamic/commentary/01-14-11-01.txt
- dynamic/commentary/01-14-12-01.txt
- dynamic/commentary/01-14-13-01.txt
- dynamic/commentary/02-15-01-01.txt
- dynamic/commentary/02-15-02-01.txt
- dynamic/commentary/02-15-03-01.txt
- dynamic/commentary/02-16-01-01.txt
- dynamic/commentary/02-16-02-01.txt
- dynamic/commentary/02-16-03-01.txt
- dynamic/commentary/02-16-04-01.txt
- dynamic/commentary/02-16-05-01.txt
- dynamic/commentary/02-17-01-01.txt
- dynamic/commentary/02-17-02-01.txt
- dynamic/commentary/02-17-03-01.txt
- dynamic/commentary/02-17-04-01.txt
- dynamic/commentary/02-17-05-01.txt
- dynamic/commentary/02-17-06-01.txt
- dynamic/commentary/02-17-07-01.txt
- dynamic/commentary/02-17-08-01.txt
- dynamic/commentary/02-17-09-01.txt
- dynamic/commentary/02-17-09-02.txt
- dynamic/commentary/02-17-10-01.txt
- dynamic/commentary/02-17-11-01.txt
- dynamic/commentary/02-17-12-01.txt
- dynamic/commentary/02-17-13-01.txt
- dynamic/commentary/02-17-14-01.txt
- dynamic/commentary/02-18-01-01.txt
- dynamic/commentary/02-18-02-01.txt
- dynamic/commentary/02-18-02-02.txt
- dynamic/commentary/02-18-02-03.txt
- dynamic/commentary/02-18-03-01.txt
- dynamic/commentary/02-18-03-02.txt
- dynamic/commentary/02-18-03-03.txt
- dynamic/commentary/02-18-03-04.txt
- dynamic/commentary/02-18-04-01.txt
- dynamic/commentary/02-18-05-01.txt
- dynamic/commentary/02-18-06-01.txt
- dynamic/commentary/02-18-07-01.txt
- dynamic/commentary/02-18-08-01.txt
- dynamic/commentary/02-18-08-02.txt
- dynamic/commentary/02-18-09-01.txt
- dynamic/commentary/02-18-10-01.txt
- dynamic/commentary/02-18-11-01.txt
- dynamic/commentary/02-18-12-01.txt
- dynamic/commentary/02-18-13-01.txt
- dynamic/commentary/02-18-14-01.txt
- dynamic/commentary/02-18-15-01.txt
- dynamic/commentary/02-18-16-01.txt
- dynamic/commentary/02-18-16-02.txt
- dynamic/commentary/02-18-16-03.txt
- dynamic/commentary/02-18-16-04.txt
- dynamic/commentary/02-19-00-01.txt
- dynamic/commentary/02-19-01-01.txt
- dynamic/commentary/02-20-01-01.txt
- dynamic/commentary/02-20-02-01.txt
- dynamic/commentary/02-20-03-01.txt
- dynamic/commentary/02-20-04-01.txt
- dynamic/commentary/02-20-05-01.txt
- dynamic/commentary/02-20-06-01.txt
- dynamic/commentary/02-20-07-01.txt
- dynamic/commentary/02-20-08-01.txt
- dynamic/commentary/02-21-00-01.txt
- dynamic/commentary/02-21-01-01.txt
- dynamic/commentary/02-22-01-01.txt
- dynamic/commentary/02-22-02-01.txt
- dynamic/commentary/02-22-03-01.txt
- dynamic/commentary/02-22-03-02.txt
- dynamic/commentary/02-22-03-03.txt
- dynamic/commentary/02-22-04-01.txt
- dynamic/commentary/02-22-05-01.txt
- dynamic/commentary/02-22-05-02.txt
- dynamic/commentary/02-22-06-01.txt
- dynamic/commentary/02-22-07-01.txt
- dynamic/commentary/02-23-01-01.txt
- dynamic/commentary/02-23-02-01.txt
- dynamic/commentary/02-23-02-02.txt
- dynamic/commentary/02-23-03-01.txt
- dynamic/commentary/02-23-03-02.txt
- dynamic/commentary/02-23-04-01.txt
- dynamic/commentary/02-23-05-01.txt
- dynamic/commentary/02-23-06-01.txt
- dynamic/commentary/02-23-06-02.txt
- dynamic/commentary/02-23-07-01.txt
- dynamic/commentary/02-23-08-01.txt
- dynamic/commentary/02-23-08-02.txt
- dynamic/commentary/02-23-08-03.txt
- dynamic/commentary/02-23-08-04.txt
- dynamic/commentary/02-23-08-05.txt
- dynamic/commentary/02-23-08-06.txt
- dynamic/commentary/02-23-08-07.txt
- dynamic/commentary/02-23-08-08.txt
- dynamic/commentary/02-23-08-09.txt
- dynamic/commentary/02-23-09-01.txt
- dynamic/commentary/02-24-01-01.txt
- dynamic/commentary/02-25-01-01.txt
- dynamic/commentary/02-25-02-01.txt
- dynamic/commentary/02-25-03-01.txt
- dynamic/commentary/02-25-04-01.txt
- dynamic/commentary/02-25-05-01.txt
- dynamic/commentary/02-25-06-01.txt
- dynamic/commentary/02-25-06-02.txt
- dynamic/commentary/02-25-07-01.txt
- dynamic/commentary_BACKUP/01-01-01-01.txt
- dynamic/commentary_BACKUP/01-01-03-01.txt
- dynamic/commentary_BACKUP/01-02-01-05.txt
- dynamic/commentary_BACKUP/01-02-02-01.txt
- dynamic/commentary_BACKUP/01-02-02-02.txt
- dynamic/commentary_BACKUP/01-03-02-01.txt
- dynamic/commentary_BACKUP/01-04-01-01.txt
- dynamic/commentary_BACKUP/01-04-02-01.txt
- dynamic/commentary_BACKUP/01-04-03-01.txt
- dynamic/commentary_BACKUP/01-04-04-01.txt
- dynamic/commentary_BACKUP/01-04-05-01.txt
- dynamic/commentary_BACKUP/01-04-06-01.txt
- dynamic/commentary_BACKUP/01-04-07-01.txt
- dynamic/commentary_BACKUP/01-04-08-01.txt
- dynamic/commentary_BACKUP/01-04-09-01.txt
- dynamic/commentary_BACKUP/01-04-10-01.txt
- dynamic/commentary_BACKUP/01-04-11-01.txt
- dynamic/commentary_BACKUP/01-04-12-01.txt
- dynamic/commentary_BACKUP/01-04-13-01.txt
- dynamic/commentary_BACKUP/01-04-14-01.txt
- dynamic/commentary_BACKUP/01-04-16-01.txt
- dynamic/commentary_BACKUP/01-04-18-01.txt
- dynamic/commentary_BACKUP/01-04-18-02.txt
- dynamic/commentary_BACKUP/01-04-19-01.txt
- dynamic/commentary_BACKUP/01-05-02-01.txt
- dynamic/commentary_BACKUP/01-05-03-01.txt
- dynamic/commentary_BACKUP/01-05-04-01.txt
- dynamic/commentary_BACKUP/01-05-04-02.txt
- dynamic/commentary_BACKUP/01-05-04-03.txt
- dynamic/commentary_BACKUP/01-05-04-04.txt
- dynamic/commentary_BACKUP/01-05-04-05.txt
- dynamic/commentary_BACKUP/01-05-04-06.txt
- dynamic/commentary_BACKUP/01-05-05-01.txt
- dynamic/commentary_BACKUP/01-06-01-01.txt
- dynamic/commentary_BACKUP/01-06-02-01.txt
- dynamic/commentary_BACKUP/01-06-03-01.txt
- dynamic/commentary_BACKUP/01-06-04-01.txt
- dynamic/commentary_BACKUP/01-06-05-01.txt
- dynamic/commentary_BACKUP/01-06-05-02.txt
- dynamic/commentary_BACKUP/01-06-05-03.txt
- dynamic/commentary_BACKUP/01-06-05-04.txt
- dynamic/commentary_BACKUP/01-06-05-05.txt
- dynamic/commentary_BACKUP/01-06-06-01.txt
- dynamic/commentary_BACKUP/01-06-07-01.txt
- dynamic/commentary_BACKUP/01-06-07-02.txt
- dynamic/commentary_BACKUP/01-06-07-03.txt
- dynamic/commentary_BACKUP/01-06-08-01.txt
- dynamic/commentary_BACKUP/01-06-10-01.txt
- dynamic/commentary_BACKUP/01-06-11-01.txt
- dynamic/commentary_BACKUP/01-06-12-01.txt
- dynamic/commentary_BACKUP/01-06-14-01.txt
- dynamic/commentary_BACKUP/01-07-01-01.txt
- dynamic/commentary_BACKUP/01-07-02-01.txt
- dynamic/commentary_BACKUP/01-07-03-01.txt
- dynamic/commentary_BACKUP/01-07-05-01.txt
- dynamic/commentary_BACKUP/01-08-01-01.txt
- dynamic/commentary_BACKUP/01-08-02-01.txt
- dynamic/commentary_BACKUP/01-08-04-01.txt
- dynamic/commentary_BACKUP/01-08-04-02.txt
- dynamic/commentary_BACKUP/01-08-06-01.txt
- dynamic/commentary_BACKUP/01-08-07-01.txt
- dynamic/commentary_BACKUP/01-08-08-01.txt
- dynamic/commentary_BACKUP/01-09-01-01.txt
- dynamic/commentary_BACKUP/01-09-02-01.txt
- dynamic/commentary_BACKUP/01-11-01-01.txt
- dynamic/commentary_BACKUP/01-11-02-01.txt
- dynamic/commentary_BACKUP/01-12-01-01.txt
- dynamic/commentary_BACKUP/01-12-02-01.txt
- dynamic/commentary_BACKUP/01-12-04-01.txt
- dynamic/commentary_BACKUP/01-12-05-01.txt
- dynamic/commentary_BACKUP/01-12-05-02.txt
- dynamic/commentary_BACKUP/01-12-06-01.txt
- dynamic/commentary_BACKUP/01-13-03-01.txt
- dynamic/commentary_BACKUP/01-13-04-01.txt
- dynamic/commentary_BACKUP/01-13-05-01.txt
- dynamic/commentary_BACKUP/01-14-02-01.txt
- dynamic/commentary_BACKUP/01-14-03-02.txt
- dynamic/commentary_BACKUP/01-14-05-01.txt
- dynamic/commentary_BACKUP/01-14-06-01.txt
- dynamic/commentary_BACKUP/01-14-07-01.txt
- dynamic/commentary_BACKUP/01-14-07-02.txt
- dynamic/commentary_BACKUP/01-14-07-03.txt
- dynamic/commentary_BACKUP/01-14-10-01.txt
- dynamic/commentary_BACKUP/01-14-11-01.txt
- dynamic/commentary_BACKUP/01-14-12-01.txt
- dynamic/commentary_BACKUP/01-14-13-01.txt
- dynamic/commentary_BACKUP/02-15-01-01.txt
- dynamic/commentary_BACKUP/02-15-02-01.txt
- dynamic/commentary_BACKUP/02-15-03-01.txt
- dynamic/commentary_BACKUP/02-16-01-01.txt
- dynamic/commentary_BACKUP/02-16-05-01.txt
- dynamic/commentary_BACKUP/02-17-01-01.txt
- dynamic/commentary_BACKUP/02-17-02-01.txt
- dynamic/commentary_BACKUP/02-17-03-01.txt
- dynamic/commentary_BACKUP/02-17-04-01.txt
- dynamic/commentary_BACKUP/02-17-05-01.txt
- dynamic/commentary_BACKUP/02-17-06-01.txt
- dynamic/commentary_BACKUP/02-17-09-01.txt
- dynamic/commentary_BACKUP/02-17-10-01.txt
- dynamic/commentary_BACKUP/02-17-11-01.txt
- dynamic/commentary_BACKUP/02-18-02-02.txt
- dynamic/commentary_BACKUP/02-18-03-01.txt
- dynamic/commentary_BACKUP/02-18-03-02.txt
- dynamic/commentary_BACKUP/02-18-03-03.txt
- dynamic/commentary_BACKUP/02-18-04-01.txt
- dynamic/commentary_BACKUP/02-18-06-01.txt
- dynamic/commentary_BACKUP/02-18-07-01.txt
- dynamic/commentary_BACKUP/02-18-08-01.txt
- dynamic/commentary_BACKUP/02-18-08-02.txt
- dynamic/commentary_BACKUP/02-18-09-01.txt
- dynamic/commentary_BACKUP/02-18-10-01.txt
- dynamic/commentary_BACKUP/02-18-14-01.txt
- dynamic/commentary_BACKUP/02-18-16-02.txt
- dynamic/commentary_BACKUP/02-18-16-03.txt
- dynamic/commentary_BACKUP/02-19-01-01.txt
- dynamic/commentary_BACKUP/02-20-01-01.txt
- dynamic/commentary_BACKUP/02-20-03-01.txt
- dynamic/commentary_BACKUP/02-20-04-01.txt
- dynamic/commentary_BACKUP/02-20-05-01.txt
- dynamic/commentary_BACKUP/02-20-06-01.txt
- dynamic/commentary_BACKUP/02-20-07-01.txt
- dynamic/commentary_BACKUP/02-20-08-01.txt
- dynamic/commentary_BACKUP/02-20-09-01.txt
- dynamic/commentary_BACKUP/02-22-02-01.txt
- dynamic/commentary_BACKUP/02-22-03-02.txt
- dynamic/commentary_BACKUP/02-22-03-03.txt
- dynamic/commentary_BACKUP/02-22-04-01.txt
- dynamic/commentary_BACKUP/02-23-02-01.txt
- dynamic/commentary_BACKUP/02-23-03-02.txt
- dynamic/commentary_BACKUP/02-23-04-01.txt
- dynamic/commentary_BACKUP/02-23-05-01.txt
- dynamic/commentary_BACKUP/02-23-06-01.txt
- dynamic/commentary_BACKUP/02-23-07-01.txt
- dynamic/commentary_BACKUP/02-23-08-01.txt
- dynamic/commentary_BACKUP/02-23-08-02.txt
- dynamic/commentary_BACKUP/02-23-08-03.txt
- dynamic/commentary_BACKUP/02-23-08-04.txt
- dynamic/commentary_BACKUP/02-23-08-06.txt
- dynamic/commentary_BACKUP/02-23-08-07.txt
- dynamic/commentary_BACKUP/02-23-08-08.txt
- dynamic/commentary_BACKUP/02-23-08-09.txt
- dynamic/commentary_BACKUP/02-23-09-01.txt
- dynamic/delusion/01-02-02-02.txt
- dynamic/delusion/01-04-03-01.txt
- dynamic/delusion/01-04-08-01.txt
- dynamic/delusion/01-04-10-01.txt
- dynamic/delusion/01-05-04-04.txt
- dynamic/delusion/01-06-01-01.txt
- dynamic/delusion/01-06-04-01.txt
- dynamic/delusion/01-06-13-01.txt
- dynamic/delusion/01-09-01-01.txt
- dynamic/delusion/01-10-01-01.txt
- dynamic/delusion/01-13-05-01.txt
- dynamic/delusion/01-13-06-01.txt
- dynamic/delusion/01-14-01-01.txt
- dynamic/delusion/02-16-03-01.txt
- dynamic/delusion/02-17-01-01.txt
- dynamic/delusion/02-17-08-01.txt
- dynamic/delusion/02-17-09-01.txt
- dynamic/delusion/02-17-09-02.txt
- dynamic/delusion/02-17-10-01.txt
- dynamic/delusion/02-17-12-01.txt
- dynamic/delusion/02-17-13-01.txt
- dynamic/delusion/02-18-03-04.txt
- dynamic/delusion/02-18-04-01.txt
- dynamic/delusion/02-18-05-01.txt
- dynamic/delusion/02-18-06-01.txt
- dynamic/delusion/02-18-07-01.txt
- dynamic/delusion/02-18-09-01.txt
- dynamic/delusion/02-18-10-01.txt
- dynamic/delusion/02-18-12-01.txt
- dynamic/delusion/02-18-13-01.txt
- dynamic/delusion/02-18-15-01.txt
- dynamic/delusion/02-18-16-04.txt
- dynamic/delusion/02-19-00-01.txt
- dynamic/delusion/02-20-02-01.txt
- dynamic/delusion/02-20-04-01.txt
- dynamic/delusion/02-20-05-01.txt
- dynamic/delusion/02-20-07-01.txt
- dynamic/delusion/02-20-08-01.txt
- dynamic/delusion/02-21-00-01.txt
- dynamic/delusion/02-21-01-01.txt
- dynamic/delusion/02-22-01-01.txt
- dynamic/delusion/02-22-03-02.txt
- dynamic/delusion/02-22-03-03.txt
- dynamic/delusion/02-22-04-01.txt
- dynamic/delusion/02-22-05-01.txt
- dynamic/delusion/02-22-05-02.txt
- dynamic/delusion/02-22-06-01.txt
- dynamic/delusion/02-23-01-01.txt
- dynamic/delusion/02-23-02-01.txt
- dynamic/delusion/02-23-02-02.txt
- dynamic/delusion/02-23-03-01.txt
- dynamic/delusion/02-23-03-02.txt
- dynamic/delusion/02-23-04-01.txt
- dynamic/delusion/02-23-06-01.txt
- dynamic/delusion/02-23-06-02.txt
- dynamic/delusion/02-23-08-03.txt
- dynamic/delusion/02-23-08-05.txt
- dynamic/delusion/02-23-08-09.txt
- dynamic/delusion/02-24-01-01.txt
- dynamic/delusion/02-25-02-01.txt
- dynamic/delusion/02-25-03-01.txt
- dynamic/delusion/02-25-04-01.txt
- dynamic/delusion/02-25-06-01.txt
- dynamic/delusion/02-25-06-02.txt
- dynamic/delusion/02-25-07-01.txt
- dynamic/delusion_backup/01-03-01-01.txt
- dynamic/delusion_backup/01-03-02-01.txt
- dynamic/delusion_backup/01-03-03-01.txt
- dynamic/delusion_backup/01-04-01-01.txt
- dynamic/delusion_backup/01-04-06-01.txt
- dynamic/delusion_backup/01-05-04-01.txt
- dynamic/delusion_backup/01-05-04-06.txt
- dynamic/delusion_backup/01-08-02-01.txt
- dynamic/delusion_backup/01-13-01-01.txt
- dynamic/delusion_backup/01-13-02-01.txt
- dynamic/delusion_backup/01-13-03-01.txt
- dynamic/delusion_backup/01-13-04-01.txt
- dynamic/delusion_backup/02-15-01-01.txt
- dynamic/delusion_backup/02-15-02-01.txt
- dynamic/delusion_backup/02-16-02-01.txt
- dynamic/delusion_backup/02-16-05-01.txt
- dynamic/delusion_backup/02-17-05-01.txt
- dynamic/delusion_backup/02-17-07-01.txt
- dynamic/delusion_final_backup/01-02-02-02.txt
- dynamic/delusion_final_backup/01-04-03-01.txt
- dynamic/delusion_final_backup/01-04-08-01.txt
- dynamic/delusion_final_backup/01-04-10-01.txt
- dynamic/delusion_final_backup/01-05-04-04.txt
- dynamic/delusion_final_backup/01-06-01-01.txt
- dynamic/delusion_final_backup/01-06-04-01.txt
- dynamic/delusion_final_backup/01-06-13-01.txt
- dynamic/delusion_final_backup/01-09-01-01.txt
- dynamic/delusion_final_backup/01-10-01-01.txt
- dynamic/delusion_final_backup/01-13-05-01.txt
- dynamic/delusion_final_backup/01-13-06-01.txt
- dynamic/delusion_final_backup/01-14-01-01.txt
- dynamic/delusion_final_backup/02-16-03-01.txt
- dynamic/delusion_final_backup/02-17-01-01.txt
- dynamic/delusion_final_backup/02-17-08-01.txt
- dynamic/delusion_final_backup/02-17-09-01.txt
- dynamic/delusion_final_backup/02-17-09-02.txt
- dynamic/delusion_final_backup/02-17-10-01.txt
- dynamic/delusion_final_backup/02-17-12-01.txt
- dynamic/delusion_final_backup/02-17-13-01.txt
- dynamic/delusion_final_backup/02-18-03-04.txt
- dynamic/delusion_final_backup/02-18-04-01.txt
- dynamic/delusion_final_backup/02-18-05-01.txt
- dynamic/delusion_final_backup/02-18-06-01.txt
- dynamic/delusion_final_backup/02-18-07-01.txt
- dynamic/delusion_final_backup/02-18-09-01.txt
- dynamic/delusion_final_backup/02-18-10-01.txt
- dynamic/delusion_final_backup/02-18-12-01.txt
- dynamic/delusion_final_backup/02-18-13-01.txt
- dynamic/delusion_final_backup/02-18-15-01.txt
- dynamic/delusion_final_backup/02-18-16-04.txt
- dynamic/delusion_final_backup/02-19-00-01.txt
- dynamic/delusion_final_backup/02-20-02-01.txt
- dynamic/delusion_final_backup/02-20-04-01.txt
- dynamic/delusion_final_backup/02-20-05-01.txt
- dynamic/delusion_final_backup/02-20-07-01.txt
- dynamic/delusion_final_backup/02-20-08-01.txt
- dynamic/delusion_final_backup/02-21-00-01.txt
- dynamic/delusion_final_backup/02-21-01-01.txt
- dynamic/delusion_final_backup/02-22-01-01.txt
- dynamic/delusion_final_backup/02-22-03-02.txt
- dynamic/delusion_final_backup/02-22-03-03.txt
- dynamic/delusion_final_backup/02-22-04-01.txt
- dynamic/delusion_final_backup/02-22-05-01.txt
- dynamic/delusion_final_backup/02-22-05-02.txt
- dynamic/delusion_final_backup/02-22-06-01.txt
- dynamic/delusion_final_backup/02-23-01-01.txt
- dynamic/delusion_final_backup/02-23-02-01.txt
- dynamic/delusion_final_backup/02-23-02-02.txt
- dynamic/delusion_final_backup/02-23-03-01.txt
- dynamic/delusion_final_backup/02-23-03-02.txt
- dynamic/delusion_final_backup/02-23-04-01.txt
- dynamic/delusion_final_backup/02-23-06-01.txt
- dynamic/delusion_final_backup/02-23-06-02.txt
- dynamic/delusion_final_backup/02-23-08-03.txt
- dynamic/delusion_final_backup/02-23-08-05.txt
- dynamic/delusion_final_backup/02-23-08-09.txt
- dynamic/delusion_final_backup/02-24-01-01.txt
- dynamic/delusion_final_backup/02-25-02-01.txt
- dynamic/delusion_final_backup/02-25-03-01.txt
- dynamic/delusion_final_backup/02-25-04-01.txt
- dynamic/delusion_final_backup/02-25-06-01.txt
- dynamic/delusion_final_backup/02-25-06-02.txt
- dynamic/delusion_final_backup/02-25-07-01.txt
- dynamic/delusion_oob_backup/02-16-03-01.txt
- dynamic/delusion_oob_backup/02-18-06-01.txt
- dynamic/delusion_oob_backup/02-18-16-04.txt
- dynamic/delusion_oob_backup/02-22-01-01.txt
- dynamic/delusion_oob_backup/02-22-03-02.txt
- dynamic/delusion_oob_backup/02-22-06-01.txt
- dynamic/delusion_oob_backup/02-23-06-01.txt
- dynamic/delusion_oob_backup/02-23-06-02.txt
- dynamic/delusion_oob_backup/02-23-08-03.txt
- dynamic/delusion_oob_backup/02-25-07-01.txt
- dynamic/scholar/01-01-01-01.txt
- dynamic/scholar/01-01-02-01.txt
- dynamic/scholar/01-02-01-03.txt
- dynamic/scholar/01-02-01-04.txt
- dynamic/scholar/01-02-01-05.txt
- dynamic/scholar/01-02-02-01.txt
- dynamic/scholar/01-02-02-02.txt
- dynamic/scholar/01-04-01-01.txt
- dynamic/scholar/01-04-02-01.txt
- dynamic/scholar/01-04-03-01.txt
- dynamic/scholar/01-04-04-01.txt
- dynamic/scholar/01-04-05-01.txt
- dynamic/scholar/01-04-06-01.txt
- dynamic/scholar/01-04-07-01.txt
- dynamic/scholar/01-04-08-01.txt
- dynamic/scholar/01-04-09-01.txt
- dynamic/scholar/01-04-10-01.txt
- dynamic/scholar/01-04-11-01.txt
- dynamic/scholar/01-04-12-01.txt
- dynamic/scholar/01-04-13-01.txt
- dynamic/scholar/01-04-14-01.txt
- dynamic/scholar/01-04-15-01.txt
- dynamic/scholar/01-04-17-01.txt
- dynamic/scholar/01-04-18-01.txt
- dynamic/scholar/01-04-18-02.txt
- dynamic/scholar/01-04-19-01.txt
- dynamic/scholar/01-05-01-01.txt
- dynamic/scholar/01-05-02-01.txt
- dynamic/scholar/01-05-03-01.txt
- dynamic/scholar/01-05-04-01.txt
- dynamic/scholar/01-05-04-06.txt
- dynamic/scholar/01-05-05-01.txt
- dynamic/scholar/01-06-01-01.txt
- dynamic/scholar/01-06-02-01.txt
- dynamic/scholar/01-06-04-01.txt
- dynamic/scholar/01-06-05-01.txt
- dynamic/scholar/01-06-05-05.txt
- dynamic/scholar/01-06-06-01.txt
- dynamic/scholar/01-06-07-01.txt
- dynamic/scholar/01-06-07-03.txt
- dynamic/scholar/01-06-08-01.txt
- dynamic/scholar/01-06-09-01.txt
- dynamic/scholar/01-06-10-01.txt
- dynamic/scholar/01-06-11-01.txt
- dynamic/scholar/01-06-12-01.txt
- dynamic/scholar/01-06-13-01.txt
- dynamic/scholar/01-07-03-01.txt
- dynamic/scholar/01-07-04-01.txt
- dynamic/scholar/01-08-01-01.txt
- dynamic/scholar/01-08-02-01.txt
- dynamic/scholar/01-08-03-01.txt
- dynamic/scholar/01-08-04-01.txt
- dynamic/scholar/01-08-05-01.txt
- dynamic/scholar/01-08-06-01.txt
- dynamic/scholar/01-08-07-01.txt
- dynamic/scholar/01-09-01-01.txt
- dynamic/scholar/01-10-01-01.txt
- dynamic/scholar/01-11-01-01.txt
- dynamic/scholar/01-12-04-01.txt
- dynamic/scholar/01-12-05-01.txt
- dynamic/scholar/01-12-05-02.txt
- dynamic/scholar/01-12-06-01.txt
- dynamic/scholar/01-12-07-01.txt
- dynamic/scholar/01-13-01-01.txt
- dynamic/scholar/01-13-02-01.txt
- dynamic/scholar/01-13-03-01.txt
- dynamic/scholar/01-14-02-01.txt
- dynamic/scholar/01-14-03-01.txt
- dynamic/scholar/01-14-03-02.txt
- dynamic/scholar/01-14-04-01.txt
- dynamic/scholar/01-14-05-01.txt
- dynamic/scholar/01-14-06-01.txt
- dynamic/scholar/01-14-07-04.txt
- dynamic/scholar/01-14-08-01.txt
- dynamic/scholar/01-14-09-01.txt
- dynamic/scholar/01-14-11-01.txt
- dynamic/scholar/02-15-03-01.txt
- dynamic/scholar/02-16-04-01.txt
- dynamic/scholar/02-16-05-01.txt
- dynamic/scholar/02-17-01-01.txt
- dynamic/scholar/02-17-02-01.txt
- dynamic/scholar/02-17-03-01.txt
- dynamic/scholar/02-17-04-01.txt
- dynamic/scholar/02-17-05-01.txt
- dynamic/scholar/02-17-06-01.txt
- dynamic/scholar/02-17-07-01.txt
- dynamic/scholar/02-17-08-01.txt
- dynamic/scholar/02-17-09-01.txt
- dynamic/scholar/02-17-09-02.txt
- dynamic/scholar/02-17-10-01.txt
- dynamic/scholar/02-17-11-01.txt
- dynamic/scholar/02-17-12-01.txt
- dynamic/scholar/02-17-13-01.txt
- dynamic/scholar/02-17-14-01.txt
- dynamic/scholar/02-18-01-01.txt
- dynamic/scholar/02-18-02-01.txt
- dynamic/scholar/02-18-02-02.txt
- dynamic/scholar/02-18-02-03.txt
- dynamic/scholar/02-18-03-04.txt
- dynamic/scholar/02-18-04-01.txt
- dynamic/scholar/02-18-06-01.txt
- dynamic/scholar/02-18-07-01.txt
- dynamic/scholar/02-18-08-01.txt
- dynamic/scholar/02-18-08-02.txt
- dynamic/scholar/02-18-09-01.txt
- dynamic/scholar/02-18-10-01.txt
- dynamic/scholar/02-18-11-01.txt
- dynamic/scholar/02-18-12-01.txt
- dynamic/scholar/02-18-13-01.txt
- dynamic/scholar/02-18-14-01.txt
- dynamic/scholar/02-18-15-01.txt
- dynamic/scholar/02-18-16-01.txt
- dynamic/scholar/02-18-16-02.txt
- dynamic/scholar/02-18-16-03.txt
- dynamic/scholar/02-18-16-04.txt
- dynamic/scholar/02-19-00-01.txt
- dynamic/scholar/02-19-01-01.txt
- dynamic/scholar/02-20-01-01.txt
- dynamic/scholar/02-20-02-01.txt
- dynamic/scholar/02-20-03-01.txt
- dynamic/scholar/02-20-04-01.txt
- dynamic/scholar/02-20-05-01.txt
- dynamic/scholar/02-20-06-01.txt
- dynamic/scholar/02-20-07-01.txt
- dynamic/scholar/02-20-08-01.txt
- dynamic/scholar/02-20-09-01.txt
- dynamic/scholar/02-21-00-01.txt
- dynamic/scholar/02-21-01-01.txt
- dynamic/scholar/02-22-01-01.txt
- dynamic/scholar/02-22-02-01.txt
- dynamic/scholar/02-22-03-03.txt
- dynamic/scholar/02-22-04-01.txt
- dynamic/scholar/02-22-05-01.txt
- dynamic/scholar/02-22-05-02.txt
- dynamic/scholar/02-22-06-01.txt
- dynamic/scholar/02-22-07-01.txt
- dynamic/scholar/02-23-01-01.txt
- dynamic/scholar/02-23-02-01.txt
- dynamic/scholar/02-23-02-02.txt
- dynamic/scholar/02-23-03-01.txt
- dynamic/scholar/02-23-03-02.txt
- dynamic/scholar/02-23-04-01.txt
- dynamic/scholar/02-23-05-01.txt
- dynamic/scholar/02-23-06-01.txt
- dynamic/scholar/02-23-06-02.txt
- dynamic/scholar/02-23-07-01.txt
- dynamic/scholar/02-23-08-03.txt
- dynamic/scholar/02-23-08-05.txt
- dynamic/scholar/02-23-08-09.txt
- dynamic/scholar/02-23-09-01.txt
- dynamic/scholar/02-24-01-01.txt
- dynamic/scholar/02-25-01-01.txt
- dynamic/scholar/02-25-02-01.txt
- dynamic/scholar/02-25-03-01.txt
- dynamic/scholar/02-25-04-01.txt
- dynamic/scholar/02-25-05-01.txt
- dynamic/scholar/02-25-06-01.txt
- dynamic/scholar/02-25-06-02.txt
- dynamic/scholar/02-25-07-01.txt
- frozen/epistemic/01-03-02-01.txt
- frozen/epistemic/01-03-03-01.txt
- frozen/epistemic/01-04-03-01.txt
- frozen/epistemic/01-04-05-01.txt
- frozen/epistemic/01-04-06-01.txt
- frozen/epistemic/01-04-08-01.txt
- frozen/epistemic/01-04-09-01.txt
- frozen/epistemic/01-04-11-01.txt
- frozen/epistemic/01-04-12-01.txt
- frozen/epistemic/01-04-18-01.txt
- frozen/epistemic/01-06-07-01.txt
- frozen/epistemic/01-06-07-03.txt
- frozen/epistemic/01-06-09-01.txt
- frozen/epistemic/01-06-10-01.txt
- frozen/epistemic/01-07-02-01.txt
- frozen/epistemic/01-07-03-01.txt
- frozen/epistemic/01-08-01-01.txt
- frozen/epistemic/01-08-03-01.txt
- frozen/epistemic/01-08-04-02.txt
- frozen/epistemic/01-14-11-01.txt
- frozen/epistemic/01-14-12-01.txt
- frozen/epistemic/02-18-11-01.txt
- frozen/epistemic/02-18-13-01.txt
- frozen/epistemic/02-18-15-01.txt
- frozen/epistemic/02-20-02-01.txt
- frozen/epistemic/02-20-04-01.txt
- frozen/epistemic/02-20-05-01.txt
- frozen/epistemic/02-20-06-01.txt
- frozen/epistemic/02-20-07-01.txt
- frozen/epistemic/02-20-08-01.txt
- frozen/epistemic/02-21-00-01.txt
- frozen/epistemic/02-21-01-01.txt
- frozen/epistemic/02-22-02-01.txt
- frozen/epistemic/02-22-03-01.txt
- frozen/epistemic/02-22-03-02.txt
- frozen/epistemic/02-22-03-03.txt
- frozen/epistemic/02-22-04-01.txt
- frozen/epistemic/02-22-05-01.txt
- frozen/epistemic/02-22-05-02.txt
- frozen/epistemic/02-22-06-01.txt

---

## Detailed Error Report

### File: dynamic/commentary/01-01-01-01.txt

**Errors:**
- Line 190: Non-sequential range [95-174] - Start (95) < Previous start (169)
- Line 216: Non-sequential range [146-174] - Start (146) < Previous start (161)
- Line 220: Non-sequential range [1-174] - Start (1) < Previous start (161)
- Line 304: Non-sequential range [166-174] - Start (166) < Previous start (171)
- Line 308: Non-sequential range [131-174] - Start (131) < Previous start (166)
- Line 192: Duplicate range [95-174]
- Line 194: Duplicate range [95-174]
- Line 196: Duplicate range [95-174]
- Line 200: Duplicate range [135-174]
- Line 202: Duplicate range [135-174]
- Line 204: Duplicate range [135-174]
- Line 206: Duplicate range [135-174]
- Line 208: Duplicate range [135-174]
- Line 210: Duplicate range [135-174]
- Line 212: Duplicate range [135-174]
- Line 218: Duplicate range [161-174]
- Line 222: Duplicate range [1-174]
- Line 224: Duplicate range [1-174]
- Line 226: Duplicate range [1-174]
- Line 228: Duplicate range [1-174]
- Line 230: Duplicate range [1-174]
- Line 232: Duplicate range [1-174]
- Line 234: Duplicate range [1-174]
- Line 236: Duplicate range [1-174]
- Line 238: Duplicate range [1-174]
- Line 240: Duplicate range [1-174]
- Line 242: Duplicate range [1-174]
- Line 244: Duplicate range [1-174]
- Line 246: Duplicate range [1-174]
- Line 248: Duplicate range [1-174]
- Line 250: Duplicate range [1-174]
- Line 252: Duplicate range [1-174]
- Line 254: Duplicate range [1-174]
- Line 256: Duplicate range [1-174]
- Line 258: Duplicate range [1-174]
- Line 260: Duplicate range [1-174]
- Line 262: Duplicate range [1-174]
- Line 264: Duplicate range [1-174]
- Line 266: Duplicate range [1-174]
- Line 268: Duplicate range [1-174]
- Line 270: Duplicate range [1-174]
- Line 272: Duplicate range [1-174]
- Line 274: Duplicate range [1-174]
- Line 276: Duplicate range [1-174]
- Line 278: Duplicate range [1-174]
- Line 280: Duplicate range [1-174]
- Line 282: Duplicate range [1-174]
- Line 284: Duplicate range [1-174]
- Line 286: Duplicate range [95-174]
- Line 290: Duplicate range [171-174]
- Line 292: Duplicate range [171-174]
- Line 294: Duplicate range [171-174]
- Line 296: Duplicate range [171-174]
- Line 298: Duplicate range [171-174]
- Line 300: Duplicate range [171-174]
- Line 302: Duplicate range [171-174]
- Line 306: Duplicate range [166-174]
- Line 310: Duplicate range [131-174]
- Line 312: Duplicate range [131-174]
- Line 314: Duplicate range [131-174]
- Line 316: Duplicate range [131-174]
- Line 318: Duplicate range [131-174]

---

### File: dynamic/commentary/01-01-03-01.txt

**Errors:**
- Line 30: Non-sequential range [1-57] - Start (1) < Previous start (42)
- Line 39: Duplicate range [57-57]
- Line 42: Duplicate range [57-57]
- Line 45: Duplicate range [57-57]
- Line 48: Duplicate range [57-57]

---

### File: dynamic/commentary/01-02-01-05.txt

**Errors:**
- Line 156: Non-sequential range [400-425] - Start (400) < Previous start (404)
- Line 186: Non-sequential range [390-425] - Start (390) < Previous start (402)
- Line 211: Non-sequential range [398-425] - Start (398) < Previous start (400)
- Line 226: Non-sequential range [376-425] - Start (376) < Previous start (398)
- Line 271: Non-sequential range [395-400] - Start (395) < Previous start (420)
- Line 281: Non-sequential range [382-387] - Start (382) < Previous start (401)
- Line 286: Non-sequential range [345-350] - Start (345) < Previous start (382)
- Line 296: Non-sequential range [326-331] - Start (326) < Previous start (351)
- Line 301: Non-sequential range [271-276] - Start (271) < Previous start (326)
- Line 306: Non-sequential range [216-221] - Start (216) < Previous start (271)
- Line 311: Non-sequential range [161-166] - Start (161) < Previous start (216)
- Line 316: Non-sequential range [84-89] - Start (84) < Previous start (161)
- Line 321: Non-sequential range [7-12] - Start (7) < Previous start (84)
- Line 326: Non-sequential range [1-425] - Start (1) < Previous start (7)
- Line 596: Non-sequential range [356-361] - Start (356) < Previous start (381)
- Line 601: Non-sequential range [311-316] - Start (311) < Previous start (356)
- Line 606: Non-sequential range [256-261] - Start (256) < Previous start (311)
- Line 611: Non-sequential range [179-184] - Start (179) < Previous start (256)
- Line 616: Non-sequential range [82-87] - Start (82) < Previous start (179)
- Line 621: Non-sequential range [1-425] - Start (1) < Previous start (82)
- Line 661: Non-sequential range [411-425] - Start (411) < Previous start (419)
- Line 666: Non-sequential range [406-425] - Start (406) < Previous start (411)
- Line 671: Non-sequential range [404-425] - Start (404) < Previous start (406)
- Line 681: Non-sequential range [402-425] - Start (402) < Previous start (404)
- Line 696: Non-sequential range [400-425] - Start (400) < Previous start (404)
- Line 706: Non-sequential range [390-425] - Start (390) < Previous start (402)
- Line 716: Non-sequential range [398-425] - Start (398) < Previous start (400)
- Line 721: Non-sequential range [376-425] - Start (376) < Previous start (398)
- Line 731: Non-sequential range [401-425] - Start (401) < Previous start (403)
- Line 736: Non-sequential range [395-400] - Start (395) < Previous start (401)
- Line 741: Non-sequential range [350-355] - Start (350) < Previous start (395)
- Line 761: Non-sequential range [295-300] - Start (295) < Previous start (398)
- Line 766: Non-sequential range [1-425] - Start (1) < Previous start (295)
- Line 781: Non-sequential range [412-425] - Start (412) < Previous start (419)
- Line 786: Non-sequential range [411-425] - Start (411) < Previous start (412)
- Line 801: Non-sequential range [411-425] - Start (411) < Previous start (419)
- Line 806: Non-sequential range [406-425] - Start (406) < Previous start (411)
- Line 811: Non-sequential range [404-425] - Start (404) < Previous start (406)
- Line 821: Non-sequential range [402-425] - Start (402) < Previous start (404)
- Line 836: Non-sequential range [400-425] - Start (400) < Previous start (404)
- Line 846: Non-sequential range [390-425] - Start (390) < Previous start (402)
- Line 856: Non-sequential range [398-425] - Start (398) < Previous start (400)
- Line 861: Non-sequential range [376-425] - Start (376) < Previous start (398)
- Line 876: Non-sequential range [395-400] - Start (395) < Previous start (420)
- Line 881: Non-sequential range [350-355] - Start (350) < Previous start (395)
- Line 886: Non-sequential range [295-300] - Start (295) < Previous start (350)
- Line 891: Non-sequential range [218-223] - Start (218) < Previous start (295)
- Line 896: Non-sequential range [121-126] - Start (121) < Previous start (218)
- Line 901: Non-sequential range [4-9] - Start (4) < Previous start (121)
- Line 131: Duplicate range [402-425]
- Line 136: Duplicate range [402-425]
- Line 146: Duplicate range [404-425]
- Line 151: Duplicate range [404-425]
- Line 161: Duplicate range [400-425]
- Line 166: Duplicate range [400-425]
- Line 171: Duplicate range [400-425]
- Line 176: Duplicate range [402-425]
- Line 181: Duplicate range [402-425]
- Line 191: Duplicate range [390-425]
- Line 196: Duplicate range [390-425]
- Line 201: Duplicate range [400-425]
- Line 206: Duplicate range [400-425]
- Line 216: Duplicate range [398-425]
- Line 221: Duplicate range [398-425]
- Line 231: Duplicate range [376-425]
- Line 236: Duplicate range [376-425]
- Line 246: Duplicate range [403-425]
- Line 251: Duplicate range [403-425]
- Line 261: Duplicate range [420-425]
- Line 266: Duplicate range [420-425]
- Line 331: Duplicate range [1-425]
- Line 336: Duplicate range [1-425]
- Line 341: Duplicate range [1-425]
- Line 346: Duplicate range [1-425]
- Line 351: Duplicate range [1-425]
- Line 356: Duplicate range [1-425]
- Line 361: Duplicate range [1-425]
- Line 366: Duplicate range [1-425]
- Line 371: Duplicate range [1-425]
- Line 376: Duplicate range [1-425]
- Line 381: Duplicate range [1-425]
- Line 386: Duplicate range [1-425]
- Line 391: Duplicate range [1-425]
- Line 396: Duplicate range [1-425]
- Line 401: Duplicate range [1-425]
- Line 406: Duplicate range [1-425]
- Line 411: Duplicate range [1-425]
- Line 416: Duplicate range [1-425]
- Line 421: Duplicate range [1-425]
- Line 426: Duplicate range [1-425]
- Line 431: Duplicate range [1-425]
- Line 436: Duplicate range [1-425]
- Line 441: Duplicate range [1-425]
- Line 446: Duplicate range [1-425]
- Line 451: Duplicate range [1-425]
- Line 456: Duplicate range [1-425]
- Line 461: Duplicate range [1-425]
- Line 466: Duplicate range [1-425]
- Line 471: Duplicate range [1-425]
- Line 476: Duplicate range [1-425]
- Line 481: Duplicate range [1-425]
- Line 486: Duplicate range [1-425]
- Line 491: Duplicate range [1-425]
- Line 496: Duplicate range [1-425]
- Line 501: Duplicate range [1-425]
- Line 621: Duplicate range [1-425]
- Line 661: Duplicate range [411-425]
- Line 671: Duplicate range [404-425]
- Line 676: Duplicate range [404-425]
- Line 681: Duplicate range [402-425]
- Line 686: Duplicate range [402-425]
- Line 691: Duplicate range [404-425]
- Line 696: Duplicate range [400-425]
- Line 701: Duplicate range [402-425]
- Line 706: Duplicate range [390-425]
- Line 711: Duplicate range [400-425]
- Line 716: Duplicate range [398-425]
- Line 721: Duplicate range [376-425]
- Line 726: Duplicate range [403-425]
- Line 736: Duplicate range [395-400]
- Line 766: Duplicate range [1-425]
- Line 771: Duplicate range [419-425]
- Line 776: Duplicate range [419-425]
- Line 786: Duplicate range [411-425]
- Line 791: Duplicate range [413-425]
- Line 796: Duplicate range [419-425]
- Line 801: Duplicate range [411-425]
- Line 806: Duplicate range [406-425]
- Line 811: Duplicate range [404-425]
- Line 816: Duplicate range [404-425]
- Line 821: Duplicate range [402-425]
- Line 826: Duplicate range [402-425]
- Line 831: Duplicate range [404-425]
- Line 836: Duplicate range [400-425]
- Line 841: Duplicate range [402-425]
- Line 846: Duplicate range [390-425]
- Line 851: Duplicate range [400-425]
- Line 856: Duplicate range [398-425]
- Line 861: Duplicate range [376-425]
- Line 866: Duplicate range [403-425]
- Line 871: Duplicate range [420-425]
- Line 876: Duplicate range [395-400]
- Line 881: Duplicate range [350-355]
- Line 886: Duplicate range [295-300]

---

### File: dynamic/commentary/01-02-02-01.txt

**Errors:**
- Line 29: Duplicate range [39-39]
- Line 34: Duplicate range [39-39]
- Line 41: Duplicate range [39-39]
- Line 46: Duplicate range [39-39]
- Line 53: Duplicate range [39-39]
- Line 56: Duplicate range [39-39]

---

### File: dynamic/commentary/01-03-01-01.txt

**Errors:**
- Line 29: Non-sequential range [64-69] - Start (64) < Previous start (84)
- Line 32: Non-sequential range [24-29] - Start (24) < Previous start (64)
- Line 35: Non-sequential range [1-89] - Start (1) < Previous start (24)
- Line 43: Duplicate range [1-89]
- Line 50: Duplicate range [1-89]
- Line 55: Duplicate range [1-89]

---

### File: dynamic/commentary/01-03-02-01.txt

**Errors:**
- Line 45: Non-sequential range [51-61] - Start (51) < Previous start (52)
- Line 28: Duplicate range [52-61]
- Line 33: Duplicate range [52-61]
- Line 36: Duplicate range [52-61]
- Line 39: Duplicate range [52-61]
- Line 42: Duplicate range [52-61]
- Line 50: Duplicate range [51-61]
- Line 53: Duplicate range [51-61]

---

### File: dynamic/commentary/01-03-03-01.txt

**Errors:**
- Line 75: Non-sequential range [120-170] - Start (120) < Previous start (166)

---

### File: dynamic/commentary/01-04-01-01.txt

**Errors:**
- Line 294: Non-sequential range [553-637] - Start (553) < Previous start (564)
- Line 299: Non-sequential range [438-637] - Start (438) < Previous start (553)
- Line 311: Non-sequential range [438-637] - Start (438) < Previous start (472)
- Line 328: Non-sequential range [621-637] - Start (621) < Previous start (635)
- Line 347: Non-sequential range [622-637] - Start (622) < Previous start (629)
- Line 406: Non-sequential range [618-637] - Start (618) < Previous start (628)
- Line 424: Non-sequential range [538-637] - Start (538) < Previous start (634)
- Line 443: Non-sequential range [338-637] - Start (338) < Previous start (538)
- Line 479: Non-sequential range [523-637] - Start (523) < Previous start (612)
- Line 493: Non-sequential range [553-637] - Start (553) < Previous start (564)
- Line 500: Non-sequential range [538-637] - Start (538) < Previous start (553)
- Line 506: Non-sequential range [338-637] - Start (338) < Previous start (538)
- Line 564: Non-sequential range [629-637] - Start (629) < Previous start (637)
- Line 571: Non-sequential range [613-637] - Start (613) < Previous start (629)
- Line 578: Non-sequential range [523-637] - Start (523) < Previous start (613)
- Line 591: Non-sequential range [538-637] - Start (538) < Previous start (587)
- Line 596: Non-sequential range [338-637] - Start (338) < Previous start (538)
- Line 675: Non-sequential range [625-637] - Start (625) < Previous start (637)
- Line 687: Non-sequential range [523-637] - Start (523) < Previous start (626)
- Line 708: Non-sequential range [619-637] - Start (619) < Previous start (621)
- Line 715: Non-sequential range [618-637] - Start (618) < Previous start (619)
- Line 727: Non-sequential range [614-637] - Start (614) < Previous start (618)
- Line 734: Non-sequential range [338-637] - Start (338) < Previous start (614)
- Line 778: Non-sequential range [612-637] - Start (612) < Previous start (637)
- Line 785: Non-sequential range [379-637] - Start (379) < Previous start (612)
- Line 792: Non-sequential range [338-637] - Start (338) < Previous start (379)
- Line 807: Non-sequential range [338-637] - Start (338) < Previous start (637)
- Line 299: Duplicate range [438-637]
- Line 311: Duplicate range [438-637]
- Line 352: Duplicate range [628-637]
- Line 359: Duplicate range [628-637]
- Line 365: Duplicate range [628-637]
- Line 371: Duplicate range [628-637]
- Line 377: Duplicate range [628-637]
- Line 383: Duplicate range [628-637]
- Line 389: Duplicate range [628-637]
- Line 395: Duplicate range [628-637]
- Line 401: Duplicate range [628-637]
- Line 412: Duplicate range [618-637]
- Line 430: Duplicate range [538-637]
- Line 437: Duplicate range [538-637]
- Line 449: Duplicate range [338-637]
- Line 456: Duplicate range [338-637]
- Line 466: Duplicate range [338-637]
- Line 486: Duplicate range [564-637]
- Line 493: Duplicate range [553-637]
- Line 500: Duplicate range [538-637]
- Line 506: Duplicate range [338-637]
- Line 514: Duplicate range [338-637]
- Line 521: Duplicate range [338-637]
- Line 527: Duplicate range [338-637]
- Line 533: Duplicate range [338-637]
- Line 537: Duplicate range [338-637]
- Line 544: Duplicate range [338-637]
- Line 550: Duplicate range [338-637]
- Line 564: Duplicate range [629-637]
- Line 578: Duplicate range [523-637]
- Line 591: Duplicate range [538-637]
- Line 596: Duplicate range [338-637]
- Line 602: Duplicate range [338-637]
- Line 608: Duplicate range [338-637]
- Line 614: Duplicate range [338-637]
- Line 620: Duplicate range [338-637]
- Line 626: Duplicate range [338-637]
- Line 633: Duplicate range [338-637]
- Line 640: Duplicate range [338-637]
- Line 647: Duplicate range [338-637]
- Line 653: Duplicate range [338-637]
- Line 659: Duplicate range [338-637]
- Line 666: Duplicate range [637-637]
- Line 687: Duplicate range [523-637]
- Line 694: Duplicate range [587-637]
- Line 701: Duplicate range [621-637]
- Line 715: Duplicate range [618-637]
- Line 721: Duplicate range [618-637]
- Line 734: Duplicate range [338-637]
- Line 740: Duplicate range [338-637]
- Line 746: Duplicate range [338-637]
- Line 753: Duplicate range [338-637]
- Line 760: Duplicate range [338-637]
- Line 767: Duplicate range [637-637]
- Line 778: Duplicate range [612-637]
- Line 792: Duplicate range [338-637]
- Line 797: Duplicate range [338-637]
- Line 804: Duplicate range [637-637]
- Line 807: Duplicate range [338-637]

---

### File: dynamic/commentary/01-04-02-01.txt

**Errors:**
- Line 40: Non-sequential range [80-294] - Start (80) < Previous start (179)
- Line 46: Non-sequential range [1-294] - Start (1) < Previous start (80)
- Line 67: Non-sequential range [1-294] - Start (1) < Previous start (294)
- Line 233: Non-sequential range [1-294] - Start (1) < Previous start (294)
- Line 269: Non-sequential range [1-294] - Start (1) < Previous start (294)
- Line 43: Duplicate range [80-294]
- Line 49: Duplicate range [1-294]
- Line 52: Duplicate range [1-294]
- Line 55: Duplicate range [1-294]
- Line 58: Duplicate range [1-294]
- Line 61: Duplicate range [1-294]
- Line 67: Duplicate range [1-294]
- Line 73: Duplicate range [1-294]
- Line 80: Duplicate range [1-294]
- Line 86: Duplicate range [1-294]
- Line 93: Duplicate range [1-294]
- Line 101: Duplicate range [1-294]
- Line 107: Duplicate range [1-294]
- Line 114: Duplicate range [1-294]
- Line 121: Duplicate range [1-294]
- Line 127: Duplicate range [1-294]
- Line 132: Duplicate range [1-294]
- Line 138: Duplicate range [1-294]
- Line 144: Duplicate range [1-294]
- Line 151: Duplicate range [1-294]
- Line 157: Duplicate range [1-294]
- Line 163: Duplicate range [1-294]
- Line 169: Duplicate range [1-294]
- Line 175: Duplicate range [1-294]
- Line 183: Duplicate range [1-294]
- Line 188: Duplicate range [1-294]
- Line 193: Duplicate range [1-294]
- Line 199: Duplicate range [1-294]
- Line 205: Duplicate range [1-294]
- Line 210: Duplicate range [1-294]
- Line 215: Duplicate range [1-294]
- Line 225: Duplicate range [1-294]
- Line 230: Duplicate range [294-294]
- Line 233: Duplicate range [1-294]
- Line 239: Duplicate range [1-294]
- Line 245: Duplicate range [1-294]
- Line 251: Duplicate range [1-294]
- Line 256: Duplicate range [1-294]
- Line 261: Duplicate range [1-294]
- Line 266: Duplicate range [294-294]
- Line 269: Duplicate range [1-294]
- Line 277: Duplicate range [1-294]
- Line 283: Duplicate range [1-294]
- Line 290: Duplicate range [1-294]
- Line 297: Duplicate range [1-294]
- Line 303: Duplicate range [1-294]
- Line 310: Duplicate range [1-294]
- Line 316: Duplicate range [1-294]
- Line 322: Duplicate range [1-294]
- Line 333: Duplicate range [1-294]
- Line 339: Duplicate range [294-294]

---

### File: dynamic/commentary/01-04-03-01.txt

**Errors:**
- Line 28: Non-sequential range [1-2] - Start (1) < Previous start (3)
- Line 31: Duplicate range [1-3]
- Line 34: Duplicate range [1-3]
- Line 37: Duplicate range [1-3]

---

### File: dynamic/commentary/01-04-04-01.txt

**Errors:**
- Line 28: Non-sequential range [8-13] - Start (8) < Previous start (11)
- Line 43: Non-sequential range [1-13] - Start (1) < Previous start (8)
- Line 13: Duplicate range [8-13]
- Line 19: Duplicate range [11-13]
- Line 22: Duplicate range [11-13]
- Line 25: Duplicate range [11-13]
- Line 28: Duplicate range [8-13]
- Line 31: Duplicate range [8-13]
- Line 34: Duplicate range [8-13]
- Line 37: Duplicate range [8-13]
- Line 40: Duplicate range [8-13]
- Line 43: Duplicate range [1-13]

---

### File: dynamic/commentary/01-04-05-01.txt

**Errors:**
- Line 16: Non-sequential range [12-24] - Start (12) < Previous start (22)
- Line 26: Non-sequential range [14-24] - Start (14) < Previous start (17)
- Line 32: Non-sequential range [19-24] - Start (19) < Previous start (20)
- Line 38: Non-sequential range [1-24] - Start (1) < Previous start (22)
- Line 46: Non-sequential range [1-24] - Start (1) < Previous start (14)
- Line 32: Duplicate range [19-24]
- Line 35: Duplicate range [22-24]
- Line 43: Duplicate range [14-24]
- Line 46: Duplicate range [1-24]

---

### File: dynamic/commentary/01-04-06-01.txt

**Errors:**
- Line 27: Non-sequential range [94-110] - Start (94) < Previous start (101)
- Line 33: Non-sequential range [91-110] - Start (91) < Previous start (94)
- Line 39: Non-sequential range [83-110] - Start (83) < Previous start (91)
- Line 49: Non-sequential range [105-110] - Start (105) < Previous start (107)
- Line 51: Non-sequential range [103-110] - Start (103) < Previous start (105)
- Line 55: Non-sequential range [97-102] - Start (97) < Previous start (105)
- Line 59: Non-sequential range [94-99] - Start (94) < Previous start (103)
- Line 23: Duplicate range [101-110]
- Line 25: Duplicate range [101-110]
- Line 29: Duplicate range [94-110]
- Line 31: Duplicate range [94-110]
- Line 35: Duplicate range [91-110]
- Line 37: Duplicate range [91-110]
- Line 41: Duplicate range [83-110]
- Line 43: Duplicate range [83-110]
- Line 47: Duplicate range [107-110]
- Line 53: Duplicate range [105-110]

---

### File: dynamic/commentary/01-04-07-01.txt

**Errors:**
- Line 16: Non-sequential range [3-6] - Start (3) < Previous start (5)
- Line 28: Non-sequential range [1-6] - Start (1) < Previous start (5)
- Line 19: Duplicate range [5-6]
- Line 28: Duplicate range [1-6]
- Line 31: Duplicate range [1-6]
- Line 34: Duplicate range [1-6]
- Line 37: Duplicate range [1-6]
- Line 40: Duplicate range [1-6]
- Line 43: Duplicate range [1-6]

---

### File: dynamic/commentary/01-04-08-01.txt

**Errors:**
- Line 20: Non-sequential range [25-28] - Start (25) < Previous start (26)
- Line 27: Non-sequential range [23-28] - Start (23) < Previous start (25)
- Line 47: Non-sequential range [21-28] - Start (21) < Previous start (27)
- Line 52: Duplicate range [27-28]

---

### File: dynamic/commentary/01-04-09-01.txt

**Errors:**
- Line 11: Non-sequential range [10-20] - Start (10) < Previous start (12)
- Line 31: Duplicate range [14-20]

---

### File: dynamic/commentary/01-04-10-01.txt

**Errors:**
- Line 25: Non-sequential range [1-3] - Start (1) < Previous start (2)
- Line 25: Duplicate range [1-3]
- Line 28: Duplicate range [1-3]
- Line 31: Duplicate range [1-3]
- Line 34: Duplicate range [1-3]
- Line 37: Duplicate range [1-3]
- Line 40: Duplicate range [1-3]
- Line 43: Duplicate range [1-3]

---

### File: dynamic/commentary/01-04-11-01.txt

**Errors:**
- Line 15: Non-sequential range [6-22] - Start (6) < Previous start (10)
- Line 35: Non-sequential range [18-22] - Start (18) < Previous start (19)
- Line 46: Duplicate range [18-22]
- Line 53: Duplicate range [18-22]

---

### File: dynamic/commentary/01-04-12-01.txt

**Errors:**
- Line 129: Non-sequential range [187-251] - Start (187) < Previous start (190)
- Line 143: Non-sequential range [232-251] - Start (232) < Previous start (233)
- Line 150: Non-sequential range [226-251] - Start (226) < Previous start (232)
- Line 164: Non-sequential range [225-251] - Start (225) < Previous start (229)
- Line 185: Non-sequential range [202-251] - Start (202) < Previous start (244)
- Line 199: Non-sequential range [187-251] - Start (187) < Previous start (241)
- Line 206: Non-sequential range [182-251] - Start (182) < Previous start (187)
- Line 213: Non-sequential range [73-251] - Start (73) < Previous start (182)
- Line 227: Non-sequential range [210-251] - Start (210) < Previous start (245)
- Line 234: Non-sequential range [3-251] - Start (3) < Previous start (210)
- Line 262: Non-sequential range [225-251] - Start (225) < Previous start (226)
- Line 276: Non-sequential range [237-251] - Start (237) < Previous start (239)
- Line 290: Non-sequential range [3-251] - Start (3) < Previous start (240)
- Line 318: Non-sequential range [3-251] - Start (3) < Previous start (245)
- Line 346: Non-sequential range [3-251] - Start (3) < Previous start (237)
- Line 360: Non-sequential range [187-251] - Start (187) < Previous start (225)
- Line 367: Non-sequential range [3-251] - Start (3) < Previous start (187)
- Line 381: Non-sequential range [195-251] - Start (195) < Previous start (239)
- Line 388: Non-sequential range [73-251] - Start (73) < Previous start (195)
- Line 409: Non-sequential range [3-251] - Start (3) < Previous start (237)
- Line 423: Non-sequential range [3-251] - Start (3) < Previous start (240)
- Line 437: Non-sequential range [3-251] - Start (3) < Previous start (225)
- Line 451: Non-sequential range [195-251] - Start (195) < Previous start (245)
- Line 458: Non-sequential range [3-251] - Start (3) < Previous start (195)
- Line 199: Duplicate range [187-251]
- Line 241: Duplicate range [202-251]
- Line 255: Duplicate range [226-251]
- Line 262: Duplicate range [225-251]
- Line 290: Duplicate range [3-251]
- Line 297: Duplicate range [73-251]
- Line 311: Duplicate range [245-251]
- Line 318: Duplicate range [3-251]
- Line 325: Duplicate range [187-251]
- Line 332: Duplicate range [237-251]
- Line 346: Duplicate range [3-251]
- Line 353: Duplicate range [225-251]
- Line 360: Duplicate range [187-251]
- Line 367: Duplicate range [3-251]
- Line 374: Duplicate range [239-251]
- Line 381: Duplicate range [195-251]
- Line 388: Duplicate range [73-251]
- Line 395: Duplicate range [237-251]
- Line 409: Duplicate range [3-251]
- Line 416: Duplicate range [240-251]
- Line 423: Duplicate range [3-251]
- Line 430: Duplicate range [225-251]
- Line 437: Duplicate range [3-251]
- Line 444: Duplicate range [245-251]
- Line 451: Duplicate range [195-251]
- Line 458: Duplicate range [3-251]

---

### File: dynamic/commentary/01-04-14-01.txt

**Errors:**
- Line 77: Non-sequential range [339-380] - Start (339) < Previous start (350)
- Line 97: Non-sequential range [301-380] - Start (301) < Previous start (364)
- Line 127: Non-sequential range [345-350] - Start (345) < Previous start (375)
- Line 130: Non-sequential range [285-290] - Start (285) < Previous start (345)
- Line 135: Non-sequential range [195-200] - Start (195) < Previous start (285)
- Line 140: Non-sequential range [75-80] - Start (75) < Previous start (195)
- Line 145: Non-sequential range [1-380] - Start (1) < Previous start (75)
- Line 70: Duplicate range [350-380]
- Line 82: Duplicate range [339-380]
- Line 92: Duplicate range [364-380]
- Line 102: Duplicate range [301-380]
- Line 150: Duplicate range [1-380]
- Line 155: Duplicate range [1-380]
- Line 185: Duplicate range [1-380]
- Line 190: Duplicate range [1-380]
- Line 195: Duplicate range [1-380]
- Line 200: Duplicate range [1-380]
- Line 205: Duplicate range [1-380]

---

### File: dynamic/commentary/01-04-15-01.txt

**Errors:**
- Line 66: Non-sequential range [33-45] - Start (33) < Previous start (40)

---

### File: dynamic/commentary/01-04-16-01.txt

**Errors:**
- Line 65: Non-sequential range [83-104] - Start (83) < Previous start (93)
- Line 81: Non-sequential range [83-104] - Start (83) < Previous start (96)
- Line 114: Non-sequential range [1-104] - Start (1) < Previous start (94)
- Line 81: Duplicate range [83-104]
- Line 116: Duplicate range [1-104]
- Line 118: Duplicate range [1-104]
- Line 120: Duplicate range [1-104]
- Line 122: Duplicate range [1-104]
- Line 124: Duplicate range [1-104]
- Line 126: Duplicate range [1-104]
- Line 128: Duplicate range [1-104]
- Line 130: Duplicate range [1-104]
- Line 132: Duplicate range [1-104]
- Line 134: Duplicate range [1-104]

---

### File: dynamic/commentary/01-04-18-01.txt

**Errors:**
- Line 8: Duplicate range [1-5]
- Line 13: Duplicate range [1-5]

---

### File: dynamic/commentary/01-04-18-02.txt

**Errors:**
- Line 85: Non-sequential range [88-101] - Start (88) < Previous start (89)
- Line 118: Non-sequential range [80-101] - Start (80) < Previous start (98)
- Line 74: Duplicate range [89-101]
- Line 120: Duplicate range [80-101]
- Line 122: Duplicate range [80-101]
- Line 124: Duplicate range [80-101]
- Line 126: Duplicate range [80-101]
- Line 128: Duplicate range [80-101]
- Line 130: Duplicate range [80-101]
- Line 132: Duplicate range [80-101]
- Line 134: Duplicate range [80-101]
- Line 136: Duplicate range [80-101]
- Line 138: Duplicate range [80-101]
- Line 140: Duplicate range [80-101]
- Line 142: Duplicate range [80-101]
- Line 144: Duplicate range [80-101]
- Line 146: Duplicate range [80-101]
- Line 148: Duplicate range [80-101]
- Line 150: Duplicate range [80-101]
- Line 152: Duplicate range [80-101]
- Line 154: Duplicate range [80-101]
- Line 156: Duplicate range [80-101]
- Line 158: Duplicate range [80-101]
- Line 160: Duplicate range [80-101]
- Line 162: Duplicate range [80-101]
- Line 164: Duplicate range [80-101]
- Line 166: Duplicate range [80-101]
- Line 168: Duplicate range [80-101]

---

### File: dynamic/commentary/01-05-02-01.txt

**Errors:**
- Line 166: Non-sequential range [336-356] - Start (336) < Previous start (340)
- Line 171: Non-sequential range [333-356] - Start (333) < Previous start (336)
- Line 181: Non-sequential range [332-356] - Start (332) < Previous start (334)
- Line 251: Non-sequential range [336-356] - Start (336) < Previous start (340)
- Line 256: Non-sequential range [333-356] - Start (333) < Previous start (336)
- Line 266: Non-sequential range [332-356] - Start (332) < Previous start (334)
- Line 336: Non-sequential range [2-356] - Start (2) < Previous start (340)
- Line 351: Non-sequential range [333-356] - Start (333) < Previous start (336)
- Line 361: Non-sequential range [332-356] - Start (332) < Previous start (334)
- Line 431: Non-sequential range [2-356] - Start (2) < Previous start (340)
- Line 96: Duplicate range [337-356]
- Line 101: Duplicate range [337-356]
- Line 106: Duplicate range [337-356]
- Line 111: Duplicate range [337-356]
- Line 116: Duplicate range [337-356]
- Line 121: Duplicate range [337-356]
- Line 126: Duplicate range [337-356]
- Line 131: Duplicate range [337-356]
- Line 136: Duplicate range [337-356]
- Line 141: Duplicate range [337-356]
- Line 146: Duplicate range [337-356]
- Line 151: Duplicate range [337-356]
- Line 156: Duplicate range [337-356]
- Line 186: Duplicate range [332-356]
- Line 191: Duplicate range [337-356]
- Line 196: Duplicate range [337-356]
- Line 201: Duplicate range [337-356]
- Line 206: Duplicate range [337-356]
- Line 211: Duplicate range [337-356]
- Line 216: Duplicate range [337-356]
- Line 221: Duplicate range [337-356]
- Line 226: Duplicate range [337-356]
- Line 231: Duplicate range [337-356]
- Line 236: Duplicate range [337-356]
- Line 241: Duplicate range [337-356]
- Line 246: Duplicate range [340-356]
- Line 251: Duplicate range [336-356]
- Line 256: Duplicate range [333-356]
- Line 261: Duplicate range [334-356]
- Line 266: Duplicate range [332-356]
- Line 271: Duplicate range [332-356]
- Line 276: Duplicate range [337-356]
- Line 281: Duplicate range [337-356]
- Line 286: Duplicate range [337-356]
- Line 291: Duplicate range [337-356]
- Line 296: Duplicate range [337-356]
- Line 301: Duplicate range [337-356]
- Line 306: Duplicate range [337-356]
- Line 311: Duplicate range [337-356]
- Line 316: Duplicate range [337-356]
- Line 321: Duplicate range [337-356]
- Line 326: Duplicate range [337-356]
- Line 331: Duplicate range [340-356]
- Line 341: Duplicate range [2-356]
- Line 346: Duplicate range [336-356]
- Line 351: Duplicate range [333-356]
- Line 356: Duplicate range [334-356]
- Line 361: Duplicate range [332-356]
- Line 366: Duplicate range [332-356]
- Line 371: Duplicate range [337-356]
- Line 376: Duplicate range [337-356]
- Line 381: Duplicate range [337-356]
- Line 386: Duplicate range [337-356]
- Line 391: Duplicate range [337-356]
- Line 396: Duplicate range [337-356]
- Line 401: Duplicate range [337-356]
- Line 406: Duplicate range [337-356]
- Line 411: Duplicate range [337-356]
- Line 416: Duplicate range [337-356]
- Line 421: Duplicate range [337-356]
- Line 426: Duplicate range [340-356]
- Line 431: Duplicate range [2-356]
- Line 436: Duplicate range [2-356]
- Line 441: Duplicate range [2-356]

---

### File: dynamic/commentary/01-05-03-01.txt

**Errors:**
- Line 121: Non-sequential range [38-209] - Start (38) < Previous start (190)
- Line 75: Duplicate range [190-209]
- Line 77: Duplicate range [190-209]
- Line 81: Duplicate range [190-209]
- Line 83: Duplicate range [190-209]
- Line 85: Duplicate range [190-209]
- Line 87: Duplicate range [190-209]
- Line 89: Duplicate range [190-209]
- Line 91: Duplicate range [190-209]
- Line 93: Duplicate range [190-209]
- Line 95: Duplicate range [190-209]
- Line 97: Duplicate range [190-209]
- Line 99: Duplicate range [190-209]
- Line 101: Duplicate range [190-209]
- Line 103: Duplicate range [190-209]
- Line 105: Duplicate range [190-209]
- Line 109: Duplicate range [190-209]
- Line 111: Duplicate range [190-209]
- Line 113: Duplicate range [190-209]
- Line 115: Duplicate range [190-209]
- Line 117: Duplicate range [190-209]
- Line 119: Duplicate range [190-209]
- Line 123: Duplicate range [38-209]
- Line 125: Duplicate range [38-209]
- Line 127: Duplicate range [38-209]
- Line 129: Duplicate range [38-209]
- Line 131: Duplicate range [38-209]
- Line 133: Duplicate range [38-209]
- Line 135: Duplicate range [38-209]
- Line 137: Duplicate range [38-209]
- Line 139: Duplicate range [38-209]
- Line 141: Duplicate range [38-209]
- Line 143: Duplicate range [38-209]
- Line 145: Duplicate range [38-209]
- Line 146: Duplicate range [38-209]
- Line 148: Duplicate range [38-209]
- Line 150: Duplicate range [38-209]
- Line 152: Duplicate range [38-209]
- Line 154: Duplicate range [38-209]
- Line 156: Duplicate range [38-209]
- Line 158: Duplicate range [38-209]
- Line 160: Duplicate range [38-209]
- Line 164: Duplicate range [38-209]

---

### File: dynamic/commentary/01-05-04-01.txt

**Errors:**
- Line 226: Non-sequential range [1-1572] - Start (1) < Previous start (1554)
- Line 236: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 246: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 261: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 266: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 316: Non-sequential range [1354-1572] - Start (1354) < Previous start (1473)
- Line 321: Non-sequential range [1-1572] - Start (1) < Previous start (1354)
- Line 341: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 351: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 366: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 371: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 421: Non-sequential range [1354-1572] - Start (1354) < Previous start (1473)
- Line 426: Non-sequential range [1-1572] - Start (1) < Previous start (1354)
- Line 441: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 451: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 466: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 471: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 516: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 541: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 636: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 646: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 656: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 671: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 676: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 726: Non-sequential range [1354-1572] - Start (1354) < Previous start (1473)
- Line 736: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 746: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 761: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 766: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 811: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 826: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 896: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 901: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 911: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 921: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 936: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 941: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 986: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 991: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1001: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1011: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1026: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1031: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 1076: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 1081: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1091: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1101: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1116: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1121: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 1166: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 1171: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1181: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1191: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1206: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1211: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 1256: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 1261: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1276: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1286: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1301: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1306: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 1351: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 1356: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1371: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1381: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1396: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1401: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 1446: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 1451: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1466: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1476: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1491: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1496: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 1541: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 1546: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1561: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1571: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1586: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1591: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 1636: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 1641: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1656: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1666: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1681: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1686: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 1731: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 1736: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1751: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1761: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1776: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1781: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 1826: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 1831: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1846: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1856: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1871: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1876: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 1921: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 1926: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 1941: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 1951: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 1966: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 1971: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 2016: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 2021: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 2036: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 2046: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 2061: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 2066: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 2111: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 2116: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 2131: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 2141: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 2156: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 2161: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 2206: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 2211: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 2226: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 2236: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 2251: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 2256: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 2301: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 2306: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 2321: Non-sequential range [1523-1572] - Start (1523) < Previous start (1542)
- Line 2331: Non-sequential range [1521-1572] - Start (1521) < Previous start (1523)
- Line 2346: Non-sequential range [1507-1572] - Start (1507) < Previous start (1521)
- Line 2351: Non-sequential range [1473-1572] - Start (1473) < Previous start (1507)
- Line 2396: Non-sequential range [1254-1572] - Start (1254) < Previous start (1473)
- Line 2401: Non-sequential range [1-1572] - Start (1) < Previous start (1254)
- Line 181: Duplicate range [1473-1572]
- Line 186: Duplicate range [1473-1572]
- Line 191: Duplicate range [1473-1572]
- Line 196: Duplicate range [1473-1572]
- Line 201: Duplicate range [1473-1572]
- Line 206: Duplicate range [1473-1572]
- Line 211: Duplicate range [1473-1572]
- Line 216: Duplicate range [1473-1572]
- Line 241: Duplicate range [1523-1572]
- Line 251: Duplicate range [1521-1572]
- Line 256: Duplicate range [1521-1572]
- Line 266: Duplicate range [1473-1572]
- Line 271: Duplicate range [1473-1572]
- Line 276: Duplicate range [1473-1572]
- Line 281: Duplicate range [1473-1572]
- Line 286: Duplicate range [1473-1572]
- Line 291: Duplicate range [1473-1572]
- Line 296: Duplicate range [1473-1572]
- Line 301: Duplicate range [1473-1572]
- Line 306: Duplicate range [1473-1572]
- Line 311: Duplicate range [1473-1572]
- Line 321: Duplicate range [1-1572]
- Line 326: Duplicate range [1-1572]
- Line 331: Duplicate range [1-1572]
- Line 336: Duplicate range [1542-1572]
- Line 341: Duplicate range [1523-1572]
- Line 346: Duplicate range [1523-1572]
- Line 351: Duplicate range [1521-1572]
- Line 356: Duplicate range [1521-1572]
- Line 361: Duplicate range [1521-1572]
- Line 366: Duplicate range [1507-1572]
- Line 371: Duplicate range [1473-1572]
- Line 376: Duplicate range [1473-1572]
- Line 381: Duplicate range [1473-1572]
- Line 386: Duplicate range [1473-1572]
- Line 391: Duplicate range [1473-1572]
- Line 396: Duplicate range [1473-1572]
- Line 401: Duplicate range [1473-1572]
- Line 406: Duplicate range [1473-1572]
- Line 411: Duplicate range [1473-1572]
- Line 416: Duplicate range [1473-1572]
- Line 421: Duplicate range [1354-1572]
- Line 426: Duplicate range [1-1572]
- Line 431: Duplicate range [1-1572]
- Line 436: Duplicate range [1542-1572]
- Line 441: Duplicate range [1523-1572]
- Line 446: Duplicate range [1523-1572]
- Line 451: Duplicate range [1521-1572]
- Line 456: Duplicate range [1521-1572]
- Line 461: Duplicate range [1521-1572]
- Line 466: Duplicate range [1507-1572]
- Line 471: Duplicate range [1473-1572]
- Line 476: Duplicate range [1473-1572]
- Line 481: Duplicate range [1473-1572]
- Line 486: Duplicate range [1473-1572]
- Line 491: Duplicate range [1473-1572]
- Line 496: Duplicate range [1473-1572]
- Line 501: Duplicate range [1473-1572]
- Line 506: Duplicate range [1473-1572]
- Line 511: Duplicate range [1473-1572]
- Line 521: Duplicate range [1507-1572]
- Line 526: Duplicate range [1507-1572]
- Line 531: Duplicate range [1507-1572]
- Line 536: Duplicate range [1507-1572]
- Line 541: Duplicate range [1473-1572]
- Line 546: Duplicate range [1473-1572]
- Line 551: Duplicate range [1473-1572]
- Line 556: Duplicate range [1473-1572]
- Line 561: Duplicate range [1473-1572]
- Line 566: Duplicate range [1473-1572]
- Line 571: Duplicate range [1473-1572]
- Line 576: Duplicate range [1473-1572]
- Line 581: Duplicate range [1473-1572]
- Line 586: Duplicate range [1473-1572]
- Line 591: Duplicate range [1473-1572]
- Line 596: Duplicate range [1473-1572]
- Line 601: Duplicate range [1473-1572]
- Line 606: Duplicate range [1473-1572]
- Line 611: Duplicate range [1473-1572]
- Line 616: Duplicate range [1473-1572]
- Line 621: Duplicate range [1473-1572]
- Line 626: Duplicate range [1473-1572]
- Line 631: Duplicate range [1473-1572]
- Line 636: Duplicate range [1254-1572]
- Line 641: Duplicate range [1542-1572]
- Line 646: Duplicate range [1523-1572]
- Line 651: Duplicate range [1523-1572]
- Line 656: Duplicate range [1521-1572]
- Line 661: Duplicate range [1521-1572]
- Line 666: Duplicate range [1521-1572]
- Line 671: Duplicate range [1507-1572]
- Line 676: Duplicate range [1473-1572]
- Line 681: Duplicate range [1473-1572]
- Line 686: Duplicate range [1473-1572]
- Line 691: Duplicate range [1473-1572]
- Line 696: Duplicate range [1473-1572]
- Line 701: Duplicate range [1473-1572]
- Line 706: Duplicate range [1473-1572]
- Line 711: Duplicate range [1473-1572]
- Line 716: Duplicate range [1473-1572]
- Line 721: Duplicate range [1473-1572]
- Line 726: Duplicate range [1354-1572]
- Line 731: Duplicate range [1542-1572]
- Line 736: Duplicate range [1523-1572]
- Line 741: Duplicate range [1523-1572]
- Line 746: Duplicate range [1521-1572]
- Line 751: Duplicate range [1521-1572]
- Line 756: Duplicate range [1521-1572]
- Line 761: Duplicate range [1507-1572]
- Line 766: Duplicate range [1473-1572]
- Line 771: Duplicate range [1473-1572]
- Line 776: Duplicate range [1473-1572]
- Line 781: Duplicate range [1473-1572]
- Line 786: Duplicate range [1473-1572]
- Line 791: Duplicate range [1473-1572]
- Line 796: Duplicate range [1473-1572]
- Line 801: Duplicate range [1473-1572]
- Line 806: Duplicate range [1473-1572]
- Line 811: Duplicate range [1254-1572]
- Line 816: Duplicate range [1507-1572]
- Line 821: Duplicate range [1507-1572]
- Line 826: Duplicate range [1473-1572]
- Line 831: Duplicate range [1473-1572]
- Line 836: Duplicate range [1473-1572]
- Line 841: Duplicate range [1473-1572]
- Line 846: Duplicate range [1473-1572]
- Line 851: Duplicate range [1473-1572]
- Line 856: Duplicate range [1473-1572]
- Line 861: Duplicate range [1473-1572]
- Line 866: Duplicate range [1473-1572]
- Line 871: Duplicate range [1473-1572]
- Line 876: Duplicate range [1473-1572]
- Line 881: Duplicate range [1473-1572]
- Line 886: Duplicate range [1473-1572]
- Line 891: Duplicate range [1473-1572]
- Line 896: Duplicate range [1254-1572]
- Line 901: Duplicate range [1-1572]
- Line 906: Duplicate range [1542-1572]
- Line 911: Duplicate range [1523-1572]
- Line 916: Duplicate range [1523-1572]
- Line 921: Duplicate range [1521-1572]
- Line 926: Duplicate range [1521-1572]
- Line 931: Duplicate range [1521-1572]
- Line 936: Duplicate range [1507-1572]
- Line 941: Duplicate range [1473-1572]
- Line 946: Duplicate range [1473-1572]
- Line 951: Duplicate range [1473-1572]
- Line 956: Duplicate range [1473-1572]
- Line 961: Duplicate range [1473-1572]
- Line 966: Duplicate range [1473-1572]
- Line 971: Duplicate range [1473-1572]
- Line 976: Duplicate range [1473-1572]
- Line 981: Duplicate range [1473-1572]
- Line 986: Duplicate range [1254-1572]
- Line 991: Duplicate range [1-1572]
- Line 996: Duplicate range [1542-1572]
- Line 1001: Duplicate range [1523-1572]
- Line 1006: Duplicate range [1523-1572]
- Line 1011: Duplicate range [1521-1572]
- Line 1016: Duplicate range [1521-1572]
- Line 1021: Duplicate range [1521-1572]
- Line 1026: Duplicate range [1507-1572]
- Line 1031: Duplicate range [1473-1572]
- Line 1036: Duplicate range [1473-1572]
- Line 1041: Duplicate range [1473-1572]
- Line 1046: Duplicate range [1473-1572]
- Line 1051: Duplicate range [1473-1572]
- Line 1056: Duplicate range [1473-1572]
- Line 1061: Duplicate range [1473-1572]
- Line 1066: Duplicate range [1473-1572]
- Line 1071: Duplicate range [1473-1572]
- Line 1076: Duplicate range [1254-1572]
- Line 1081: Duplicate range [1-1572]
- Line 1086: Duplicate range [1542-1572]
- Line 1091: Duplicate range [1523-1572]
- Line 1096: Duplicate range [1523-1572]
- Line 1101: Duplicate range [1521-1572]
- Line 1106: Duplicate range [1521-1572]
- Line 1111: Duplicate range [1521-1572]
- Line 1116: Duplicate range [1507-1572]
- Line 1121: Duplicate range [1473-1572]
- Line 1126: Duplicate range [1473-1572]
- Line 1131: Duplicate range [1473-1572]
- Line 1136: Duplicate range [1473-1572]
- Line 1141: Duplicate range [1473-1572]
- Line 1146: Duplicate range [1473-1572]
- Line 1151: Duplicate range [1473-1572]
- Line 1156: Duplicate range [1473-1572]
- Line 1161: Duplicate range [1473-1572]
- Line 1166: Duplicate range [1254-1572]
- Line 1171: Duplicate range [1-1572]
- Line 1176: Duplicate range [1542-1572]
- Line 1181: Duplicate range [1523-1572]
- Line 1186: Duplicate range [1523-1572]
- Line 1191: Duplicate range [1521-1572]
- Line 1196: Duplicate range [1521-1572]
- Line 1201: Duplicate range [1521-1572]
- Line 1206: Duplicate range [1507-1572]
- Line 1211: Duplicate range [1473-1572]
- Line 1216: Duplicate range [1473-1572]
- Line 1221: Duplicate range [1473-1572]
- Line 1226: Duplicate range [1473-1572]
- Line 1231: Duplicate range [1473-1572]
- Line 1236: Duplicate range [1473-1572]
- Line 1241: Duplicate range [1473-1572]
- Line 1246: Duplicate range [1473-1572]
- Line 1251: Duplicate range [1473-1572]
- Line 1256: Duplicate range [1254-1572]
- Line 1261: Duplicate range [1-1572]
- Line 1266: Duplicate range [1-1572]
- Line 1271: Duplicate range [1542-1572]
- Line 1276: Duplicate range [1523-1572]
- Line 1281: Duplicate range [1523-1572]
- Line 1286: Duplicate range [1521-1572]
- Line 1291: Duplicate range [1521-1572]
- Line 1296: Duplicate range [1521-1572]
- Line 1301: Duplicate range [1507-1572]
- Line 1306: Duplicate range [1473-1572]
- Line 1311: Duplicate range [1473-1572]
- Line 1316: Duplicate range [1473-1572]
- Line 1321: Duplicate range [1473-1572]
- Line 1326: Duplicate range [1473-1572]
- Line 1331: Duplicate range [1473-1572]
- Line 1336: Duplicate range [1473-1572]
- Line 1341: Duplicate range [1473-1572]
- Line 1346: Duplicate range [1473-1572]
- Line 1351: Duplicate range [1254-1572]
- Line 1356: Duplicate range [1-1572]
- Line 1361: Duplicate range [1-1572]
- Line 1366: Duplicate range [1542-1572]
- Line 1371: Duplicate range [1523-1572]
- Line 1376: Duplicate range [1523-1572]
- Line 1381: Duplicate range [1521-1572]
- Line 1386: Duplicate range [1521-1572]
- Line 1391: Duplicate range [1521-1572]
- Line 1396: Duplicate range [1507-1572]
- Line 1401: Duplicate range [1473-1572]
- Line 1406: Duplicate range [1473-1572]
- Line 1411: Duplicate range [1473-1572]
- Line 1416: Duplicate range [1473-1572]
- Line 1421: Duplicate range [1473-1572]
- Line 1426: Duplicate range [1473-1572]
- Line 1431: Duplicate range [1473-1572]
- Line 1436: Duplicate range [1473-1572]
- Line 1441: Duplicate range [1473-1572]
- Line 1446: Duplicate range [1254-1572]
- Line 1451: Duplicate range [1-1572]
- Line 1456: Duplicate range [1-1572]
- Line 1461: Duplicate range [1542-1572]
- Line 1466: Duplicate range [1523-1572]
- Line 1471: Duplicate range [1523-1572]
- Line 1476: Duplicate range [1521-1572]
- Line 1481: Duplicate range [1521-1572]
- Line 1486: Duplicate range [1521-1572]
- Line 1491: Duplicate range [1507-1572]
- Line 1496: Duplicate range [1473-1572]
- Line 1501: Duplicate range [1473-1572]
- Line 1506: Duplicate range [1473-1572]
- Line 1511: Duplicate range [1473-1572]
- Line 1516: Duplicate range [1473-1572]
- Line 1521: Duplicate range [1473-1572]
- Line 1526: Duplicate range [1473-1572]
- Line 1531: Duplicate range [1473-1572]
- Line 1536: Duplicate range [1473-1572]
- Line 1541: Duplicate range [1254-1572]
- Line 1546: Duplicate range [1-1572]
- Line 1551: Duplicate range [1-1572]
- Line 1556: Duplicate range [1542-1572]
- Line 1561: Duplicate range [1523-1572]
- Line 1566: Duplicate range [1523-1572]
- Line 1571: Duplicate range [1521-1572]
- Line 1576: Duplicate range [1521-1572]
- Line 1581: Duplicate range [1521-1572]
- Line 1586: Duplicate range [1507-1572]
- Line 1591: Duplicate range [1473-1572]
- Line 1596: Duplicate range [1473-1572]
- Line 1601: Duplicate range [1473-1572]
- Line 1606: Duplicate range [1473-1572]
- Line 1611: Duplicate range [1473-1572]
- Line 1616: Duplicate range [1473-1572]
- Line 1621: Duplicate range [1473-1572]
- Line 1626: Duplicate range [1473-1572]
- Line 1631: Duplicate range [1473-1572]
- Line 1636: Duplicate range [1254-1572]
- Line 1641: Duplicate range [1-1572]
- Line 1646: Duplicate range [1-1572]
- Line 1651: Duplicate range [1542-1572]
- Line 1656: Duplicate range [1523-1572]
- Line 1661: Duplicate range [1523-1572]
- Line 1666: Duplicate range [1521-1572]
- Line 1671: Duplicate range [1521-1572]
- Line 1676: Duplicate range [1521-1572]
- Line 1681: Duplicate range [1507-1572]
- Line 1686: Duplicate range [1473-1572]
- Line 1691: Duplicate range [1473-1572]
- Line 1696: Duplicate range [1473-1572]
- Line 1701: Duplicate range [1473-1572]
- Line 1706: Duplicate range [1473-1572]
- Line 1711: Duplicate range [1473-1572]
- Line 1716: Duplicate range [1473-1572]
- Line 1721: Duplicate range [1473-1572]
- Line 1726: Duplicate range [1473-1572]
- Line 1731: Duplicate range [1254-1572]
- Line 1736: Duplicate range [1-1572]
- Line 1741: Duplicate range [1-1572]
- Line 1746: Duplicate range [1542-1572]
- Line 1751: Duplicate range [1523-1572]
- Line 1756: Duplicate range [1523-1572]
- Line 1761: Duplicate range [1521-1572]
- Line 1766: Duplicate range [1521-1572]
- Line 1771: Duplicate range [1521-1572]
- Line 1776: Duplicate range [1507-1572]
- Line 1781: Duplicate range [1473-1572]
- Line 1786: Duplicate range [1473-1572]
- Line 1791: Duplicate range [1473-1572]
- Line 1796: Duplicate range [1473-1572]
- Line 1801: Duplicate range [1473-1572]
- Line 1806: Duplicate range [1473-1572]
- Line 1811: Duplicate range [1473-1572]
- Line 1816: Duplicate range [1473-1572]
- Line 1821: Duplicate range [1473-1572]
- Line 1826: Duplicate range [1254-1572]
- Line 1831: Duplicate range [1-1572]
- Line 1836: Duplicate range [1-1572]
- Line 1841: Duplicate range [1542-1572]
- Line 1846: Duplicate range [1523-1572]
- Line 1851: Duplicate range [1523-1572]
- Line 1856: Duplicate range [1521-1572]
- Line 1861: Duplicate range [1521-1572]
- Line 1866: Duplicate range [1521-1572]
- Line 1871: Duplicate range [1507-1572]
- Line 1876: Duplicate range [1473-1572]
- Line 1881: Duplicate range [1473-1572]
- Line 1886: Duplicate range [1473-1572]
- Line 1891: Duplicate range [1473-1572]
- Line 1896: Duplicate range [1473-1572]
- Line 1901: Duplicate range [1473-1572]
- Line 1906: Duplicate range [1473-1572]
- Line 1911: Duplicate range [1473-1572]
- Line 1916: Duplicate range [1473-1572]
- Line 1921: Duplicate range [1254-1572]
- Line 1926: Duplicate range [1-1572]
- Line 1931: Duplicate range [1-1572]
- Line 1936: Duplicate range [1542-1572]
- Line 1941: Duplicate range [1523-1572]
- Line 1946: Duplicate range [1523-1572]
- Line 1951: Duplicate range [1521-1572]
- Line 1956: Duplicate range [1521-1572]
- Line 1961: Duplicate range [1521-1572]
- Line 1966: Duplicate range [1507-1572]
- Line 1971: Duplicate range [1473-1572]
- Line 1976: Duplicate range [1473-1572]
- Line 1981: Duplicate range [1473-1572]
- Line 1986: Duplicate range [1473-1572]
- Line 1991: Duplicate range [1473-1572]
- Line 1996: Duplicate range [1473-1572]
- Line 2001: Duplicate range [1473-1572]
- Line 2006: Duplicate range [1473-1572]
- Line 2011: Duplicate range [1473-1572]
- Line 2016: Duplicate range [1254-1572]
- Line 2021: Duplicate range [1-1572]
- Line 2026: Duplicate range [1-1572]
- Line 2031: Duplicate range [1542-1572]
- Line 2036: Duplicate range [1523-1572]
- Line 2041: Duplicate range [1523-1572]
- Line 2046: Duplicate range [1521-1572]
- Line 2051: Duplicate range [1521-1572]
- Line 2056: Duplicate range [1521-1572]
- Line 2061: Duplicate range [1507-1572]
- Line 2066: Duplicate range [1473-1572]
- Line 2071: Duplicate range [1473-1572]
- Line 2076: Duplicate range [1473-1572]
- Line 2081: Duplicate range [1473-1572]
- Line 2086: Duplicate range [1473-1572]
- Line 2091: Duplicate range [1473-1572]
- Line 2096: Duplicate range [1473-1572]
- Line 2101: Duplicate range [1473-1572]
- Line 2106: Duplicate range [1473-1572]
- Line 2111: Duplicate range [1254-1572]
- Line 2116: Duplicate range [1-1572]
- Line 2121: Duplicate range [1-1572]
- Line 2126: Duplicate range [1542-1572]
- Line 2131: Duplicate range [1523-1572]
- Line 2136: Duplicate range [1523-1572]
- Line 2141: Duplicate range [1521-1572]
- Line 2146: Duplicate range [1521-1572]
- Line 2151: Duplicate range [1521-1572]
- Line 2156: Duplicate range [1507-1572]
- Line 2161: Duplicate range [1473-1572]
- Line 2166: Duplicate range [1473-1572]
- Line 2171: Duplicate range [1473-1572]
- Line 2176: Duplicate range [1473-1572]
- Line 2181: Duplicate range [1473-1572]
- Line 2186: Duplicate range [1473-1572]
- Line 2191: Duplicate range [1473-1572]
- Line 2196: Duplicate range [1473-1572]
- Line 2201: Duplicate range [1473-1572]
- Line 2206: Duplicate range [1254-1572]
- Line 2211: Duplicate range [1-1572]
- Line 2216: Duplicate range [1-1572]
- Line 2221: Duplicate range [1542-1572]
- Line 2226: Duplicate range [1523-1572]
- Line 2231: Duplicate range [1523-1572]
- Line 2236: Duplicate range [1521-1572]
- Line 2241: Duplicate range [1521-1572]
- Line 2246: Duplicate range [1521-1572]
- Line 2251: Duplicate range [1507-1572]
- Line 2256: Duplicate range [1473-1572]
- Line 2261: Duplicate range [1473-1572]
- Line 2266: Duplicate range [1473-1572]
- Line 2271: Duplicate range [1473-1572]
- Line 2276: Duplicate range [1473-1572]
- Line 2281: Duplicate range [1473-1572]
- Line 2286: Duplicate range [1473-1572]
- Line 2291: Duplicate range [1473-1572]
- Line 2296: Duplicate range [1473-1572]
- Line 2301: Duplicate range [1254-1572]
- Line 2306: Duplicate range [1-1572]
- Line 2311: Duplicate range [1-1572]
- Line 2316: Duplicate range [1542-1572]
- Line 2321: Duplicate range [1523-1572]
- Line 2326: Duplicate range [1523-1572]
- Line 2331: Duplicate range [1521-1572]
- Line 2336: Duplicate range [1521-1572]
- Line 2341: Duplicate range [1521-1572]
- Line 2346: Duplicate range [1507-1572]
- Line 2351: Duplicate range [1473-1572]
- Line 2356: Duplicate range [1473-1572]
- Line 2361: Duplicate range [1473-1572]
- Line 2366: Duplicate range [1473-1572]
- Line 2371: Duplicate range [1473-1572]
- Line 2376: Duplicate range [1473-1572]
- Line 2381: Duplicate range [1473-1572]
- Line 2386: Duplicate range [1473-1572]
- Line 2391: Duplicate range [1473-1572]
- Line 2396: Duplicate range [1254-1572]
- Line 2401: Duplicate range [1-1572]

---

### File: dynamic/commentary/01-05-04-02.txt

**Errors:**
- Line 3: Duplicate range [1-1]
- Line 5: Duplicate range [1-1]
- Line 7: Duplicate range [1-1]
- Line 9: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 13: Duplicate range [1-1]
- Line 15: Duplicate range [1-1]
- Line 17: Duplicate range [1-1]
- Line 19: Duplicate range [1-1]
- Line 21: Duplicate range [1-1]

---

### File: dynamic/commentary/01-05-04-03.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 16: Duplicate range [1-1]
- Line 20: Duplicate range [1-1]

---

### File: dynamic/commentary/01-05-04-04.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 12: Duplicate range [1-1]
- Line 17: Duplicate range [1-1]
- Line 21: Duplicate range [1-1]

---

### File: dynamic/commentary/01-05-04-05.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 16: Duplicate range [1-1]
- Line 20: Duplicate range [1-1]

---

### File: dynamic/commentary/01-05-04-06.txt

**Errors:**
- Line 71: Non-sequential range [177-182] - Start (177) < Previous start (269)
- Line 74: Non-sequential range [10-15] - Start (10) < Previous start (177)
- Line 93: Non-sequential range [1-335] - Start (1) < Previous start (10)
- Line 100: Duplicate range [1-335]
- Line 105: Duplicate range [1-335]
- Line 110: Duplicate range [1-335]
- Line 121: Duplicate range [1-335]
- Line 140: Duplicate range [1-335]
- Line 165: Duplicate range [1-335]
- Line 171: Duplicate range [1-335]
- Line 177: Duplicate range [1-335]
- Line 181: Duplicate range [1-335]
- Line 187: Duplicate range [1-335]

---

### File: dynamic/commentary/01-05-05-01.txt

**Errors:**
- Line 10: Duplicate range [42-42]
- Line 17: Duplicate range [42-42]
- Line 24: Duplicate range [42-42]
- Line 31: Duplicate range [42-42]
- Line 36: Duplicate range [42-42]
- Line 41: Duplicate range [42-42]
- Line 46: Duplicate range [42-42]
- Line 53: Duplicate range [42-42]
- Line 56: Duplicate range [42-42]
- Line 61: Duplicate range [42-42]
- Line 62: Duplicate range [42-42]

---

### File: dynamic/commentary/01-06-01-01.txt

**Errors:**
- Line 43: Non-sequential range [197-298] - Start (197) < Previous start (226)
- Line 46: Non-sequential range [99-298] - Start (99) < Previous start (197)
- Line 61: Non-sequential range [99-298] - Start (99) < Previous start (298)
- Line 159: Non-sequential range [99-298] - Start (99) < Previous start (298)
- Line 233: Non-sequential range [99-298] - Start (99) < Previous start (298)
- Line 295: Non-sequential range [99-298] - Start (99) < Previous start (298)
- Line 350: Non-sequential range [99-298] - Start (99) < Previous start (298)
- Line 357: Non-sequential range [99-298] - Start (99) < Previous start (298)
- Line 49: Duplicate range [99-298]
- Line 52: Duplicate range [99-298]
- Line 55: Duplicate range [99-298]
- Line 61: Duplicate range [99-298]
- Line 68: Duplicate range [99-298]
- Line 74: Duplicate range [99-298]
- Line 80: Duplicate range [99-298]
- Line 86: Duplicate range [99-298]
- Line 92: Duplicate range [99-298]
- Line 97: Duplicate range [99-298]
- Line 103: Duplicate range [99-298]
- Line 109: Duplicate range [99-298]
- Line 115: Duplicate range [99-298]
- Line 120: Duplicate range [99-298]
- Line 126: Duplicate range [99-298]
- Line 132: Duplicate range [99-298]
- Line 137: Duplicate range [99-298]
- Line 143: Duplicate range [99-298]
- Line 151: Duplicate range [99-298]
- Line 156: Duplicate range [298-298]
- Line 159: Duplicate range [99-298]
- Line 165: Duplicate range [99-298]
- Line 170: Duplicate range [99-298]
- Line 176: Duplicate range [99-298]
- Line 181: Duplicate range [99-298]
- Line 187: Duplicate range [99-298]
- Line 193: Duplicate range [99-298]
- Line 199: Duplicate range [99-298]
- Line 204: Duplicate range [99-298]
- Line 210: Duplicate range [99-298]
- Line 216: Duplicate range [99-298]
- Line 225: Duplicate range [99-298]
- Line 230: Duplicate range [298-298]
- Line 233: Duplicate range [99-298]
- Line 239: Duplicate range [99-298]
- Line 245: Duplicate range [99-298]
- Line 258: Duplicate range [99-298]
- Line 264: Duplicate range [99-298]
- Line 270: Duplicate range [99-298]
- Line 277: Duplicate range [99-298]
- Line 282: Duplicate range [99-298]
- Line 287: Duplicate range [99-298]
- Line 292: Duplicate range [298-298]
- Line 295: Duplicate range [99-298]
- Line 301: Duplicate range [99-298]
- Line 307: Duplicate range [99-298]
- Line 313: Duplicate range [99-298]
- Line 323: Duplicate range [99-298]
- Line 329: Duplicate range [99-298]
- Line 334: Duplicate range [99-298]
- Line 337: Duplicate range [99-298]
- Line 342: Duplicate range [99-298]
- Line 347: Duplicate range [298-298]
- Line 350: Duplicate range [99-298]
- Line 354: Duplicate range [298-298]
- Line 357: Duplicate range [99-298]
- Line 362: Duplicate range [99-298]
- Line 365: Duplicate range [99-298]
- Line 368: Duplicate range [298-298]

---

### File: dynamic/commentary/01-06-02-01.txt

**Errors:**
- Line 121: Non-sequential range [1-1013] - Start (1) < Previous start (263)
- Line 149: Duplicate range [1-1013]
- Line 158: Duplicate range [1-1013]
- Line 167: Duplicate range [1-1013]
- Line 176: Duplicate range [1-1013]
- Line 189: Duplicate range [1-1013]
- Line 198: Duplicate range [1-1013]
- Line 215: Duplicate range [1-1013]
- Line 232: Duplicate range [1-1013]
- Line 243: Duplicate range [1-1013]
- Line 258: Duplicate range [1-1013]
- Line 275: Duplicate range [1-1013]
- Line 288: Duplicate range [1-1013]
- Line 307: Duplicate range [1-1013]
- Line 326: Duplicate range [1-1013]
- Line 343: Duplicate range [1-1013]
- Line 356: Duplicate range [1-1013]
- Line 375: Duplicate range [1-1013]
- Line 392: Duplicate range [1-1013]
- Line 407: Duplicate range [1-1013]
- Line 426: Duplicate range [1-1013]
- Line 445: Duplicate range [1-1013]
- Line 462: Duplicate range [1-1013]
- Line 481: Duplicate range [1-1013]
- Line 494: Duplicate range [1-1013]
- Line 511: Duplicate range [1-1013]
- Line 528: Duplicate range [1-1013]
- Line 545: Duplicate range [1-1013]
- Line 566: Duplicate range [1-1013]
- Line 591: Duplicate range [1-1013]
- Line 610: Duplicate range [1-1013]
- Line 627: Duplicate range [1-1013]
- Line 646: Duplicate range [1-1013]
- Line 661: Duplicate range [1-1013]
- Line 676: Duplicate range [1-1013]
- Line 689: Duplicate range [1-1013]
- Line 706: Duplicate range [1-1013]
- Line 723: Duplicate range [1-1013]
- Line 738: Duplicate range [1-1013]
- Line 751: Duplicate range [1-1013]
- Line 768: Duplicate range [1-1013]

---

### File: dynamic/commentary/01-06-04-01.txt

**Errors:**
- Line 251: Non-sequential range [371-376] - Start (371) < Previous start (500)
- Line 259: Non-sequential range [142-147] - Start (142) < Previous start (371)
- Line 267: Non-sequential range [1-534] - Start (1) < Previous start (142)
- Line 221: Duplicate range [435-534]
- Line 276: Duplicate range [1-534]
- Line 285: Duplicate range [1-534]
- Line 294: Duplicate range [1-534]
- Line 307: Duplicate range [1-534]
- Line 324: Duplicate range [1-534]
- Line 337: Duplicate range [1-534]
- Line 345: Duplicate range [1-534]
- Line 353: Duplicate range [1-534]
- Line 362: Duplicate range [1-534]
- Line 369: Duplicate range [1-534]
- Line 406: Duplicate range [1-534]

---

### File: dynamic/commentary/01-06-05-01.txt

**Errors:**
- Line 7: Duplicate range [1-2]
- Line 19: Duplicate range [1-2]
- Line 22: Duplicate range [1-2]

---

### File: dynamic/commentary/01-06-05-02.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 15: Duplicate range [1-1]
- Line 20: Duplicate range [1-1]

---

### File: dynamic/commentary/01-06-05-03.txt

**Errors:**
- Line 7: Duplicate range [1-1]
- Line 12: Duplicate range [1-1]
- Line 17: Duplicate range [1-1]
- Line 22: Duplicate range [1-1]

---

### File: dynamic/commentary/01-06-05-04.txt

**Errors:**
- Line 7: Duplicate range [1-1]
- Line 13: Duplicate range [1-1]
- Line 18: Duplicate range [1-1]
- Line 23: Duplicate range [1-1]
- Line 28: Duplicate range [1-1]
- Line 33: Duplicate range [1-1]
- Line 37: Duplicate range [1-1]

---

### File: dynamic/commentary/01-06-05-05.txt

**Errors:**
- Line 12: Non-sequential range [1-2] - Start (1) < Previous start (3)
- Line 16: Duplicate range [1-3]
- Line 20: Duplicate range [1-3]
- Line 25: Duplicate range [1-3]

---

### File: dynamic/commentary/01-06-06-01.txt

**Errors:**
- Line 23: Non-sequential range [1-6] - Start (1) < Previous start (7)
- Line 35: Duplicate range [1-7]

---

### File: dynamic/commentary/01-06-07-01.txt

**Errors:**
- Line 28: Non-sequential range [25-37] - Start (25) < Previous start (32)
- Line 33: Duplicate range [25-37]
- Line 36: Duplicate range [25-37]
- Line 47: Duplicate range [33-37]

---

### File: dynamic/commentary/01-06-07-02.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 16: Duplicate range [1-1]
- Line 20: Duplicate range [1-1]

---

### File: dynamic/commentary/01-06-07-03.txt

**Errors:**
- Line 23: Non-sequential range [35-45] - Start (35) < Previous start (40)
- Line 45: Non-sequential range [32-45] - Start (32) < Previous start (43)
- Line 28: Duplicate range [35-45]
- Line 31: Duplicate range [35-45]
- Line 34: Duplicate range [35-45]
- Line 42: Duplicate range [43-45]
- Line 50: Duplicate range [32-45]
- Line 53: Duplicate range [32-45]

---

### File: dynamic/commentary/01-06-10-01.txt

**Errors:**
- Line 51: Duplicate range [32-32]
- Line 54: Duplicate range [32-32]
- Line 57: Duplicate range [32-32]
- Line 60: Duplicate range [32-32]
- Line 67: Duplicate range [32-32]
- Line 74: Duplicate range [32-32]

---

### File: dynamic/commentary/01-06-12-01.txt

**Errors:**
- Line 256: Non-sequential range [494-503] - Start (494) < Previous start (497)
- Line 296: Non-sequential range [63-503] - Start (63) < Previous start (494)
- Line 321: Non-sequential range [480-503] - Start (480) < Previous start (484)
- Line 326: Non-sequential range [474-503] - Start (474) < Previous start (480)
- Line 331: Non-sequential range [468-503] - Start (468) < Previous start (474)
- Line 346: Non-sequential range [479-503] - Start (479) < Previous start (484)
- Line 356: Non-sequential range [472-503] - Start (472) < Previous start (493)
- Line 366: Non-sequential range [2-503] - Start (2) < Previous start (472)
- Line 381: Non-sequential range [2-503] - Start (2) < Previous start (262)
- Line 401: Non-sequential range [478-503] - Start (478) < Previous start (488)
- Line 411: Non-sequential range [467-503] - Start (467) < Previous start (480)
- Line 421: Non-sequential range [475-503] - Start (475) < Previous start (481)
- Line 426: Non-sequential range [466-503] - Start (466) < Previous start (475)
- Line 431: Non-sequential range [451-503] - Start (451) < Previous start (466)
- Line 441: Non-sequential range [460-503] - Start (460) < Previous start (470)
- Line 451: Non-sequential range [468-503] - Start (468) < Previous start (474)
- Line 456: Non-sequential range [460-503] - Start (460) < Previous start (468)
- Line 471: Non-sequential range [2-503] - Start (2) < Previous start (472)
- Line 496: Non-sequential range [460-503] - Start (460) < Previous start (484)
- Line 501: Non-sequential range [438-503] - Start (438) < Previous start (460)
- Line 511: Non-sequential range [436-503] - Start (436) < Previous start (460)
- Line 516: Non-sequential range [2-503] - Start (2) < Previous start (436)
- Line 221: Duplicate range [489-503]
- Line 231: Duplicate range [494-503]
- Line 236: Duplicate range [494-503]
- Line 241: Duplicate range [494-503]
- Line 251: Duplicate range [497-503]
- Line 256: Duplicate range [494-503]
- Line 261: Duplicate range [494-503]
- Line 266: Duplicate range [494-503]
- Line 271: Duplicate range [494-503]
- Line 276: Duplicate range [494-503]
- Line 281: Duplicate range [494-503]
- Line 286: Duplicate range [494-503]
- Line 291: Duplicate range [494-503]
- Line 301: Duplicate range [484-503]
- Line 306: Duplicate range [484-503]
- Line 311: Duplicate range [484-503]
- Line 316: Duplicate range [484-503]
- Line 336: Duplicate range [480-503]
- Line 341: Duplicate range [484-503]
- Line 361: Duplicate range [472-503]
- Line 371: Duplicate range [2-503]
- Line 381: Duplicate range [2-503]
- Line 386: Duplicate range [2-503]
- Line 391: Duplicate range [2-503]
- Line 406: Duplicate range [480-503]
- Line 446: Duplicate range [474-503]
- Line 451: Duplicate range [468-503]
- Line 456: Duplicate range [460-503]
- Line 461: Duplicate range [468-503]
- Line 466: Duplicate range [472-503]
- Line 471: Duplicate range [2-503]
- Line 476: Duplicate range [2-503]
- Line 481: Duplicate range [2-503]
- Line 491: Duplicate range [484-503]
- Line 496: Duplicate range [460-503]
- Line 506: Duplicate range [460-503]
- Line 516: Duplicate range [2-503]
- Line 521: Duplicate range [2-503]
- Line 526: Duplicate range [2-503]
- Line 531: Duplicate range [2-503]
- Line 536: Duplicate range [2-503]
- Line 541: Duplicate range [2-503]
- Line 546: Duplicate range [2-503]
- Line 551: Duplicate range [2-503]
- Line 556: Duplicate range [2-503]
- Line 561: Duplicate range [2-503]
- Line 566: Duplicate range [2-503]
- Line 571: Duplicate range [2-503]
- Line 576: Duplicate range [2-503]
- Line 581: Duplicate range [2-503]
- Line 586: Duplicate range [2-503]
- Line 591: Duplicate range [2-503]
- Line 596: Duplicate range [2-503]
- Line 601: Duplicate range [2-503]
- Line 606: Duplicate range [2-503]
- Line 611: Duplicate range [2-503]
- Line 614: Duplicate range [2-503]

---

### File: dynamic/commentary/01-06-14-01.txt

**Errors:**
- Line 7: Duplicate range [1-1]
- Line 13: Duplicate range [1-1]
- Line 19: Duplicate range [1-1]
- Line 24: Duplicate range [1-1]

---

### File: dynamic/commentary/01-07-01-01.txt

**Errors:**
- Line 81: Non-sequential range [167-195] - Start (167) < Previous start (184)
- Line 53: Duplicate range [175-195]
- Line 55: Duplicate range [175-195]
- Line 57: Duplicate range [175-195]
- Line 59: Duplicate range [175-195]
- Line 61: Duplicate range [175-195]
- Line 63: Duplicate range [175-195]
- Line 67: Duplicate range [184-195]
- Line 69: Duplicate range [184-195]
- Line 71: Duplicate range [184-195]
- Line 73: Duplicate range [184-195]
- Line 75: Duplicate range [184-195]
- Line 77: Duplicate range [184-195]
- Line 79: Duplicate range [184-195]
- Line 83: Duplicate range [167-195]
- Line 85: Duplicate range [167-195]
- Line 87: Duplicate range [167-195]
- Line 89: Duplicate range [167-195]
- Line 91: Duplicate range [167-195]
- Line 93: Duplicate range [167-195]
- Line 95: Duplicate range [167-195]
- Line 99: Duplicate range [185-195]
- Line 101: Duplicate range [185-195]
- Line 103: Duplicate range [185-195]
- Line 105: Duplicate range [185-195]
- Line 107: Duplicate range [185-195]
- Line 109: Duplicate range [185-195]
- Line 111: Duplicate range [185-195]

---

### File: dynamic/commentary/01-07-02-01.txt

**Errors:**
- Line 33: Non-sequential range [72-91] - Start (72) < Previous start (78)
- Line 49: Non-sequential range [60-91] - Start (60) < Previous start (72)
- Line 9: Duplicate range [69-91]
- Line 11: Duplicate range [69-91]
- Line 13: Duplicate range [69-91]
- Line 15: Duplicate range [69-91]
- Line 19: Duplicate range [78-91]
- Line 21: Duplicate range [78-91]
- Line 23: Duplicate range [78-91]
- Line 25: Duplicate range [78-91]
- Line 27: Duplicate range [78-91]
- Line 29: Duplicate range [78-91]
- Line 31: Duplicate range [78-91]
- Line 35: Duplicate range [72-91]
- Line 37: Duplicate range [72-91]
- Line 39: Duplicate range [72-91]
- Line 41: Duplicate range [72-91]
- Line 43: Duplicate range [72-91]
- Line 45: Duplicate range [72-91]
- Line 47: Duplicate range [72-91]
- Line 51: Duplicate range [60-91]
- Line 53: Duplicate range [60-91]
- Line 55: Duplicate range [60-91]
- Line 57: Duplicate range [60-91]
- Line 59: Duplicate range [60-91]
- Line 61: Duplicate range [60-91]
- Line 63: Duplicate range [60-91]
- Line 67: Duplicate range [90-91]
- Line 69: Duplicate range [90-91]
- Line 71: Duplicate range [90-91]
- Line 73: Duplicate range [90-91]
- Line 75: Duplicate range [90-91]
- Line 77: Duplicate range [90-91]
- Line 79: Duplicate range [90-91]

---

### File: dynamic/commentary/01-07-03-01.txt

**Errors:**
- Line 17: Non-sequential range [66-96] - Start (66) < Previous start (82)
- Line 33: Non-sequential range [49-96] - Start (49) < Previous start (66)
- Line 15: Duplicate range [82-96]
- Line 19: Duplicate range [66-96]
- Line 21: Duplicate range [66-96]
- Line 23: Duplicate range [66-96]
- Line 25: Duplicate range [66-96]
- Line 27: Duplicate range [66-96]
- Line 29: Duplicate range [66-96]
- Line 31: Duplicate range [66-96]
- Line 35: Duplicate range [49-96]
- Line 37: Duplicate range [49-96]
- Line 39: Duplicate range [49-96]
- Line 41: Duplicate range [49-96]
- Line 43: Duplicate range [49-96]
- Line 45: Duplicate range [49-96]
- Line 47: Duplicate range [49-96]
- Line 51: Duplicate range [54-96]
- Line 53: Duplicate range [54-96]
- Line 55: Duplicate range [54-96]
- Line 57: Duplicate range [54-96]
- Line 59: Duplicate range [54-96]
- Line 61: Duplicate range [54-96]
- Line 63: Duplicate range [54-96]
- Line 67: Duplicate range [95-96]
- Line 69: Duplicate range [95-96]
- Line 71: Duplicate range [95-96]
- Line 73: Duplicate range [95-96]
- Line 75: Duplicate range [95-96]
- Line 77: Duplicate range [95-96]
- Line 79: Duplicate range [95-96]

---

### File: dynamic/commentary/01-07-04-01.txt

**Errors:**
- Line 139: Non-sequential range [360-365] - Start (360) < Previous start (376)
- Line 144: Non-sequential range [310-315] - Start (310) < Previous start (360)
- Line 149: Non-sequential range [230-235] - Start (230) < Previous start (310)
- Line 129: Duplicate range [356-385]

---

### File: dynamic/commentary/01-07-05-01.txt

**Errors:**
- Line 3: Duplicate range [1-1]
- Line 5: Duplicate range [1-1]
- Line 7: Duplicate range [1-1]
- Line 9: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]

---

### File: dynamic/commentary/01-08-01-01.txt

**Errors:**
- Line 39: Non-sequential range [50-76] - Start (50) < Previous start (66)
- Line 56: Non-sequential range [1-76] - Start (1) < Previous start (75)
- Line 28: Duplicate range [66-76]
- Line 31: Duplicate range [66-76]
- Line 36: Duplicate range [66-76]
- Line 44: Duplicate range [50-76]
- Line 50: Duplicate range [65-76]
- Line 61: Duplicate range [1-76]
- Line 63: Duplicate range [1-76]
- Line 65: Duplicate range [1-76]
- Line 67: Duplicate range [1-76]
- Line 69: Duplicate range [1-76]
- Line 71: Duplicate range [1-76]
- Line 73: Duplicate range [1-76]
- Line 75: Duplicate range [1-76]
- Line 77: Duplicate range [1-76]
- Line 79: Duplicate range [1-76]
- Line 81: Duplicate range [1-76]
- Line 83: Duplicate range [1-76]

---

### File: dynamic/commentary/01-08-04-01.txt

**Errors:**
- Line 6: Duplicate range [1-2]
- Line 11: Duplicate range [1-2]

---

### File: dynamic/commentary/01-08-04-02.txt

**Errors:**
- Line 24: Non-sequential range [22-33] - Start (22) < Previous start (30)
- Line 37: Duplicate range [25-33]
- Line 51: Duplicate range [33-33]

---

### File: dynamic/commentary/01-08-06-01.txt

**Errors:**
- Line 23: Non-sequential range [1-6] - Start (1) < Previous start (7)
- Line 33: Duplicate range [1-7]

---

### File: dynamic/commentary/01-08-07-01.txt

**Errors:**
- Line 256: Non-sequential range [530-535] - Start (530) < Previous start (550)
- Line 261: Non-sequential range [493-498] - Start (493) < Previous start (530)
- Line 266: Non-sequential range [436-441] - Start (436) < Previous start (493)
- Line 271: Non-sequential range [359-364] - Start (359) < Previous start (436)
- Line 276: Non-sequential range [1-552] - Start (1) < Previous start (359)
- Line 156: Duplicate range [533-552]
- Line 161: Duplicate range [533-552]
- Line 166: Duplicate range [533-552]
- Line 171: Duplicate range [533-552]
- Line 176: Duplicate range [533-552]
- Line 181: Duplicate range [533-552]
- Line 186: Duplicate range [533-552]
- Line 191: Duplicate range [533-552]
- Line 196: Duplicate range [533-552]
- Line 201: Duplicate range [533-552]
- Line 206: Duplicate range [533-552]
- Line 211: Duplicate range [533-552]
- Line 216: Duplicate range [533-552]
- Line 221: Duplicate range [533-552]
- Line 226: Duplicate range [533-552]
- Line 231: Duplicate range [533-552]
- Line 236: Duplicate range [533-552]
- Line 241: Duplicate range [533-552]
- Line 246: Duplicate range [533-552]
- Line 281: Duplicate range [1-552]
- Line 286: Duplicate range [1-552]
- Line 291: Duplicate range [1-552]
- Line 296: Duplicate range [1-552]
- Line 301: Duplicate range [1-552]
- Line 306: Duplicate range [1-552]
- Line 311: Duplicate range [1-552]
- Line 316: Duplicate range [1-552]
- Line 321: Duplicate range [1-552]
- Line 326: Duplicate range [1-552]
- Line 331: Duplicate range [1-552]
- Line 336: Duplicate range [1-552]
- Line 341: Duplicate range [1-552]
- Line 346: Duplicate range [1-552]
- Line 351: Duplicate range [1-552]
- Line 356: Duplicate range [1-552]
- Line 361: Duplicate range [1-552]
- Line 366: Duplicate range [1-552]
- Line 371: Duplicate range [1-552]
- Line 376: Duplicate range [1-552]
- Line 381: Duplicate range [1-552]
- Line 386: Duplicate range [1-552]
- Line 391: Duplicate range [1-552]
- Line 396: Duplicate range [1-552]
- Line 401: Duplicate range [1-552]
- Line 406: Duplicate range [1-552]
- Line 411: Duplicate range [1-552]
- Line 416: Duplicate range [1-552]
- Line 421: Duplicate range [1-552]
- Line 426: Duplicate range [1-552]
- Line 431: Duplicate range [1-552]
- Line 436: Duplicate range [1-552]
- Line 441: Duplicate range [1-552]
- Line 446: Duplicate range [1-552]
- Line 451: Duplicate range [1-552]
- Line 456: Duplicate range [1-552]
- Line 461: Duplicate range [1-552]
- Line 466: Duplicate range [1-552]
- Line 471: Duplicate range [1-552]
- Line 476: Duplicate range [1-552]
- Line 481: Duplicate range [1-552]
- Line 486: Duplicate range [1-552]
- Line 489: Duplicate range [1-552]
- Line 494: Duplicate range [1-552]
- Line 497: Duplicate range [1-552]
- Line 499: Duplicate range [1-552]

---

### File: dynamic/commentary/01-08-08-01.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 10: Duplicate range [1-1]
- Line 14: Duplicate range [1-1]
- Line 18: Duplicate range [1-1]

---

### File: dynamic/commentary/01-09-01-01.txt

**Errors:**
- Line 210: Non-sequential range [1109-1143] - Start (1109) < Previous start (1126)
- Line 226: Non-sequential range [1131-1143] - Start (1131) < Previous start (1135)
- Line 237: Non-sequential range [1132-1143] - Start (1132) < Previous start (1136)
- Line 244: Non-sequential range [1126-1143] - Start (1126) < Previous start (1132)
- Line 258: Non-sequential range [1078-1143] - Start (1078) < Previous start (1133)
- Line 314: Non-sequential range [878-1143] - Start (878) < Previous start (1078)
- Line 436: Non-sequential range [1044-1143] - Start (1044) < Previous start (1143)
- Line 586: Non-sequential range [1044-1143] - Start (1044) < Previous start (1143)
- Line 829: Non-sequential range [478-1143] - Start (478) < Previous start (1044)
- Line 839: Non-sequential range [1134-1143] - Start (1134) < Previous start (1143)
- Line 853: Non-sequential range [1117-1143] - Start (1117) < Previous start (1134)
- Line 890: Non-sequential range [1120-1143] - Start (1120) < Previous start (1130)
- Line 903: Non-sequential range [1114-1143] - Start (1114) < Previous start (1138)
- Line 927: Non-sequential range [844-1143] - Start (844) < Previous start (1114)
- Line 954: Non-sequential range [844-1143] - Start (844) < Previous start (1143)
- Line 1108: Non-sequential range [844-1143] - Start (844) < Previous start (1143)
- Line 244: Duplicate range [1126-1143]
- Line 264: Duplicate range [1078-1143]
- Line 270: Duplicate range [1078-1143]
- Line 276: Duplicate range [1078-1143]
- Line 282: Duplicate range [1078-1143]
- Line 288: Duplicate range [1078-1143]
- Line 293: Duplicate range [1078-1143]
- Line 298: Duplicate range [1078-1143]
- Line 303: Duplicate range [1078-1143]
- Line 308: Duplicate range [1078-1143]
- Line 320: Duplicate range [878-1143]
- Line 324: Duplicate range [878-1143]
- Line 330: Duplicate range [878-1143]
- Line 336: Duplicate range [878-1143]
- Line 341: Duplicate range [878-1143]
- Line 346: Duplicate range [878-1143]
- Line 352: Duplicate range [878-1143]
- Line 357: Duplicate range [878-1143]
- Line 363: Duplicate range [878-1143]
- Line 369: Duplicate range [878-1143]
- Line 375: Duplicate range [878-1143]
- Line 381: Duplicate range [878-1143]
- Line 387: Duplicate range [878-1143]
- Line 393: Duplicate range [878-1143]
- Line 399: Duplicate range [878-1143]
- Line 405: Duplicate range [878-1143]
- Line 411: Duplicate range [878-1143]
- Line 417: Duplicate range [878-1143]
- Line 420: Duplicate range [878-1143]
- Line 427: Duplicate range [878-1143]
- Line 443: Duplicate range [1044-1143]
- Line 450: Duplicate range [1044-1143]
- Line 456: Duplicate range [1044-1143]
- Line 462: Duplicate range [1044-1143]
- Line 468: Duplicate range [1044-1143]
- Line 475: Duplicate range [1044-1143]
- Line 481: Duplicate range [1044-1143]
- Line 487: Duplicate range [1044-1143]
- Line 493: Duplicate range [1044-1143]
- Line 501: Duplicate range [1044-1143]
- Line 506: Duplicate range [1044-1143]
- Line 512: Duplicate range [1044-1143]
- Line 518: Duplicate range [1044-1143]
- Line 524: Duplicate range [1044-1143]
- Line 530: Duplicate range [1044-1143]
- Line 536: Duplicate range [1044-1143]
- Line 542: Duplicate range [1044-1143]
- Line 548: Duplicate range [1044-1143]
- Line 554: Duplicate range [1044-1143]
- Line 560: Duplicate range [1044-1143]
- Line 566: Duplicate range [1044-1143]
- Line 576: Duplicate range [1044-1143]
- Line 583: Duplicate range [1143-1143]
- Line 586: Duplicate range [1044-1143]
- Line 599: Duplicate range [1044-1143]
- Line 606: Duplicate range [1044-1143]
- Line 612: Duplicate range [1044-1143]
- Line 618: Duplicate range [1044-1143]
- Line 624: Duplicate range [1044-1143]
- Line 630: Duplicate range [1044-1143]
- Line 636: Duplicate range [1044-1143]
- Line 642: Duplicate range [1044-1143]
- Line 653: Duplicate range [1044-1143]
- Line 659: Duplicate range [1044-1143]
- Line 665: Duplicate range [1044-1143]
- Line 671: Duplicate range [1044-1143]
- Line 677: Duplicate range [1044-1143]
- Line 683: Duplicate range [1044-1143]
- Line 689: Duplicate range [1044-1143]
- Line 695: Duplicate range [1044-1143]
- Line 701: Duplicate range [1044-1143]
- Line 707: Duplicate range [1044-1143]
- Line 713: Duplicate range [1044-1143]
- Line 719: Duplicate range [1044-1143]
- Line 725: Duplicate range [1044-1143]
- Line 739: Duplicate range [1044-1143]
- Line 745: Duplicate range [1044-1143]
- Line 751: Duplicate range [1044-1143]
- Line 757: Duplicate range [1044-1143]
- Line 763: Duplicate range [1044-1143]
- Line 769: Duplicate range [1044-1143]
- Line 775: Duplicate range [1044-1143]
- Line 780: Duplicate range [1044-1143]
- Line 785: Duplicate range [1044-1143]
- Line 790: Duplicate range [1044-1143]
- Line 797: Duplicate range [1044-1143]
- Line 804: Duplicate range [1044-1143]
- Line 810: Duplicate range [1044-1143]
- Line 816: Duplicate range [1044-1143]
- Line 821: Duplicate range [1044-1143]
- Line 836: Duplicate range [1143-1143]
- Line 846: Duplicate range [1134-1143]
- Line 861: Duplicate range [1117-1143]
- Line 883: Duplicate range [1130-1143]
- Line 914: Duplicate range [1114-1143]
- Line 921: Duplicate range [1114-1143]
- Line 933: Duplicate range [844-1143]
- Line 938: Duplicate range [844-1143]
- Line 945: Duplicate range [844-1143]
- Line 951: Duplicate range [1143-1143]
- Line 954: Duplicate range [844-1143]
- Line 962: Duplicate range [844-1143]
- Line 969: Duplicate range [844-1143]
- Line 975: Duplicate range [844-1143]
- Line 981: Duplicate range [844-1143]
- Line 988: Duplicate range [844-1143]
- Line 995: Duplicate range [844-1143]
- Line 1001: Duplicate range [844-1143]
- Line 1007: Duplicate range [844-1143]
- Line 1012: Duplicate range [844-1143]
- Line 1017: Duplicate range [844-1143]
- Line 1022: Duplicate range [844-1143]
- Line 1026: Duplicate range [844-1143]
- Line 1032: Duplicate range [844-1143]
- Line 1037: Duplicate range [844-1143]
- Line 1043: Duplicate range [844-1143]
- Line 1049: Duplicate range [844-1143]
- Line 1055: Duplicate range [844-1143]
- Line 1061: Duplicate range [844-1143]
- Line 1067: Duplicate range [844-1143]
- Line 1073: Duplicate range [844-1143]
- Line 1079: Duplicate range [844-1143]
- Line 1085: Duplicate range [844-1143]
- Line 1094: Duplicate range [844-1143]
- Line 1100: Duplicate range [1143-1143]
- Line 1108: Duplicate range [844-1143]
- Line 1114: Duplicate range [844-1143]
- Line 1120: Duplicate range [844-1143]
- Line 1127: Duplicate range [844-1143]
- Line 1133: Duplicate range [844-1143]
- Line 1139: Duplicate range [844-1143]
- Line 1146: Duplicate range [844-1143]
- Line 1152: Duplicate range [844-1143]
- Line 1157: Duplicate range [844-1143]
- Line 1164: Duplicate range [844-1143]
- Line 1170: Duplicate range [844-1143]
- Line 1176: Duplicate range [844-1143]
- Line 1183: Duplicate range [844-1143]
- Line 1189: Duplicate range [844-1143]
- Line 1195: Duplicate range [844-1143]
- Line 1202: Duplicate range [844-1143]
- Line 1208: Duplicate range [844-1143]
- Line 1214: Duplicate range [844-1143]
- Line 1221: Duplicate range [844-1143]
- Line 1227: Duplicate range [844-1143]
- Line 1233: Duplicate range [844-1143]
- Line 1240: Duplicate range [844-1143]
- Line 1246: Duplicate range [844-1143]
- Line 1252: Duplicate range [844-1143]
- Line 1259: Duplicate range [844-1143]
- Line 1265: Duplicate range [844-1143]
- Line 1271: Duplicate range [844-1143]
- Line 1278: Duplicate range [844-1143]
- Line 1284: Duplicate range [844-1143]
- Line 1290: Duplicate range [844-1143]
- Line 1297: Duplicate range [844-1143]
- Line 1303: Duplicate range [844-1143]
- Line 1309: Duplicate range [844-1143]
- Line 1316: Duplicate range [844-1143]
- Line 1322: Duplicate range [844-1143]
- Line 1328: Duplicate range [844-1143]
- Line 1335: Duplicate range [844-1143]
- Line 1341: Duplicate range [844-1143]
- Line 1347: Duplicate range [844-1143]
- Line 1354: Duplicate range [844-1143]
- Line 1360: Duplicate range [844-1143]
- Line 1365: Duplicate range [844-1143]
- Line 1372: Duplicate range [844-1143]
- Line 1378: Duplicate range [844-1143]
- Line 1384: Duplicate range [844-1143]
- Line 1391: Duplicate range [844-1143]
- Line 1397: Duplicate range [844-1143]
- Line 1403: Duplicate range [844-1143]
- Line 1410: Duplicate range [844-1143]
- Line 1416: Duplicate range [844-1143]
- Line 1422: Duplicate range [844-1143]
- Line 1429: Duplicate range [844-1143]
- Line 1435: Duplicate range [844-1143]
- Line 1441: Duplicate range [844-1143]
- Line 1448: Duplicate range [844-1143]
- Line 1454: Duplicate range [844-1143]
- Line 1460: Duplicate range [844-1143]
- Line 1467: Duplicate range [844-1143]
- Line 1473: Duplicate range [844-1143]
- Line 1479: Duplicate range [844-1143]
- Line 1486: Duplicate range [844-1143]
- Line 1492: Duplicate range [844-1143]
- Line 1498: Duplicate range [844-1143]
- Line 1505: Duplicate range [844-1143]
- Line 1511: Duplicate range [844-1143]
- Line 1516: Duplicate range [844-1143]
- Line 1523: Duplicate range [844-1143]
- Line 1529: Duplicate range [844-1143]
- Line 1534: Duplicate range [844-1143]
- Line 1541: Duplicate range [844-1143]
- Line 1547: Duplicate range [844-1143]
- Line 1553: Duplicate range [844-1143]
- Line 1560: Duplicate range [844-1143]
- Line 1566: Duplicate range [844-1143]
- Line 1572: Duplicate range [844-1143]
- Line 1579: Duplicate range [844-1143]
- Line 1585: Duplicate range [844-1143]
- Line 1591: Duplicate range [844-1143]
- Line 1598: Duplicate range [844-1143]
- Line 1604: Duplicate range [844-1143]
- Line 1610: Duplicate range [844-1143]
- Line 1617: Duplicate range [844-1143]
- Line 1623: Duplicate range [844-1143]
- Line 1629: Duplicate range [844-1143]
- Line 1636: Duplicate range [844-1143]
- Line 1642: Duplicate range [844-1143]
- Line 1648: Duplicate range [844-1143]
- Line 1655: Duplicate range [844-1143]
- Line 1661: Duplicate range [844-1143]
- Line 1667: Duplicate range [844-1143]
- Line 1672: Duplicate range [844-1143]
- Line 1679: Duplicate range [844-1143]
- Line 1684: Duplicate range [844-1143]
- Line 1690: Duplicate range [844-1143]
- Line 1696: Duplicate range [1143-1143]

---

### File: dynamic/commentary/01-10-01-01.txt

**Errors:**
- Line 185: Non-sequential range [552-557] - Start (552) < Previous start (602)
- Line 191: Non-sequential range [455-460] - Start (455) < Previous start (552)
- Line 197: Non-sequential range [308-313] - Start (308) < Previous start (455)
- Line 204: Non-sequential range [111-116] - Start (111) < Previous start (308)
- Line 210: Non-sequential range [1-604] - Start (1) < Previous start (111)
- Line 216: Duplicate range [1-604]
- Line 222: Duplicate range [1-604]
- Line 229: Duplicate range [1-604]
- Line 245: Duplicate range [1-604]
- Line 255: Duplicate range [1-604]
- Line 267: Duplicate range [1-604]
- Line 274: Duplicate range [1-604]
- Line 282: Duplicate range [1-604]
- Line 288: Duplicate range [1-604]
- Line 294: Duplicate range [1-604]
- Line 301: Duplicate range [1-604]
- Line 319: Duplicate range [1-604]
- Line 366: Duplicate range [1-604]
- Line 439: Duplicate range [1-604]
- Line 467: Duplicate range [1-604]
- Line 493: Duplicate range [1-604]

---

### File: dynamic/commentary/01-11-01-01.txt

**Errors:**
- Line 272: Non-sequential range [314-328] - Start (314) < Previous start (319)
- Line 311: Non-sequential range [315-328] - Start (315) < Previous start (318)
- Line 324: Non-sequential range [314-328] - Start (314) < Previous start (315)
- Line 337: Non-sequential range [313-328] - Start (313) < Previous start (314)
- Line 363: Non-sequential range [309-328] - Start (309) < Previous start (317)
- Line 249: Duplicate range [319-328]
- Line 259: Duplicate range [319-328]
- Line 262: Duplicate range [319-328]
- Line 272: Duplicate range [314-328]
- Line 287: Duplicate range [318-328]
- Line 297: Duplicate range [318-328]
- Line 300: Duplicate range [318-328]
- Line 314: Duplicate range [315-328]
- Line 324: Duplicate range [314-328]
- Line 327: Duplicate range [314-328]
- Line 340: Duplicate range [313-328]
- Line 353: Duplicate range [317-328]
- Line 366: Duplicate range [309-328]
- Line 380: Duplicate range [316-328]
- Line 390: Duplicate range [316-328]
- Line 393: Duplicate range [316-328]

---

### File: dynamic/commentary/01-12-01-01.txt

**Errors:**
- Line 102: Non-sequential range [669-674] - Start (669) < Previous start (671)
- Line 108: Non-sequential range [596-601] - Start (596) < Previous start (669)
- Line 114: Non-sequential range [473-478] - Start (473) < Previous start (596)
- Line 120: Non-sequential range [300-305] - Start (300) < Previous start (473)
- Line 127: Non-sequential range [77-82] - Start (77) < Previous start (300)
- Line 133: Non-sequential range [1-697] - Start (1) < Previous start (77)
- Line 140: Duplicate range [1-697]
- Line 147: Duplicate range [1-697]
- Line 154: Duplicate range [1-697]
- Line 160: Duplicate range [1-697]
- Line 167: Duplicate range [1-697]
- Line 180: Duplicate range [1-697]
- Line 187: Duplicate range [1-697]
- Line 193: Duplicate range [1-697]
- Line 200: Duplicate range [1-697]
- Line 206: Duplicate range [1-697]
- Line 213: Duplicate range [1-697]
- Line 219: Duplicate range [1-697]
- Line 226: Duplicate range [1-697]
- Line 233: Duplicate range [1-697]
- Line 240: Duplicate range [1-697]
- Line 246: Duplicate range [1-697]
- Line 252: Duplicate range [1-697]
- Line 265: Duplicate range [1-697]
- Line 276: Duplicate range [1-697]
- Line 286: Duplicate range [1-697]
- Line 297: Duplicate range [1-697]
- Line 304: Duplicate range [1-697]
- Line 311: Duplicate range [1-697]
- Line 318: Duplicate range [1-697]
- Line 324: Duplicate range [1-697]
- Line 331: Duplicate range [1-697]
- Line 338: Duplicate range [1-697]
- Line 352: Duplicate range [1-697]
- Line 377: Duplicate range [1-697]
- Line 387: Duplicate range [1-697]
- Line 399: Duplicate range [1-697]
- Line 406: Duplicate range [1-697]
- Line 413: Duplicate range [1-697]
- Line 418: Duplicate range [1-697]
- Line 424: Duplicate range [1-697]
- Line 429: Duplicate range [1-697]
- Line 435: Duplicate range [1-697]
- Line 440: Duplicate range [1-697]
- Line 446: Duplicate range [1-697]
- Line 452: Duplicate range [1-697]
- Line 474: Duplicate range [1-697]
- Line 488: Duplicate range [1-697]
- Line 516: Duplicate range [1-697]
- Line 561: Duplicate range [1-697]
- Line 604: Duplicate range [1-697]
- Line 691: Duplicate range [1-697]

---

### File: dynamic/commentary/01-12-02-01.txt

**Errors:**
- Line 98: Non-sequential range [1-287] - Start (1) < Previous start (287)
- Line 79: Duplicate range [273-287]
- Line 100: Duplicate range [1-287]
- Line 102: Duplicate range [1-287]
- Line 104: Duplicate range [1-287]
- Line 106: Duplicate range [1-287]
- Line 108: Duplicate range [1-287]
- Line 110: Duplicate range [1-287]
- Line 112: Duplicate range [1-287]
- Line 114: Duplicate range [1-287]
- Line 116: Duplicate range [1-287]
- Line 120: Duplicate range [1-287]

---

### File: dynamic/commentary/01-12-05-01.txt

**Errors:**
- Line 65: Non-sequential range [196-214] - Start (196) < Previous start (205)
- Line 81: Non-sequential range [197-214] - Start (197) < Previous start (207)
- Line 89: Non-sequential range [191-214] - Start (191) < Previous start (197)
- Line 111: Non-sequential range [198-214] - Start (198) < Previous start (208)
- Line 119: Non-sequential range [191-214] - Start (191) < Previous start (198)
- Line 135: Non-sequential range [1-214] - Start (1) < Previous start (197)
- Line 63: Duplicate range [205-214]
- Line 67: Duplicate range [196-214]
- Line 69: Duplicate range [196-214]
- Line 71: Duplicate range [196-214]
- Line 75: Duplicate range [207-214]
- Line 79: Duplicate range [207-214]
- Line 83: Duplicate range [197-214]
- Line 87: Duplicate range [197-214]
- Line 91: Duplicate range [191-214]
- Line 93: Duplicate range [191-214]
- Line 95: Duplicate range [191-214]
- Line 97: Duplicate range [197-214]
- Line 99: Duplicate range [197-214]
- Line 101: Duplicate range [197-214]
- Line 105: Duplicate range [208-214]
- Line 109: Duplicate range [208-214]
- Line 113: Duplicate range [198-214]
- Line 115: Duplicate range [198-214]
- Line 119: Duplicate range [191-214]
- Line 121: Duplicate range [191-214]
- Line 123: Duplicate range [191-214]
- Line 125: Duplicate range [191-214]
- Line 127: Duplicate range [197-214]
- Line 129: Duplicate range [197-214]
- Line 131: Duplicate range [197-214]
- Line 133: Duplicate range [197-214]
- Line 137: Duplicate range [1-214]
- Line 139: Duplicate range [1-214]
- Line 141: Duplicate range [1-214]
- Line 143: Duplicate range [1-214]
- Line 145: Duplicate range [1-214]
- Line 147: Duplicate range [1-214]
- Line 149: Duplicate range [1-214]
- Line 151: Duplicate range [1-214]
- Line 153: Duplicate range [1-214]
- Line 155: Duplicate range [1-214]
- Line 157: Duplicate range [1-214]
- Line 159: Duplicate range [1-214]
- Line 161: Duplicate range [1-214]
- Line 163: Duplicate range [1-214]
- Line 165: Duplicate range [1-214]
- Line 167: Duplicate range [1-214]
- Line 169: Duplicate range [1-214]
- Line 171: Duplicate range [1-214]
- Line 173: Duplicate range [1-214]
- Line 177: Duplicate range [1-214]

---

### File: dynamic/commentary/01-12-05-02.txt

**Errors:**
- Line 39: Non-sequential range [122-140] - Start (122) < Previous start (136)
- Line 58: Non-sequential range [1-140] - Start (1) < Previous start (140)
- Line 55: Duplicate range [140-140]
- Line 60: Duplicate range [1-140]
- Line 62: Duplicate range [1-140]
- Line 64: Duplicate range [1-140]
- Line 66: Duplicate range [1-140]
- Line 68: Duplicate range [1-140]
- Line 70: Duplicate range [1-140]
- Line 72: Duplicate range [1-140]
- Line 74: Duplicate range [1-140]
- Line 76: Duplicate range [1-140]
- Line 78: Duplicate range [1-140]
- Line 80: Duplicate range [1-140]
- Line 82: Duplicate range [1-140]
- Line 84: Duplicate range [1-140]

---

### File: dynamic/commentary/01-12-06-01.txt

**Errors:**
- Line 8: Duplicate range [1-9]
- Line 13: Duplicate range [1-9]

---

### File: dynamic/commentary/01-12-07-01.txt

**Errors:**
- Line 65: Non-sequential range [227-247] - Start (227) < Previous start (228)

---

### File: dynamic/commentary/01-13-01-01.txt

**Errors:**
- Line 70: Non-sequential range [240-249] - Start (240) < Previous start (245)
- Line 80: Non-sequential range [167-172] - Start (167) < Previous start (244)
- Line 87: Non-sequential range [20-25] - Start (20) < Previous start (167)
- Line 90: Non-sequential range [1-249] - Start (1) < Previous start (20)
- Line 102: Duplicate range [1-249]
- Line 105: Duplicate range [1-249]
- Line 124: Duplicate range [1-249]

---

### File: dynamic/commentary/01-13-03-01.txt

**Errors:**
- Line 50: Non-sequential range [229-286] - Start (229) < Previous start (253)
- Line 62: Non-sequential range [137-142] - Start (137) < Previous start (249)
- Line 65: Non-sequential range [1-286] - Start (1) < Previous start (137)
- Line 79: Duplicate range [1-286]
- Line 82: Duplicate range [1-286]
- Line 98: Duplicate range [1-286]
- Line 112: Duplicate range [1-286]
- Line 115: Duplicate range [1-286]
- Line 118: Duplicate range [1-286]
- Line 121: Duplicate range [1-286]
- Line 124: Duplicate range [1-286]
- Line 127: Duplicate range [1-286]
- Line 130: Duplicate range [1-286]
- Line 133: Duplicate range [1-286]
- Line 136: Duplicate range [1-286]
- Line 139: Duplicate range [1-286]
- Line 142: Duplicate range [1-286]
- Line 145: Duplicate range [1-286]

---

### File: dynamic/commentary/01-13-04-01.txt

**Errors:**
- Line 37: Non-sequential range [90-97] - Start (90) < Previous start (92)
- Line 47: Non-sequential range [91-97] - Start (91) < Previous start (92)
- Line 53: Non-sequential range [89-97] - Start (89) < Previous start (93)
- Line 35: Duplicate range [92-97]
- Line 39: Duplicate range [90-97]
- Line 43: Duplicate range [91-97]
- Line 45: Duplicate range [92-97]
- Line 47: Duplicate range [91-97]
- Line 49: Duplicate range [91-97]
- Line 55: Duplicate range [89-97]

---

### File: dynamic/commentary/01-13-05-01.txt

**Errors:**
- Line 120: Non-sequential range [201-206] - Start (201) < Previous start (203)

---

### File: dynamic/commentary/01-14-01-01.txt

**Errors:**
- Line 57: Non-sequential range [82-87] - Start (82) < Previous start (137)
- Line 60: Non-sequential range [1-163] - Start (1) < Previous start (82)

---

### File: dynamic/commentary/01-14-02-01.txt

**Errors:**
- Line 146: Duplicate range [331-359]

---

### File: dynamic/commentary/01-14-04-01.txt

**Errors:**
- Line 150: Non-sequential range [309-314] - Start (309) < Previous start (330)
- Line 162: Non-sequential range [268-273] - Start (268) < Previous start (309)
- Line 175: Non-sequential range [197-202] - Start (197) < Previous start (268)
- Line 180: Non-sequential range [96-101] - Start (96) < Previous start (197)
- Line 197: Non-sequential range [1-336] - Start (1) < Previous start (96)
- Line 202: Duplicate range [1-336]
- Line 207: Duplicate range [1-336]
- Line 212: Duplicate range [1-336]
- Line 217: Duplicate range [1-336]
- Line 230: Duplicate range [1-336]
- Line 239: Duplicate range [1-336]
- Line 244: Duplicate range [1-336]

---

### File: dynamic/commentary/01-14-05-01.txt

**Errors:**
- Line 146: Non-sequential range [473-693] - Start (473) < Previous start (501)
- Line 161: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 181: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 191: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 206: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 241: Non-sequential range [473-693] - Start (473) < Previous start (673)
- Line 251: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 261: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 266: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 271: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 276: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 281: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 296: Non-sequential range [682-693] - Start (682) < Previous start (689)
- Line 306: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 311: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 316: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 321: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 326: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 336: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 346: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 351: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 356: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 361: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 366: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 381: Non-sequential range [682-693] - Start (682) < Previous start (689)
- Line 391: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 396: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 401: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 406: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 411: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 426: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 436: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 441: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 446: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 451: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 456: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 471: Non-sequential range [682-693] - Start (682) < Previous start (689)
- Line 481: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 486: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 491: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 496: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 501: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 516: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 526: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 531: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 536: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 541: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 546: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 561: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 571: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 576: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 581: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 586: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 591: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 606: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 616: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 621: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 626: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 631: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 636: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 651: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 661: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 666: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 671: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 676: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 681: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 696: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 706: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 711: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 716: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 721: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 726: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 741: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 751: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 756: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 761: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 766: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 771: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 786: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 796: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 801: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 806: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 811: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 816: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 831: Non-sequential range [682-693] - Start (682) < Previous start (683)
- Line 841: Non-sequential range [676-693] - Start (676) < Previous start (683)
- Line 846: Non-sequential range [673-693] - Start (673) < Previous start (676)
- Line 851: Non-sequential range [668-693] - Start (668) < Previous start (673)
- Line 856: Non-sequential range [558-693] - Start (558) < Previous start (668)
- Line 861: Non-sequential range [473-693] - Start (473) < Previous start (558)
- Line 156: Duplicate range [683-693]
- Line 166: Duplicate range [682-693]
- Line 171: Duplicate range [683-693]
- Line 176: Duplicate range [683-693]
- Line 186: Duplicate range [676-693]
- Line 196: Duplicate range [673-693]
- Line 201: Duplicate range [673-693]
- Line 211: Duplicate range [668-693]
- Line 216: Duplicate range [668-693]
- Line 221: Duplicate range [668-693]
- Line 226: Duplicate range [673-693]
- Line 231: Duplicate range [673-693]
- Line 236: Duplicate range [673-693]
- Line 241: Duplicate range [473-693]
- Line 246: Duplicate range [683-693]
- Line 251: Duplicate range [682-693]
- Line 256: Duplicate range [683-693]
- Line 261: Duplicate range [676-693]
- Line 266: Duplicate range [673-693]
- Line 271: Duplicate range [668-693]
- Line 281: Duplicate range [473-693]
- Line 296: Duplicate range [682-693]
- Line 301: Duplicate range [683-693]
- Line 306: Duplicate range [676-693]
- Line 311: Duplicate range [673-693]
- Line 316: Duplicate range [668-693]
- Line 321: Duplicate range [558-693]
- Line 326: Duplicate range [473-693]
- Line 331: Duplicate range [683-693]
- Line 336: Duplicate range [682-693]
- Line 341: Duplicate range [683-693]
- Line 346: Duplicate range [676-693]
- Line 351: Duplicate range [673-693]
- Line 356: Duplicate range [668-693]
- Line 361: Duplicate range [558-693]
- Line 366: Duplicate range [473-693]
- Line 371: Duplicate range [688-693]
- Line 376: Duplicate range [689-693]
- Line 381: Duplicate range [682-693]
- Line 386: Duplicate range [683-693]
- Line 391: Duplicate range [676-693]
- Line 396: Duplicate range [673-693]
- Line 401: Duplicate range [668-693]
- Line 406: Duplicate range [558-693]
- Line 411: Duplicate range [473-693]
- Line 416: Duplicate range [473-693]
- Line 421: Duplicate range [683-693]
- Line 426: Duplicate range [682-693]
- Line 431: Duplicate range [683-693]
- Line 436: Duplicate range [676-693]
- Line 441: Duplicate range [673-693]
- Line 446: Duplicate range [668-693]
- Line 451: Duplicate range [558-693]
- Line 456: Duplicate range [473-693]
- Line 461: Duplicate range [688-693]
- Line 466: Duplicate range [689-693]
- Line 471: Duplicate range [682-693]
- Line 476: Duplicate range [683-693]
- Line 481: Duplicate range [676-693]
- Line 486: Duplicate range [673-693]
- Line 491: Duplicate range [668-693]
- Line 496: Duplicate range [558-693]
- Line 501: Duplicate range [473-693]
- Line 506: Duplicate range [473-693]
- Line 511: Duplicate range [683-693]
- Line 516: Duplicate range [682-693]
- Line 521: Duplicate range [683-693]
- Line 526: Duplicate range [676-693]
- Line 531: Duplicate range [673-693]
- Line 536: Duplicate range [668-693]
- Line 541: Duplicate range [558-693]
- Line 546: Duplicate range [473-693]
- Line 551: Duplicate range [473-693]
- Line 556: Duplicate range [683-693]
- Line 561: Duplicate range [682-693]
- Line 566: Duplicate range [683-693]
- Line 571: Duplicate range [676-693]
- Line 576: Duplicate range [673-693]
- Line 581: Duplicate range [668-693]
- Line 586: Duplicate range [558-693]
- Line 591: Duplicate range [473-693]
- Line 596: Duplicate range [473-693]
- Line 601: Duplicate range [683-693]
- Line 606: Duplicate range [682-693]
- Line 611: Duplicate range [683-693]
- Line 616: Duplicate range [676-693]
- Line 621: Duplicate range [673-693]
- Line 626: Duplicate range [668-693]
- Line 631: Duplicate range [558-693]
- Line 636: Duplicate range [473-693]
- Line 641: Duplicate range [473-693]
- Line 646: Duplicate range [683-693]
- Line 651: Duplicate range [682-693]
- Line 656: Duplicate range [683-693]
- Line 661: Duplicate range [676-693]
- Line 666: Duplicate range [673-693]
- Line 671: Duplicate range [668-693]
- Line 676: Duplicate range [558-693]
- Line 681: Duplicate range [473-693]
- Line 686: Duplicate range [473-693]
- Line 691: Duplicate range [683-693]
- Line 696: Duplicate range [682-693]
- Line 701: Duplicate range [683-693]
- Line 706: Duplicate range [676-693]
- Line 711: Duplicate range [673-693]
- Line 716: Duplicate range [668-693]
- Line 721: Duplicate range [558-693]
- Line 726: Duplicate range [473-693]
- Line 731: Duplicate range [473-693]
- Line 736: Duplicate range [683-693]
- Line 741: Duplicate range [682-693]
- Line 746: Duplicate range [683-693]
- Line 751: Duplicate range [676-693]
- Line 756: Duplicate range [673-693]
- Line 761: Duplicate range [668-693]
- Line 766: Duplicate range [558-693]
- Line 771: Duplicate range [473-693]
- Line 776: Duplicate range [473-693]
- Line 781: Duplicate range [683-693]
- Line 786: Duplicate range [682-693]
- Line 791: Duplicate range [683-693]
- Line 796: Duplicate range [676-693]
- Line 801: Duplicate range [673-693]
- Line 806: Duplicate range [668-693]
- Line 811: Duplicate range [558-693]
- Line 816: Duplicate range [473-693]
- Line 821: Duplicate range [473-693]
- Line 826: Duplicate range [683-693]
- Line 831: Duplicate range [682-693]
- Line 836: Duplicate range [683-693]
- Line 841: Duplicate range [676-693]
- Line 846: Duplicate range [673-693]
- Line 851: Duplicate range [668-693]
- Line 856: Duplicate range [558-693]
- Line 861: Duplicate range [473-693]
- Line 866: Duplicate range [473-693]
- Line 871: Duplicate range [473-693]
- Line 874: Duplicate range [473-693]
- Line 875: Duplicate range [473-693]

---

### File: dynamic/commentary/01-14-06-01.txt

**Errors:**
- Line 46: Non-sequential range [76-101] - Start (76) < Previous start (82)
- Line 62: Non-sequential range [76-101] - Start (76) < Previous start (81)
- Line 62: Duplicate range [76-101]
- Line 69: Duplicate range [81-101]
- Line 90: Duplicate range [101-101]
- Line 94: Duplicate range [101-101]

---

### File: dynamic/commentary/01-14-07-01.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 15: Duplicate range [1-1]
- Line 19: Duplicate range [1-1]

---

### File: dynamic/commentary/01-14-07-02.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 15: Duplicate range [1-1]
- Line 19: Duplicate range [1-1]

---

### File: dynamic/commentary/01-14-07-03.txt

**Errors:**
- Line 10: Duplicate range [1-15]
- Line 15: Duplicate range [1-15]

---

### File: dynamic/commentary/01-14-08-01.txt

**Errors:**
- Line 67: Duplicate range [191-216]
- Line 78: Duplicate range [191-216]

---

### File: dynamic/commentary/01-14-09-01.txt

**Errors:**
- Line 131: Non-sequential range [297-302] - Start (297) < Previous start (305)
- Line 137: Non-sequential range [251-256] - Start (251) < Previous start (297)
- Line 143: Non-sequential range [175-180] - Start (175) < Previous start (251)
- Line 150: Non-sequential range [49-54] - Start (49) < Previous start (175)
- Line 163: Non-sequential range [1-318] - Start (1) < Previous start (49)
- Line 168: Duplicate range [1-318]
- Line 173: Duplicate range [1-318]
- Line 190: Duplicate range [1-318]
- Line 195: Duplicate range [1-318]
- Line 200: Duplicate range [1-318]
- Line 210: Duplicate range [1-318]
- Line 219: Duplicate range [1-318]

---

### File: dynamic/commentary/01-14-10-01.txt

**Errors:**
- Line 95: Non-sequential range [1-172] - Start (1) < Previous start (172)
- Line 51: Duplicate range [147-172]
- Line 60: Duplicate range [147-172]
- Line 69: Duplicate range [147-172]
- Line 82: Duplicate range [172-172]
- Line 85: Duplicate range [172-172]
- Line 97: Duplicate range [1-172]
- Line 99: Duplicate range [1-172]
- Line 101: Duplicate range [1-172]
- Line 103: Duplicate range [1-172]
- Line 105: Duplicate range [1-172]
- Line 107: Duplicate range [1-172]
- Line 109: Duplicate range [1-172]
- Line 111: Duplicate range [1-172]
- Line 113: Duplicate range [1-172]
- Line 115: Duplicate range [1-172]
- Line 117: Duplicate range [1-172]

---

### File: dynamic/commentary/01-14-11-01.txt

**Errors:**
- Line 31: Non-sequential range [40-65] - Start (40) < Previous start (44)
- Line 49: Duplicate range [65-65]
- Line 56: Duplicate range [65-65]
- Line 65: Duplicate range [65-65]
- Line 68: Duplicate range [65-65]
- Line 73: Duplicate range [65-65]

---

### File: dynamic/commentary/01-14-12-01.txt

**Errors:**
- Line 42: Duplicate range [53-73]
- Line 60: Duplicate range [73-73]
- Line 69: Duplicate range [73-73]
- Line 74: Duplicate range [73-73]
- Line 81: Duplicate range [73-73]
- Line 84: Duplicate range [73-73]

---

### File: dynamic/commentary/01-14-13-01.txt

**Errors:**
- Line 113: Non-sequential range [1-142] - Start (1) < Previous start (142)
- Line 49: Duplicate range [117-142]
- Line 54: Duplicate range [117-142]
- Line 78: Duplicate range [142-142]
- Line 89: Duplicate range [142-142]
- Line 98: Duplicate range [142-142]
- Line 103: Duplicate range [142-142]
- Line 110: Duplicate range [142-142]
- Line 115: Duplicate range [1-142]
- Line 117: Duplicate range [1-142]
- Line 119: Duplicate range [1-142]
- Line 121: Duplicate range [1-142]
- Line 123: Duplicate range [1-142]
- Line 125: Duplicate range [1-142]
- Line 127: Duplicate range [1-142]
- Line 131: Duplicate range [1-142]

---

### File: dynamic/commentary/02-15-01-01.txt

**Errors:**
- Line 4: Duplicate range [1-473]
- Line 9: Duplicate range [1-473]
- Line 12: Duplicate range [1-473]
- Line 15: Duplicate range [1-473]
- Line 20: Duplicate range [1-473]
- Line 25: Duplicate range [1-473]
- Line 28: Duplicate range [1-473]
- Line 33: Duplicate range [1-473]
- Line 42: Duplicate range [1-473]
- Line 45: Duplicate range [1-473]
- Line 50: Duplicate range [1-473]
- Line 57: Duplicate range [1-473]
- Line 64: Duplicate range [1-473]
- Line 77: Duplicate range [1-473]
- Line 82: Duplicate range [1-473]
- Line 87: Duplicate range [1-473]
- Line 94: Duplicate range [1-473]
- Line 101: Duplicate range [1-473]
- Line 118: Duplicate range [1-473]
- Line 129: Duplicate range [1-473]
- Line 146: Duplicate range [1-473]
- Line 165: Duplicate range [1-473]
- Line 184: Duplicate range [1-473]
- Line 193: Duplicate range [1-473]
- Line 211: Duplicate range [1-473]
- Line 238: Duplicate range [1-473]
- Line 246: Duplicate range [1-473]
- Line 269: Duplicate range [1-473]
- Line 293: Duplicate range [1-473]
- Line 331: Duplicate range [1-473]
- Line 338: Duplicate range [1-473]
- Line 376: Duplicate range [1-473]
- Line 385: Duplicate range [1-473]
- Line 408: Duplicate range [1-473]

---

### File: dynamic/commentary/02-15-02-01.txt

**Errors:**
- Line 6: Duplicate range [1-195]
- Line 11: Duplicate range [1-195]
- Line 16: Duplicate range [1-195]
- Line 21: Duplicate range [1-195]
- Line 26: Duplicate range [1-195]
- Line 31: Duplicate range [1-195]
- Line 34: Duplicate range [1-195]
- Line 37: Duplicate range [1-195]
- Line 40: Duplicate range [1-195]
- Line 43: Duplicate range [1-195]
- Line 46: Duplicate range [1-195]
- Line 52: Duplicate range [1-195]
- Line 55: Duplicate range [1-195]
- Line 58: Duplicate range [1-195]
- Line 61: Duplicate range [1-195]
- Line 64: Duplicate range [1-195]
- Line 67: Duplicate range [1-195]
- Line 70: Duplicate range [1-195]
- Line 73: Duplicate range [1-195]
- Line 76: Duplicate range [1-195]
- Line 79: Duplicate range [1-195]
- Line 82: Duplicate range [1-195]

---

### File: dynamic/commentary/02-15-03-01.txt

**Errors:**
- Line 6: Duplicate range [1-16]
- Line 11: Duplicate range [1-16]

---

### File: dynamic/commentary/02-16-01-01.txt

**Errors:**
- Line 18: Duplicate range [1-336]
- Line 34: Duplicate range [1-336]
- Line 49: Duplicate range [1-336]
- Line 64: Duplicate range [1-336]
- Line 77: Duplicate range [1-336]
- Line 91: Duplicate range [1-336]
- Line 107: Duplicate range [1-336]
- Line 119: Duplicate range [1-336]
- Line 130: Duplicate range [1-336]
- Line 143: Duplicate range [1-336]
- Line 154: Duplicate range [1-336]
- Line 166: Duplicate range [1-336]
- Line 179: Duplicate range [1-336]
- Line 192: Duplicate range [1-336]
- Line 205: Duplicate range [1-336]
- Line 218: Duplicate range [1-336]
- Line 229: Duplicate range [1-336]
- Line 244: Duplicate range [1-336]
- Line 256: Duplicate range [1-336]
- Line 269: Duplicate range [1-336]
- Line 280: Duplicate range [1-336]
- Line 293: Duplicate range [1-336]
- Line 306: Duplicate range [1-336]
- Line 319: Duplicate range [1-336]
- Line 330: Duplicate range [1-336]
- Line 350: Duplicate range [1-336]
- Line 363: Duplicate range [1-336]
- Line 384: Duplicate range [1-336]

---

### File: dynamic/commentary/02-16-02-01.txt

**Errors:**
- Line 15: Duplicate range [1-161]
- Line 18: Duplicate range [1-161]
- Line 21: Duplicate range [1-161]
- Line 26: Duplicate range [1-161]
- Line 33: Duplicate range [1-161]
- Line 38: Duplicate range [1-161]
- Line 43: Duplicate range [1-161]
- Line 52: Duplicate range [1-161]
- Line 59: Duplicate range [1-161]
- Line 64: Duplicate range [1-161]
- Line 67: Duplicate range [1-161]
- Line 72: Duplicate range [1-161]
- Line 75: Duplicate range [1-161]
- Line 78: Duplicate range [1-161]

---

### File: dynamic/commentary/02-16-03-01.txt

**Errors:**
- Line 4: Duplicate range [1-407]
- Line 7: Duplicate range [1-407]
- Line 10: Duplicate range [1-407]
- Line 15: Duplicate range [1-407]
- Line 18: Duplicate range [1-407]
- Line 23: Duplicate range [1-407]
- Line 26: Duplicate range [1-407]
- Line 29: Duplicate range [1-407]
- Line 34: Duplicate range [1-407]
- Line 39: Duplicate range [1-407]
- Line 44: Duplicate range [1-407]
- Line 47: Duplicate range [1-407]
- Line 50: Duplicate range [1-407]
- Line 57: Duplicate range [1-407]
- Line 60: Duplicate range [1-407]
- Line 65: Duplicate range [1-407]
- Line 68: Duplicate range [1-407]
- Line 74: Duplicate range [1-407]
- Line 81: Duplicate range [1-407]
- Line 86: Duplicate range [1-407]
- Line 108: Duplicate range [1-407]
- Line 113: Duplicate range [1-407]
- Line 118: Duplicate range [1-407]
- Line 123: Duplicate range [1-407]
- Line 132: Duplicate range [1-407]
- Line 137: Duplicate range [1-407]
- Line 142: Duplicate range [1-407]
- Line 147: Duplicate range [1-407]

---

### File: dynamic/commentary/02-16-04-01.txt

**Errors:**
- Line 6: Duplicate range [1-49]
- Line 13: Duplicate range [1-49]
- Line 22: Duplicate range [1-49]
- Line 31: Duplicate range [1-49]

---

### File: dynamic/commentary/02-16-05-01.txt

**Errors:**
- Line 5: Duplicate range [1-116]
- Line 7: Duplicate range [1-116]
- Line 11: Duplicate range [1-116]
- Line 15: Duplicate range [1-116]
- Line 19: Duplicate range [1-116]
- Line 23: Duplicate range [1-116]
- Line 27: Duplicate range [1-116]
- Line 31: Duplicate range [1-116]
- Line 35: Duplicate range [1-116]
- Line 39: Duplicate range [1-116]
- Line 43: Duplicate range [1-116]

---

### File: dynamic/commentary/02-17-01-01.txt

**Errors:**
- Line 5: Duplicate range [1-107]
- Line 9: Duplicate range [1-107]
- Line 13: Duplicate range [1-107]
- Line 15: Duplicate range [1-107]
- Line 19: Duplicate range [1-107]
- Line 21: Duplicate range [1-107]
- Line 25: Duplicate range [1-107]
- Line 27: Duplicate range [1-107]
- Line 33: Duplicate range [1-107]
- Line 37: Duplicate range [1-107]

---

### File: dynamic/commentary/02-17-02-01.txt

**Errors:**
- Line 11: Duplicate range [1-190]
- Line 17: Duplicate range [1-190]
- Line 28: Duplicate range [1-190]
- Line 40: Duplicate range [1-190]
- Line 51: Duplicate range [1-190]
- Line 58: Duplicate range [1-190]
- Line 63: Duplicate range [1-190]
- Line 66: Duplicate range [1-190]
- Line 75: Duplicate range [1-190]
- Line 78: Duplicate range [1-190]
- Line 99: Duplicate range [1-190]
- Line 105: Duplicate range [1-190]
- Line 112: Duplicate range [1-190]
- Line 118: Duplicate range [1-190]
- Line 124: Duplicate range [1-190]
- Line 131: Duplicate range [1-190]
- Line 137: Duplicate range [1-190]
- Line 143: Duplicate range [1-190]
- Line 149: Duplicate range [1-190]

---

### File: dynamic/commentary/02-17-03-01.txt

**Errors:**
- Line 5: Duplicate range [1-13]
- Line 9: Duplicate range [1-13]
- Line 13: Duplicate range [1-13]

---

### File: dynamic/commentary/02-17-04-01.txt

**Errors:**
- Line 27: Duplicate range [1-625]
- Line 45: Duplicate range [1-625]
- Line 64: Duplicate range [1-625]
- Line 83: Duplicate range [1-625]
- Line 100: Duplicate range [1-625]
- Line 110: Duplicate range [1-625]
- Line 121: Duplicate range [1-625]
- Line 132: Duplicate range [1-625]
- Line 138: Duplicate range [1-625]
- Line 143: Duplicate range [1-625]
- Line 149: Duplicate range [1-625]
- Line 154: Duplicate range [1-625]
- Line 160: Duplicate range [1-625]
- Line 166: Duplicate range [1-625]
- Line 170: Duplicate range [1-625]
- Line 182: Duplicate range [1-625]
- Line 192: Duplicate range [1-625]
- Line 199: Duplicate range [1-625]
- Line 206: Duplicate range [1-625]
- Line 213: Duplicate range [1-625]
- Line 220: Duplicate range [1-625]
- Line 227: Duplicate range [1-625]
- Line 234: Duplicate range [1-625]
- Line 241: Duplicate range [1-625]
- Line 248: Duplicate range [1-625]
- Line 254: Duplicate range [1-625]
- Line 262: Duplicate range [1-625]
- Line 272: Duplicate range [1-625]
- Line 279: Duplicate range [1-625]
- Line 289: Duplicate range [1-625]
- Line 298: Duplicate range [1-625]
- Line 304: Duplicate range [1-625]
- Line 311: Duplicate range [1-625]
- Line 318: Duplicate range [1-625]
- Line 324: Duplicate range [1-625]
- Line 331: Duplicate range [1-625]
- Line 338: Duplicate range [1-625]
- Line 345: Duplicate range [1-625]
- Line 352: Duplicate range [1-625]
- Line 359: Duplicate range [1-625]
- Line 378: Duplicate range [1-625]
- Line 395: Duplicate range [1-625]
- Line 432: Duplicate range [1-625]
- Line 477: Duplicate range [1-625]
- Line 493: Duplicate range [1-625]
- Line 532: Duplicate range [1-625]
- Line 573: Duplicate range [1-625]

---

### File: dynamic/commentary/02-17-05-01.txt

**Errors:**
- Line 5: Duplicate range [1-90]
- Line 9: Duplicate range [1-90]
- Line 11: Duplicate range [1-90]
- Line 15: Duplicate range [1-90]
- Line 19: Duplicate range [1-90]
- Line 31: Duplicate range [1-90]
- Line 35: Duplicate range [1-90]
- Line 39: Duplicate range [1-90]
- Line 43: Duplicate range [1-90]

---

### File: dynamic/commentary/02-17-06-01.txt

**Errors:**
- Line 7: Duplicate range [1-226]
- Line 10: Duplicate range [1-226]
- Line 16: Duplicate range [1-226]
- Line 22: Duplicate range [1-226]
- Line 25: Duplicate range [1-226]
- Line 31: Duplicate range [1-226]
- Line 34: Duplicate range [1-226]
- Line 40: Duplicate range [1-226]
- Line 46: Duplicate range [1-226]
- Line 52: Duplicate range [1-226]
- Line 58: Duplicate range [1-226]
- Line 64: Duplicate range [1-226]
- Line 70: Duplicate range [1-226]
- Line 76: Duplicate range [1-226]
- Line 82: Duplicate range [1-226]
- Line 85: Duplicate range [1-226]
- Line 97: Duplicate range [1-226]
- Line 108: Duplicate range [1-226]
- Line 118: Duplicate range [1-226]
- Line 128: Duplicate range [1-226]
- Line 144: Duplicate range [1-226]
- Line 147: Duplicate range [1-226]
- Line 160: Duplicate range [1-226]
- Line 173: Duplicate range [1-226]
- Line 186: Duplicate range [1-226]
- Line 200: Duplicate range [1-226]
- Line 217: Duplicate range [1-226]

---

### File: dynamic/commentary/02-17-07-01.txt

**Errors:**
- Line 12: Duplicate range [1-52]
- Line 22: Duplicate range [1-52]
- Line 31: Duplicate range [1-52]
- Line 40: Duplicate range [1-52]
- Line 49: Duplicate range [1-52]
- Line 59: Duplicate range [1-52]
- Line 64: Duplicate range [1-52]
- Line 69: Duplicate range [1-52]
- Line 74: Duplicate range [1-52]
- Line 78: Duplicate range [1-52]

---

### File: dynamic/commentary/02-17-08-01.txt

**Errors:**
- Line 8: Duplicate range [1-67]
- Line 13: Duplicate range [1-67]
- Line 18: Duplicate range [1-67]
- Line 27: Duplicate range [1-67]

---

### File: dynamic/commentary/02-17-09-01.txt

**Errors:**
- Line 5: Duplicate range [1-74]
- Line 9: Duplicate range [1-74]
- Line 13: Duplicate range [1-74]
- Line 17: Duplicate range [1-74]
- Line 19: Duplicate range [1-74]
- Line 23: Duplicate range [1-74]
- Line 27: Duplicate range [1-74]

---

### File: dynamic/commentary/02-17-09-02.txt

**Errors:**
- Line 10: Duplicate range [1-109]
- Line 19: Duplicate range [1-109]
- Line 26: Duplicate range [1-109]
- Line 35: Duplicate range [1-109]
- Line 42: Duplicate range [1-109]

---

### File: dynamic/commentary/02-17-10-01.txt

**Errors:**
- Line 11: Duplicate range [1-47]
- Line 22: Duplicate range [1-47]
- Line 31: Duplicate range [1-47]
- Line 48: Duplicate range [1-47]
- Line 52: Duplicate range [1-47]
- Line 56: Duplicate range [1-47]
- Line 60: Duplicate range [1-47]
- Line 64: Duplicate range [1-47]
- Line 68: Duplicate range [1-47]

---

### File: dynamic/commentary/02-17-11-01.txt

**Errors:**
- Line 7: Duplicate range [1-246]
- Line 13: Duplicate range [1-246]
- Line 19: Duplicate range [1-246]
- Line 22: Duplicate range [1-246]
- Line 25: Duplicate range [1-246]
- Line 31: Duplicate range [1-246]
- Line 34: Duplicate range [1-246]
- Line 37: Duplicate range [1-246]
- Line 43: Duplicate range [1-246]
- Line 49: Duplicate range [1-246]
- Line 52: Duplicate range [1-246]
- Line 60: Duplicate range [1-246]
- Line 72: Duplicate range [1-246]
- Line 83: Duplicate range [1-246]
- Line 95: Duplicate range [1-246]
- Line 105: Duplicate range [1-246]
- Line 116: Duplicate range [1-246]
- Line 126: Duplicate range [1-246]
- Line 137: Duplicate range [1-246]
- Line 147: Duplicate range [1-246]
- Line 156: Duplicate range [1-246]
- Line 161: Duplicate range [1-246]
- Line 168: Duplicate range [1-246]
- Line 177: Duplicate range [1-246]
- Line 186: Duplicate range [1-246]
- Line 196: Duplicate range [1-246]
- Line 210: Duplicate range [1-246]
- Line 215: Duplicate range [1-246]
- Line 225: Duplicate range [1-246]
- Line 242: Duplicate range [1-246]
- Line 254: Duplicate range [1-246]
- Line 264: Duplicate range [1-246]
- Line 275: Duplicate range [1-246]
- Line 286: Duplicate range [1-246]
- Line 299: Duplicate range [1-246]
- Line 310: Duplicate range [1-246]
- Line 315: Duplicate range [1-246]

---

### File: dynamic/commentary/02-17-12-01.txt

**Errors:**
- Line 8: Duplicate range [1-109]
- Line 15: Duplicate range [1-109]
- Line 22: Duplicate range [1-109]
- Line 29: Duplicate range [1-109]
- Line 36: Duplicate range [1-109]
- Line 43: Duplicate range [1-109]
- Line 48: Duplicate range [1-109]
- Line 53: Duplicate range [1-109]
- Line 58: Duplicate range [1-109]
- Line 63: Duplicate range [1-109]

---

### File: dynamic/commentary/02-17-13-01.txt

**Errors:**
- Line 12: Duplicate range [1-143]
- Line 22: Duplicate range [1-143]
- Line 32: Duplicate range [1-143]
- Line 42: Duplicate range [1-143]
- Line 53: Duplicate range [1-143]
- Line 64: Duplicate range [1-143]
- Line 70: Duplicate range [1-143]
- Line 76: Duplicate range [1-143]
- Line 81: Duplicate range [1-143]
- Line 86: Duplicate range [1-143]
- Line 96: Duplicate range [1-143]
- Line 103: Duplicate range [1-143]
- Line 108: Duplicate range [1-143]
- Line 111: Duplicate range [1-143]
- Line 123: Duplicate range [1-143]
- Line 126: Duplicate range [1-143]

---

### File: dynamic/commentary/02-17-14-01.txt

**Errors:**
- Line 10: Duplicate range [1-70]
- Line 20: Duplicate range [1-70]
- Line 31: Duplicate range [1-70]
- Line 40: Duplicate range [1-70]
- Line 50: Duplicate range [1-70]
- Line 60: Duplicate range [1-70]
- Line 71: Duplicate range [1-70]
- Line 80: Duplicate range [1-70]

---

### File: dynamic/commentary/02-18-01-01.txt

**Errors:**
- Line 10: Duplicate range [1-234]
- Line 19: Duplicate range [1-234]
- Line 28: Duplicate range [1-234]
- Line 37: Duplicate range [1-234]
- Line 46: Duplicate range [1-234]
- Line 53: Duplicate range [1-234]
- Line 60: Duplicate range [1-234]
- Line 67: Duplicate range [1-234]
- Line 74: Duplicate range [1-234]
- Line 81: Duplicate range [1-234]
- Line 88: Duplicate range [1-234]
- Line 99: Duplicate range [1-234]
- Line 116: Duplicate range [1-234]
- Line 131: Duplicate range [1-234]
- Line 144: Duplicate range [1-234]
- Line 159: Duplicate range [1-234]
- Line 168: Duplicate range [1-234]
- Line 179: Duplicate range [1-234]
- Line 190: Duplicate range [1-234]
- Line 201: Duplicate range [1-234]

---

### File: dynamic/commentary/02-18-02-01.txt

**Errors:**
- Line 6: Duplicate range [1-245]
- Line 17: Duplicate range [1-245]
- Line 22: Duplicate range [1-245]
- Line 31: Duplicate range [1-245]
- Line 36: Duplicate range [1-245]
- Line 41: Duplicate range [1-245]
- Line 50: Duplicate range [1-245]
- Line 59: Duplicate range [1-245]
- Line 64: Duplicate range [1-245]
- Line 73: Duplicate range [1-245]
- Line 82: Duplicate range [1-245]
- Line 95: Duplicate range [1-245]
- Line 104: Duplicate range [1-245]

---

### File: dynamic/commentary/02-18-02-02.txt

**Errors:**
- Line 7: Duplicate range [1-5]
- Line 12: Duplicate range [1-5]
- Line 18: Duplicate range [1-5]
- Line 22: Duplicate range [1-5]
- Line 28: Duplicate range [1-5]

---

### File: dynamic/commentary/02-18-02-03.txt

**Errors:**
- Line 4: Duplicate range [1-19]
- Line 9: Duplicate range [1-19]
- Line 12: Duplicate range [1-19]
- Line 17: Duplicate range [1-19]

---

### File: dynamic/commentary/02-18-03-01.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 17: Duplicate range [1-1]
- Line 21: Duplicate range [1-1]

---

### File: dynamic/commentary/02-18-03-02.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 10: Duplicate range [1-1]
- Line 14: Duplicate range [1-1]
- Line 18: Duplicate range [1-1]

---

### File: dynamic/commentary/02-18-03-03.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 15: Duplicate range [1-1]
- Line 20: Duplicate range [1-1]

---

### File: dynamic/commentary/02-18-03-04.txt

**Errors:**
- Line 8: Duplicate range [1-40]
- Line 23: Duplicate range [1-40]
- Line 28: Duplicate range [1-40]
- Line 38: Duplicate range [1-40]
- Line 45: Duplicate range [1-40]
- Line 52: Duplicate range [1-40]

---

### File: dynamic/commentary/02-18-04-01.txt

**Errors:**
- Line 6: Duplicate range [1-133]
- Line 12: Duplicate range [1-133]
- Line 23: Duplicate range [1-133]
- Line 28: Duplicate range [1-133]
- Line 34: Duplicate range [1-133]
- Line 40: Duplicate range [1-133]
- Line 46: Duplicate range [1-133]
- Line 51: Duplicate range [1-133]
- Line 57: Duplicate range [1-133]
- Line 63: Duplicate range [1-133]
- Line 70: Duplicate range [1-133]
- Line 76: Duplicate range [1-133]
- Line 81: Duplicate range [1-133]
- Line 86: Duplicate range [1-133]
- Line 92: Duplicate range [1-133]
- Line 97: Duplicate range [1-133]
- Line 102: Duplicate range [1-133]
- Line 108: Duplicate range [1-133]
- Line 114: Duplicate range [1-133]
- Line 119: Duplicate range [1-133]
- Line 125: Duplicate range [1-133]
- Line 130: Duplicate range [1-133]
- Line 135: Duplicate range [1-133]
- Line 141: Duplicate range [1-133]
- Line 147: Duplicate range [1-133]
- Line 153: Duplicate range [1-133]
- Line 159: Duplicate range [1-133]
- Line 164: Duplicate range [1-133]
- Line 170: Duplicate range [1-133]
- Line 176: Duplicate range [1-133]
- Line 182: Duplicate range [1-133]
- Line 187: Duplicate range [1-133]
- Line 192: Duplicate range [1-133]
- Line 198: Duplicate range [1-133]
- Line 211: Duplicate range [1-133]

---

### File: dynamic/commentary/02-18-05-01.txt

**Errors:**
- Line 10: Duplicate range [1-95]
- Line 19: Duplicate range [1-95]
- Line 24: Duplicate range [1-95]
- Line 33: Duplicate range [1-95]
- Line 38: Duplicate range [1-95]
- Line 43: Duplicate range [1-95]
- Line 48: Duplicate range [1-95]
- Line 51: Duplicate range [1-95]
- Line 54: Duplicate range [1-95]

---

### File: dynamic/commentary/02-18-06-01.txt

**Errors:**
- Line 17: Duplicate range [1-51]
- Line 31: Duplicate range [1-51]
- Line 44: Duplicate range [1-51]
- Line 61: Duplicate range [1-51]
- Line 74: Duplicate range [1-51]
- Line 86: Duplicate range [1-51]

---

### File: dynamic/commentary/02-18-07-01.txt

**Errors:**
- Line 4: Duplicate range [1-169]
- Line 10: Duplicate range [1-169]
- Line 16: Duplicate range [1-169]
- Line 19: Duplicate range [1-169]
- Line 22: Duplicate range [1-169]
- Line 25: Duplicate range [1-169]
- Line 28: Duplicate range [1-169]
- Line 31: Duplicate range [1-169]
- Line 34: Duplicate range [1-169]
- Line 37: Duplicate range [1-169]
- Line 40: Duplicate range [1-169]
- Line 46: Duplicate range [1-169]
- Line 49: Duplicate range [1-169]
- Line 52: Duplicate range [1-169]
- Line 55: Duplicate range [1-169]
- Line 58: Duplicate range [1-169]
- Line 61: Duplicate range [1-169]
- Line 64: Duplicate range [1-169]
- Line 67: Duplicate range [1-169]
- Line 70: Duplicate range [1-169]
- Line 73: Duplicate range [1-169]
- Line 76: Duplicate range [1-169]
- Line 79: Duplicate range [1-169]
- Line 82: Duplicate range [1-169]
- Line 88: Duplicate range [1-169]
- Line 91: Duplicate range [1-169]
- Line 99: Duplicate range [1-169]
- Line 110: Duplicate range [1-169]
- Line 120: Duplicate range [1-169]
- Line 134: Duplicate range [1-169]
- Line 137: Duplicate range [1-169]
- Line 149: Duplicate range [1-169]
- Line 161: Duplicate range [1-169]
- Line 172: Duplicate range [1-169]
- Line 183: Duplicate range [1-169]
- Line 194: Duplicate range [1-169]
- Line 205: Duplicate range [1-169]
- Line 215: Duplicate range [1-169]

---

### File: dynamic/commentary/02-18-08-01.txt

**Errors:**
- Line 5: Duplicate range [1-119]
- Line 9: Duplicate range [1-119]
- Line 11: Duplicate range [1-119]
- Line 15: Duplicate range [1-119]
- Line 19: Duplicate range [1-119]
- Line 23: Duplicate range [1-119]
- Line 27: Duplicate range [1-119]
- Line 31: Duplicate range [1-119]
- Line 35: Duplicate range [1-119]
- Line 39: Duplicate range [1-119]
- Line 43: Duplicate range [1-119]
- Line 49: Duplicate range [1-119]
- Line 51: Duplicate range [1-119]
- Line 55: Duplicate range [1-119]
- Line 59: Duplicate range [1-119]
- Line 63: Duplicate range [1-119]
- Line 67: Duplicate range [1-119]
- Line 71: Duplicate range [1-119]
- Line 75: Duplicate range [1-119]
- Line 79: Duplicate range [1-119]
- Line 83: Duplicate range [1-119]
- Line 87: Duplicate range [1-119]
- Line 91: Duplicate range [1-119]
- Line 95: Duplicate range [1-119]
- Line 99: Duplicate range [1-119]

---

### File: dynamic/commentary/02-18-08-02.txt

**Errors:**
- Line 5: Duplicate range [1-50]
- Line 9: Duplicate range [1-50]
- Line 11: Duplicate range [1-50]
- Line 15: Duplicate range [1-50]
- Line 17: Duplicate range [1-50]
- Line 19: Duplicate range [1-50]
- Line 21: Duplicate range [1-50]
- Line 23: Duplicate range [1-50]
- Line 27: Duplicate range [1-50]
- Line 29: Duplicate range [1-50]

---

### File: dynamic/commentary/02-18-09-01.txt

**Errors:**
- Line 5: Duplicate range [1-40]
- Line 9: Duplicate range [1-40]
- Line 13: Duplicate range [1-40]
- Line 17: Duplicate range [1-40]
- Line 21: Duplicate range [1-40]

---

### File: dynamic/commentary/02-18-10-01.txt

**Errors:**
- Line 5: Duplicate range [1-34]
- Line 9: Duplicate range [1-34]
- Line 11: Duplicate range [1-34]
- Line 15: Duplicate range [1-34]
- Line 17: Duplicate range [1-34]
- Line 21: Duplicate range [1-34]
- Line 23: Duplicate range [1-34]

---

### File: dynamic/commentary/02-18-11-01.txt

**Errors:**
- Line 8: Duplicate range [1-83]
- Line 15: Duplicate range [1-83]
- Line 22: Duplicate range [1-83]
- Line 29: Duplicate range [1-83]
- Line 32: Duplicate range [1-83]
- Line 39: Duplicate range [1-83]
- Line 42: Duplicate range [1-83]
- Line 47: Duplicate range [1-83]

---

### File: dynamic/commentary/02-18-12-01.txt

**Errors:**
- Line 8: Duplicate range [1-27]
- Line 11: Duplicate range [1-27]
- Line 18: Duplicate range [1-27]
- Line 25: Duplicate range [1-27]
- Line 32: Duplicate range [1-27]

---

### File: dynamic/commentary/02-18-13-01.txt

**Errors:**
- Line 6: Duplicate range [1-371]
- Line 11: Duplicate range [1-371]
- Line 20: Duplicate range [1-371]
- Line 23: Duplicate range [1-371]
- Line 30: Duplicate range [1-371]
- Line 35: Duplicate range [1-371]
- Line 40: Duplicate range [1-371]
- Line 49: Duplicate range [1-371]
- Line 54: Duplicate range [1-371]
- Line 59: Duplicate range [1-371]
- Line 66: Duplicate range [1-371]
- Line 71: Duplicate range [1-371]
- Line 76: Duplicate range [1-371]
- Line 83: Duplicate range [1-371]
- Line 90: Duplicate range [1-371]
- Line 95: Duplicate range [1-371]
- Line 102: Duplicate range [1-371]
- Line 107: Duplicate range [1-371]
- Line 114: Duplicate range [1-371]
- Line 117: Duplicate range [1-371]
- Line 122: Duplicate range [1-371]
- Line 127: Duplicate range [1-371]
- Line 132: Duplicate range [1-371]
- Line 141: Duplicate range [1-371]
- Line 148: Duplicate range [1-371]
- Line 155: Duplicate range [1-371]
- Line 160: Duplicate range [1-371]
- Line 169: Duplicate range [1-371]
- Line 172: Duplicate range [1-371]
- Line 179: Duplicate range [1-371]
- Line 184: Duplicate range [1-371]
- Line 195: Duplicate range [1-371]
- Line 208: Duplicate range [1-371]
- Line 217: Duplicate range [1-371]
- Line 222: Duplicate range [1-371]
- Line 227: Duplicate range [1-371]
- Line 236: Duplicate range [1-371]
- Line 241: Duplicate range [1-371]
- Line 244: Duplicate range [1-371]
- Line 255: Duplicate range [1-371]
- Line 258: Duplicate range [1-371]
- Line 265: Duplicate range [1-371]
- Line 274: Duplicate range [1-371]
- Line 277: Duplicate range [1-371]
- Line 282: Duplicate range [1-371]
- Line 287: Duplicate range [1-371]
- Line 294: Duplicate range [1-371]
- Line 303: Duplicate range [1-371]
- Line 312: Duplicate range [1-371]
- Line 315: Duplicate range [1-371]
- Line 322: Duplicate range [1-371]
- Line 327: Duplicate range [1-371]
- Line 332: Duplicate range [1-371]
- Line 339: Duplicate range [1-371]
- Line 348: Duplicate range [1-371]
- Line 351: Duplicate range [1-371]
- Line 354: Duplicate range [1-371]
- Line 357: Duplicate range [1-371]

---

### File: dynamic/commentary/02-18-14-01.txt

**Errors:**
- Line 6: Duplicate range [1-6]
- Line 9: Duplicate range [1-6]
- Line 12: Duplicate range [1-6]
- Line 15: Duplicate range [1-6]

---

### File: dynamic/commentary/02-18-15-01.txt

**Errors:**
- Line 4: Duplicate range [1-265]
- Line 7: Duplicate range [1-265]
- Line 10: Duplicate range [1-265]
- Line 13: Duplicate range [1-265]
- Line 16: Duplicate range [1-265]
- Line 19: Duplicate range [1-265]
- Line 22: Duplicate range [1-265]
- Line 25: Duplicate range [1-265]
- Line 28: Duplicate range [1-265]
- Line 31: Duplicate range [1-265]
- Line 34: Duplicate range [1-265]
- Line 37: Duplicate range [1-265]
- Line 40: Duplicate range [1-265]
- Line 43: Duplicate range [1-265]
- Line 46: Duplicate range [1-265]
- Line 49: Duplicate range [1-265]
- Line 59: Duplicate range [1-265]
- Line 66: Duplicate range [1-265]
- Line 73: Duplicate range [1-265]
- Line 80: Duplicate range [1-265]
- Line 86: Duplicate range [1-265]
- Line 92: Duplicate range [1-265]
- Line 99: Duplicate range [1-265]
- Line 106: Duplicate range [1-265]
- Line 113: Duplicate range [1-265]
- Line 120: Duplicate range [1-265]
- Line 131: Duplicate range [1-265]
- Line 148: Duplicate range [1-265]
- Line 156: Duplicate range [1-265]
- Line 163: Duplicate range [1-265]
- Line 170: Duplicate range [1-265]
- Line 177: Duplicate range [1-265]
- Line 185: Duplicate range [1-265]
- Line 191: Duplicate range [1-265]
- Line 198: Duplicate range [1-265]
- Line 205: Duplicate range [1-265]
- Line 212: Duplicate range [1-265]
- Line 218: Duplicate range [1-265]
- Line 225: Duplicate range [1-265]
- Line 231: Duplicate range [1-265]
- Line 253: Duplicate range [1-265]
- Line 287: Duplicate range [1-265]
- Line 335: Duplicate range [1-265]

---

### File: dynamic/commentary/02-18-16-01.txt

**Errors:**
- Line 6: Duplicate range [1-12]

---

### File: dynamic/commentary/02-18-16-02.txt

**Errors:**
- Line 5: Duplicate range [1-2]
- Line 9: Duplicate range [1-2]
- Line 13: Duplicate range [1-2]
- Line 17: Duplicate range [1-2]
- Line 21: Duplicate range [1-2]

---

### File: dynamic/commentary/02-18-16-03.txt

**Errors:**
- Line 5: Duplicate range [1-3]
- Line 9: Duplicate range [1-3]
- Line 13: Duplicate range [1-3]
- Line 17: Duplicate range [1-3]
- Line 21: Duplicate range [1-3]
- Line 25: Duplicate range [1-3]

---

### File: dynamic/commentary/02-18-16-04.txt

**Errors:**
- Line 6: Duplicate range [1-35]
- Line 11: Duplicate range [1-35]
- Line 16: Duplicate range [1-35]
- Line 21: Duplicate range [1-35]

---

### File: dynamic/commentary/02-19-00-01.txt

**Errors:**
- Line 7: Duplicate range [1-451]
- Line 13: Duplicate range [1-451]
- Line 20: Duplicate range [1-451]
- Line 25: Duplicate range [1-451]
- Line 31: Duplicate range [1-451]
- Line 38: Duplicate range [1-451]
- Line 44: Duplicate range [1-451]
- Line 50: Duplicate range [1-451]
- Line 56: Duplicate range [1-451]
- Line 62: Duplicate range [1-451]
- Line 68: Duplicate range [1-451]
- Line 74: Duplicate range [1-451]
- Line 80: Duplicate range [1-451]
- Line 86: Duplicate range [1-451]
- Line 92: Duplicate range [1-451]
- Line 98: Duplicate range [1-451]
- Line 104: Duplicate range [1-451]
- Line 110: Duplicate range [1-451]
- Line 116: Duplicate range [1-451]
- Line 122: Duplicate range [1-451]
- Line 128: Duplicate range [1-451]
- Line 135: Duplicate range [1-451]
- Line 141: Duplicate range [1-451]
- Line 155: Duplicate range [1-451]
- Line 163: Duplicate range [1-451]
- Line 171: Duplicate range [1-451]
- Line 179: Duplicate range [1-451]
- Line 185: Duplicate range [1-451]
- Line 192: Duplicate range [1-451]
- Line 199: Duplicate range [1-451]
- Line 206: Duplicate range [1-451]
- Line 213: Duplicate range [1-451]
- Line 220: Duplicate range [1-451]
- Line 231: Duplicate range [1-451]
- Line 242: Duplicate range [1-451]
- Line 249: Duplicate range [1-451]
- Line 255: Duplicate range [1-451]
- Line 261: Duplicate range [1-451]
- Line 269: Duplicate range [1-451]
- Line 275: Duplicate range [1-451]
- Line 280: Duplicate range [1-451]
- Line 286: Duplicate range [1-451]
- Line 291: Duplicate range [1-451]
- Line 297: Duplicate range [1-451]
- Line 303: Duplicate range [1-451]
- Line 309: Duplicate range [1-451]
- Line 314: Duplicate range [1-451]
- Line 326: Duplicate range [1-451]

---

### File: dynamic/commentary/02-19-01-01.txt

**Errors:**
- Line 647: Non-sequential range [1-1669] - Start (1) < Previous start (1172)
- Line 8: Duplicate range [1-1669]
- Line 14: Duplicate range [1-1669]
- Line 21: Duplicate range [1-1669]
- Line 27: Duplicate range [1-1669]
- Line 33: Duplicate range [1-1669]
- Line 39: Duplicate range [1-1669]
- Line 44: Duplicate range [1-1669]
- Line 50: Duplicate range [1-1669]
- Line 56: Duplicate range [1-1669]
- Line 62: Duplicate range [1-1669]
- Line 67: Duplicate range [1-1669]
- Line 73: Duplicate range [1-1669]
- Line 79: Duplicate range [1-1669]
- Line 85: Duplicate range [1-1669]
- Line 91: Duplicate range [1-1669]
- Line 96: Duplicate range [1-1669]
- Line 102: Duplicate range [1-1669]
- Line 109: Duplicate range [1-1669]
- Line 114: Duplicate range [1-1669]
- Line 119: Duplicate range [1-1669]
- Line 136: Duplicate range [1-1669]
- Line 141: Duplicate range [1-1669]
- Line 146: Duplicate range [1-1669]
- Line 168: Duplicate range [1-1669]
- Line 173: Duplicate range [1-1669]
- Line 178: Duplicate range [1-1669]
- Line 183: Duplicate range [1-1669]
- Line 200: Duplicate range [1-1669]
- Line 205: Duplicate range [1-1669]
- Line 222: Duplicate range [1-1669]
- Line 227: Duplicate range [1-1669]
- Line 232: Duplicate range [1-1669]
- Line 245: Duplicate range [1-1669]
- Line 251: Duplicate range [1-1669]
- Line 257: Duplicate range [1-1669]
- Line 263: Duplicate range [1-1669]
- Line 269: Duplicate range [1-1669]
- Line 275: Duplicate range [1-1669]
- Line 281: Duplicate range [1-1669]
- Line 287: Duplicate range [1-1669]
- Line 298: Duplicate range [1-1669]
- Line 305: Duplicate range [1-1669]
- Line 310: Duplicate range [1-1669]
- Line 315: Duplicate range [1-1669]
- Line 321: Duplicate range [1-1669]
- Line 326: Duplicate range [1-1669]
- Line 332: Duplicate range [1-1669]
- Line 337: Duplicate range [1-1669]
- Line 343: Duplicate range [1-1669]
- Line 349: Duplicate range [1-1669]
- Line 354: Duplicate range [1-1669]
- Line 359: Duplicate range [1-1669]
- Line 366: Duplicate range [1-1669]
- Line 373: Duplicate range [1-1669]
- Line 378: Duplicate range [1-1669]
- Line 381: Duplicate range [1-1669]
- Line 387: Duplicate range [1-1669]
- Line 394: Duplicate range [1-1669]
- Line 398: Duplicate range [1-1669]
- Line 403: Duplicate range [1-1669]
- Line 406: Duplicate range [1-1669]
- Line 411: Duplicate range [1-1669]
- Line 419: Duplicate range [1-1669]
- Line 424: Duplicate range [1-1669]
- Line 429: Duplicate range [1-1669]
- Line 448: Duplicate range [1-1669]
- Line 460: Duplicate range [1-1669]
- Line 465: Duplicate range [1-1669]
- Line 468: Duplicate range [1-1669]
- Line 471: Duplicate range [1-1669]
- Line 474: Duplicate range [1-1669]
- Line 477: Duplicate range [1-1669]
- Line 480: Duplicate range [1-1669]
- Line 483: Duplicate range [1-1669]
- Line 486: Duplicate range [1-1669]
- Line 489: Duplicate range [1-1669]
- Line 504: Duplicate range [1-1669]
- Line 507: Duplicate range [1-1669]
- Line 510: Duplicate range [1-1669]
- Line 513: Duplicate range [1-1669]
- Line 516: Duplicate range [1-1669]
- Line 519: Duplicate range [1-1669]
- Line 529: Duplicate range [1-1669]
- Line 533: Duplicate range [1-1669]
- Line 536: Duplicate range [1-1669]
- Line 539: Duplicate range [1-1669]
- Line 548: Duplicate range [1-1669]
- Line 555: Duplicate range [1-1669]
- Line 560: Duplicate range [1-1669]
- Line 571: Duplicate range [1-1669]
- Line 580: Duplicate range [1-1669]
- Line 589: Duplicate range [1-1669]
- Line 592: Duplicate range [1-1669]
- Line 597: Duplicate range [1-1669]
- Line 600: Duplicate range [1-1669]
- Line 603: Duplicate range [1-1669]
- Line 612: Duplicate range [1-1669]
- Line 615: Duplicate range [1-1669]
- Line 618: Duplicate range [1-1669]
- Line 621: Duplicate range [1-1669]
- Line 624: Duplicate range [1-1669]
- Line 647: Duplicate range [1-1669]
- Line 650: Duplicate range [1-1669]
- Line 657: Duplicate range [1-1669]
- Line 662: Duplicate range [1-1669]
- Line 665: Duplicate range [1-1669]
- Line 668: Duplicate range [1-1669]
- Line 671: Duplicate range [1-1669]
- Line 680: Duplicate range [1-1669]
- Line 683: Duplicate range [1-1669]
- Line 686: Duplicate range [1-1669]
- Line 694: Duplicate range [1-1669]
- Line 703: Duplicate range [1-1669]
- Line 716: Duplicate range [1-1669]
- Line 721: Duplicate range [1-1669]
- Line 732: Duplicate range [1-1669]
- Line 749: Duplicate range [1-1669]
- Line 754: Duplicate range [1-1669]
- Line 761: Duplicate range [1-1669]
- Line 772: Duplicate range [1-1669]
- Line 777: Duplicate range [1-1669]
- Line 782: Duplicate range [1-1669]
- Line 791: Duplicate range [1-1669]
- Line 798: Duplicate range [1-1669]
- Line 819: Duplicate range [1-1669]
- Line 824: Duplicate range [1-1669]
- Line 835: Duplicate range [1-1669]
- Line 840: Duplicate range [1-1669]
- Line 857: Duplicate range [1-1669]
- Line 862: Duplicate range [1-1669]
- Line 872: Duplicate range [1-1669]
- Line 877: Duplicate range [1-1669]
- Line 884: Duplicate range [1-1669]
- Line 889: Duplicate range [1-1669]
- Line 894: Duplicate range [1-1669]
- Line 899: Duplicate range [1-1669]
- Line 904: Duplicate range [1-1669]
- Line 913: Duplicate range [1-1669]
- Line 924: Duplicate range [1-1669]
- Line 929: Duplicate range [1-1669]
- Line 934: Duplicate range [1-1669]
- Line 949: Duplicate range [1-1669]
- Line 972: Duplicate range [1-1669]
- Line 999: Duplicate range [1-1669]
- Line 1004: Duplicate range [1-1669]
- Line 1009: Duplicate range [1-1669]

---

### File: dynamic/commentary/02-20-01-01.txt

**Errors:**
- Line 17: Duplicate range [1-748]
- Line 33: Duplicate range [1-748]
- Line 47: Duplicate range [1-748]
- Line 62: Duplicate range [1-748]
- Line 77: Duplicate range [1-748]
- Line 93: Duplicate range [1-748]
- Line 110: Duplicate range [1-748]
- Line 126: Duplicate range [1-748]
- Line 142: Duplicate range [1-748]
- Line 156: Duplicate range [1-748]
- Line 168: Duplicate range [1-748]
- Line 182: Duplicate range [1-748]
- Line 197: Duplicate range [1-748]
- Line 210: Duplicate range [1-748]
- Line 225: Duplicate range [1-748]
- Line 241: Duplicate range [1-748]
- Line 256: Duplicate range [1-748]
- Line 270: Duplicate range [1-748]
- Line 297: Duplicate range [1-748]
- Line 315: Duplicate range [1-748]
- Line 332: Duplicate range [1-748]
- Line 350: Duplicate range [1-748]
- Line 367: Duplicate range [1-748]
- Line 381: Duplicate range [1-748]
- Line 396: Duplicate range [1-748]
- Line 412: Duplicate range [1-748]
- Line 427: Duplicate range [1-748]
- Line 442: Duplicate range [1-748]
- Line 457: Duplicate range [1-748]
- Line 472: Duplicate range [1-748]
- Line 488: Duplicate range [1-748]
- Line 501: Duplicate range [1-748]
- Line 516: Duplicate range [1-748]
- Line 530: Duplicate range [1-748]
- Line 544: Duplicate range [1-748]
- Line 560: Duplicate range [1-748]
- Line 576: Duplicate range [1-748]
- Line 592: Duplicate range [1-748]
- Line 607: Duplicate range [1-748]
- Line 614: Duplicate range [1-748]
- Line 619: Duplicate range [1-748]
- Line 630: Duplicate range [1-748]
- Line 647: Duplicate range [1-748]
- Line 652: Duplicate range [1-748]
- Line 657: Duplicate range [1-748]
- Line 668: Duplicate range [1-748]
- Line 673: Duplicate range [1-748]
- Line 681: Duplicate range [1-748]
- Line 708: Duplicate range [1-748]
- Line 713: Duplicate range [1-748]
- Line 718: Duplicate range [1-748]
- Line 732: Duplicate range [1-748]
- Line 744: Duplicate range [1-748]

---

### File: dynamic/commentary/02-20-02-01.txt

**Errors:**
- Line 10: Duplicate range [1-139]
- Line 19: Duplicate range [1-139]
- Line 22: Duplicate range [1-139]
- Line 25: Duplicate range [1-139]
- Line 28: Duplicate range [1-139]
- Line 31: Duplicate range [1-139]
- Line 38: Duplicate range [1-139]
- Line 49: Duplicate range [1-139]

---

### File: dynamic/commentary/02-20-03-01.txt

**Errors:**
- Line 6: Duplicate range [1-2]
- Line 11: Duplicate range [1-2]
- Line 15: Duplicate range [1-2]
- Line 19: Duplicate range [1-2]
- Line 22: Duplicate range [1-2]

---

### File: dynamic/commentary/02-20-04-01.txt

**Errors:**
- Line 5: Duplicate range [1-55]
- Line 9: Duplicate range [1-55]
- Line 11: Duplicate range [1-55]
- Line 17: Duplicate range [1-55]
- Line 21: Duplicate range [1-55]
- Line 23: Duplicate range [1-55]
- Line 27: Duplicate range [1-55]
- Line 29: Duplicate range [1-55]

---

### File: dynamic/commentary/02-20-05-01.txt

**Errors:**
- Line 5: Duplicate range [1-42]
- Line 9: Duplicate range [1-42]
- Line 13: Duplicate range [1-42]
- Line 19: Duplicate range [1-42]
- Line 23: Duplicate range [1-42]

---

### File: dynamic/commentary/02-20-06-01.txt

**Errors:**
- Line 6: Duplicate range [1-10]
- Line 12: Duplicate range [1-10]
- Line 18: Duplicate range [1-10]
- Line 21: Duplicate range [1-10]
- Line 27: Duplicate range [1-10]
- Line 33: Duplicate range [1-10]
- Line 40: Duplicate range [1-10]

---

### File: dynamic/commentary/02-20-07-01.txt

**Errors:**
- Line 5: Duplicate range [1-144]
- Line 7: Duplicate range [1-144]
- Line 11: Duplicate range [1-144]
- Line 15: Duplicate range [1-144]
- Line 19: Duplicate range [1-144]
- Line 23: Duplicate range [1-144]
- Line 27: Duplicate range [1-144]
- Line 31: Duplicate range [1-144]
- Line 35: Duplicate range [1-144]
- Line 39: Duplicate range [1-144]
- Line 43: Duplicate range [1-144]
- Line 47: Duplicate range [1-144]
- Line 51: Duplicate range [1-144]
- Line 55: Duplicate range [1-144]
- Line 59: Duplicate range [1-144]
- Line 63: Duplicate range [1-144]

---

### File: dynamic/commentary/02-20-08-01.txt

**Errors:**
- Line 4: Duplicate range [1-181]
- Line 7: Duplicate range [1-181]
- Line 10: Duplicate range [1-181]
- Line 15: Duplicate range [1-181]
- Line 18: Duplicate range [1-181]
- Line 21: Duplicate range [1-181]
- Line 24: Duplicate range [1-181]
- Line 27: Duplicate range [1-181]
- Line 33: Duplicate range [1-181]
- Line 44: Duplicate range [1-181]
- Line 49: Duplicate range [1-181]
- Line 54: Duplicate range [1-181]
- Line 57: Duplicate range [1-181]
- Line 60: Duplicate range [1-181]

---

### File: dynamic/commentary/02-21-00-01.txt

**Errors:**
- Line 10: Duplicate range [1-300]
- Line 21: Duplicate range [1-300]
- Line 30: Duplicate range [1-300]
- Line 43: Duplicate range [1-300]
- Line 56: Duplicate range [1-300]
- Line 61: Duplicate range [1-300]
- Line 68: Duplicate range [1-300]
- Line 73: Duplicate range [1-300]
- Line 127: Duplicate range [1-300]
- Line 132: Duplicate range [1-300]
- Line 137: Duplicate range [1-300]
- Line 142: Duplicate range [1-300]
- Line 147: Duplicate range [1-300]

---

### File: dynamic/commentary/02-21-01-01.txt

**Errors:**
- Line 6: Duplicate range [1-498]
- Line 15: Duplicate range [1-498]
- Line 22: Duplicate range [1-498]
- Line 29: Duplicate range [1-498]
- Line 36: Duplicate range [1-498]
- Line 43: Duplicate range [1-498]
- Line 48: Duplicate range [1-498]
- Line 57: Duplicate range [1-498]
- Line 66: Duplicate range [1-498]
- Line 71: Duplicate range [1-498]
- Line 80: Duplicate range [1-498]
- Line 91: Duplicate range [1-498]
- Line 100: Duplicate range [1-498]
- Line 109: Duplicate range [1-498]
- Line 116: Duplicate range [1-498]
- Line 131: Duplicate range [1-498]
- Line 144: Duplicate range [1-498]
- Line 156: Duplicate range [1-498]
- Line 167: Duplicate range [1-498]
- Line 174: Duplicate range [1-498]
- Line 182: Duplicate range [1-498]
- Line 189: Duplicate range [1-498]
- Line 200: Duplicate range [1-498]
- Line 207: Duplicate range [1-498]
- Line 214: Duplicate range [1-498]
- Line 227: Duplicate range [1-498]
- Line 257: Duplicate range [1-498]
- Line 267: Duplicate range [1-498]
- Line 274: Duplicate range [1-498]
- Line 280: Duplicate range [1-498]
- Line 288: Duplicate range [1-498]
- Line 294: Duplicate range [1-498]
- Line 299: Duplicate range [1-498]
- Line 305: Duplicate range [1-498]
- Line 310: Duplicate range [1-498]
- Line 316: Duplicate range [1-498]
- Line 322: Duplicate range [1-498]
- Line 328: Duplicate range [1-498]
- Line 334: Duplicate range [1-498]
- Line 355: Duplicate range [1-498]

---

### File: dynamic/commentary/02-22-01-01.txt

**Errors:**
- Line 10: Duplicate range [1-555]
- Line 25: Duplicate range [1-555]
- Line 34: Duplicate range [1-555]
- Line 45: Duplicate range [1-555]
- Line 56: Duplicate range [1-555]
- Line 63: Duplicate range [1-555]
- Line 70: Duplicate range [1-555]
- Line 75: Duplicate range [1-555]
- Line 80: Duplicate range [1-555]
- Line 85: Duplicate range [1-555]
- Line 90: Duplicate range [1-555]
- Line 95: Duplicate range [1-555]
- Line 104: Duplicate range [1-555]
- Line 112: Duplicate range [1-555]
- Line 115: Duplicate range [1-555]
- Line 122: Duplicate range [1-555]
- Line 129: Duplicate range [1-555]
- Line 134: Duplicate range [1-555]
- Line 141: Duplicate range [1-555]
- Line 146: Duplicate range [1-555]
- Line 155: Duplicate range [1-555]
- Line 160: Duplicate range [1-555]
- Line 165: Duplicate range [1-555]
- Line 172: Duplicate range [1-555]
- Line 177: Duplicate range [1-555]
- Line 192: Duplicate range [1-555]
- Line 199: Duplicate range [1-555]
- Line 204: Duplicate range [1-555]
- Line 209: Duplicate range [1-555]
- Line 232: Duplicate range [1-555]
- Line 237: Duplicate range [1-555]
- Line 248: Duplicate range [1-555]
- Line 269: Duplicate range [1-555]
- Line 280: Duplicate range [1-555]
- Line 285: Duplicate range [1-555]

---

### File: dynamic/commentary/02-22-02-01.txt

**Errors:**
- Line 5: Duplicate range [1-60]
- Line 9: Duplicate range [1-60]
- Line 13: Duplicate range [1-60]
- Line 17: Duplicate range [1-60]
- Line 21: Duplicate range [1-60]
- Line 25: Duplicate range [1-60]

---

### File: dynamic/commentary/02-22-03-01.txt

**Errors:**
- Line 4: Duplicate range [1-74]
- Line 11: Duplicate range [1-74]
- Line 14: Duplicate range [1-74]
- Line 23: Duplicate range [1-74]
- Line 44: Duplicate range [1-74]
- Line 47: Duplicate range [1-74]
- Line 52: Duplicate range [1-74]
- Line 55: Duplicate range [1-74]

---

### File: dynamic/commentary/02-22-03-02.txt

**Errors:**
- Line 17: Duplicate range [1-282]
- Line 26: Duplicate range [1-282]
- Line 33: Duplicate range [1-282]
- Line 38: Duplicate range [1-282]
- Line 43: Duplicate range [1-282]
- Line 48: Duplicate range [1-282]
- Line 55: Duplicate range [1-282]
- Line 64: Duplicate range [1-282]
- Line 69: Duplicate range [1-282]
- Line 78: Duplicate range [1-282]
- Line 83: Duplicate range [1-282]
- Line 86: Duplicate range [1-282]
- Line 97: Duplicate range [1-282]
- Line 102: Duplicate range [1-282]
- Line 107: Duplicate range [1-282]
- Line 110: Duplicate range [1-282]
- Line 117: Duplicate range [1-282]
- Line 122: Duplicate range [1-282]
- Line 127: Duplicate range [1-282]
- Line 130: Duplicate range [1-282]
- Line 135: Duplicate range [1-282]
- Line 140: Duplicate range [1-282]
- Line 147: Duplicate range [1-282]
- Line 152: Duplicate range [1-282]

---

### File: dynamic/commentary/02-22-03-03.txt

**Errors:**
- Line 5: Duplicate range [1-140]
- Line 7: Duplicate range [1-140]
- Line 11: Duplicate range [1-140]
- Line 15: Duplicate range [1-140]
- Line 19: Duplicate range [1-140]
- Line 23: Duplicate range [1-140]
- Line 27: Duplicate range [1-140]
- Line 31: Duplicate range [1-140]
- Line 35: Duplicate range [1-140]
- Line 39: Duplicate range [1-140]
- Line 43: Duplicate range [1-140]
- Line 47: Duplicate range [1-140]
- Line 57: Duplicate range [1-140]
- Line 61: Duplicate range [1-140]
- Line 65: Duplicate range [1-140]
- Line 69: Duplicate range [1-140]

---

### File: dynamic/commentary/02-22-04-01.txt

**Errors:**
- Line 13: Duplicate range [1-158]
- Line 24: Duplicate range [1-158]
- Line 31: Duplicate range [1-158]
- Line 43: Duplicate range [1-158]
- Line 52: Duplicate range [1-158]
- Line 59: Duplicate range [1-158]
- Line 62: Duplicate range [1-158]
- Line 81: Duplicate range [1-158]
- Line 92: Duplicate range [1-158]
- Line 98: Duplicate range [1-158]
- Line 104: Duplicate range [1-158]
- Line 110: Duplicate range [1-158]
- Line 116: Duplicate range [1-158]
- Line 123: Duplicate range [1-158]
- Line 129: Duplicate range [1-158]
- Line 136: Duplicate range [1-158]
- Line 142: Duplicate range [1-158]

---

### File: dynamic/commentary/02-22-05-01.txt

**Errors:**
- Line 4: Duplicate range [1-256]
- Line 9: Duplicate range [1-256]
- Line 14: Duplicate range [1-256]
- Line 17: Duplicate range [1-256]
- Line 20: Duplicate range [1-256]
- Line 27: Duplicate range [1-256]
- Line 36: Duplicate range [1-256]
- Line 39: Duplicate range [1-256]
- Line 44: Duplicate range [1-256]
- Line 49: Duplicate range [1-256]
- Line 56: Duplicate range [1-256]
- Line 65: Duplicate range [1-256]
- Line 70: Duplicate range [1-256]
- Line 75: Duplicate range [1-256]
- Line 82: Duplicate range [1-256]
- Line 85: Duplicate range [1-256]
- Line 90: Duplicate range [1-256]
- Line 95: Duplicate range [1-256]
- Line 100: Duplicate range [1-256]
- Line 105: Duplicate range [1-256]
- Line 108: Duplicate range [1-256]
- Line 115: Duplicate range [1-256]
- Line 120: Duplicate range [1-256]
- Line 123: Duplicate range [1-256]
- Line 128: Duplicate range [1-256]
- Line 135: Duplicate range [1-256]
- Line 140: Duplicate range [1-256]
- Line 145: Duplicate range [1-256]
- Line 150: Duplicate range [1-256]
- Line 155: Duplicate range [1-256]
- Line 158: Duplicate range [1-256]
- Line 163: Duplicate range [1-256]
- Line 168: Duplicate range [1-256]
- Line 175: Duplicate range [1-256]
- Line 178: Duplicate range [1-256]
- Line 185: Duplicate range [1-256]
- Line 190: Duplicate range [1-256]
- Line 197: Duplicate range [1-256]
- Line 202: Duplicate range [1-256]
- Line 207: Duplicate range [1-256]
- Line 212: Duplicate range [1-256]
- Line 217: Duplicate range [1-256]

---

### File: dynamic/commentary/02-22-05-02.txt

**Errors:**
- Line 7: Duplicate range [1-89]
- Line 13: Duplicate range [1-89]
- Line 19: Duplicate range [1-89]
- Line 25: Duplicate range [1-89]

---

### File: dynamic/commentary/02-22-06-01.txt

**Errors:**
- Line 4: Duplicate range [1-178]
- Line 13: Duplicate range [1-178]
- Line 32: Duplicate range [1-178]

---

### File: dynamic/commentary/02-22-07-01.txt

**Errors:**
- Line 4: Duplicate range [1-8]
- Line 9: Duplicate range [1-8]
- Line 16: Duplicate range [1-8]
- Line 21: Duplicate range [1-8]

---

### File: dynamic/commentary/02-23-01-01.txt

**Errors:**
- Line 6: Duplicate range [1-234]
- Line 17: Duplicate range [1-234]
- Line 22: Duplicate range [1-234]
- Line 27: Duplicate range [1-234]
- Line 44: Duplicate range [1-234]
- Line 55: Duplicate range [1-234]
- Line 62: Duplicate range [1-234]

---

### File: dynamic/commentary/02-23-02-01.txt

**Errors:**
- Line 4: Duplicate range [1-106]
- Line 11: Duplicate range [1-106]
- Line 14: Duplicate range [1-106]
- Line 23: Duplicate range [1-106]
- Line 28: Duplicate range [1-106]
- Line 37: Duplicate range [1-106]
- Line 42: Duplicate range [1-106]
- Line 45: Duplicate range [1-106]
- Line 52: Duplicate range [1-106]
- Line 55: Duplicate range [1-106]
- Line 64: Duplicate range [1-106]
- Line 68: Duplicate range [1-106]
- Line 74: Duplicate range [1-106]
- Line 78: Duplicate range [1-106]
- Line 80: Duplicate range [1-106]
- Line 84: Duplicate range [1-106]
- Line 90: Duplicate range [1-106]
- Line 94: Duplicate range [1-106]
- Line 98: Duplicate range [1-106]
- Line 104: Duplicate range [1-106]
- Line 108: Duplicate range [1-106]
- Line 112: Duplicate range [1-106]
- Line 116: Duplicate range [1-106]
- Line 120: Duplicate range [1-106]

---

### File: dynamic/commentary/02-23-02-02.txt

**Errors:**
- Line 4: Duplicate range [1-171]
- Line 11: Duplicate range [1-171]
- Line 18: Duplicate range [1-171]
- Line 23: Duplicate range [1-171]
- Line 30: Duplicate range [1-171]
- Line 33: Duplicate range [1-171]
- Line 42: Duplicate range [1-171]
- Line 45: Duplicate range [1-171]
- Line 52: Duplicate range [1-171]
- Line 55: Duplicate range [1-171]
- Line 60: Duplicate range [1-171]
- Line 65: Duplicate range [1-171]
- Line 74: Duplicate range [1-171]
- Line 79: Duplicate range [1-171]
- Line 82: Duplicate range [1-171]
- Line 87: Duplicate range [1-171]
- Line 92: Duplicate range [1-171]

---

### File: dynamic/commentary/02-23-03-01.txt

**Errors:**
- Line 10: Duplicate range [1-257]
- Line 17: Duplicate range [1-257]
- Line 22: Duplicate range [1-257]
- Line 31: Duplicate range [1-257]
- Line 38: Duplicate range [1-257]
- Line 43: Duplicate range [1-257]
- Line 48: Duplicate range [1-257]
- Line 55: Duplicate range [1-257]
- Line 62: Duplicate range [1-257]
- Line 69: Duplicate range [1-257]
- Line 76: Duplicate range [1-257]
- Line 83: Duplicate range [1-257]
- Line 88: Duplicate range [1-257]
- Line 111: Duplicate range [1-257]

---

### File: dynamic/commentary/02-23-03-02.txt

**Errors:**
- Line 6: Duplicate range [1-525]
- Line 11: Duplicate range [1-525]
- Line 16: Duplicate range [1-525]
- Line 21: Duplicate range [1-525]
- Line 26: Duplicate range [1-525]
- Line 31: Duplicate range [1-525]
- Line 36: Duplicate range [1-525]
- Line 41: Duplicate range [1-525]
- Line 44: Duplicate range [1-525]
- Line 47: Duplicate range [1-525]
- Line 52: Duplicate range [1-525]
- Line 55: Duplicate range [1-525]
- Line 58: Duplicate range [1-525]
- Line 61: Duplicate range [1-525]
- Line 64: Duplicate range [1-525]
- Line 67: Duplicate range [1-525]
- Line 70: Duplicate range [1-525]
- Line 73: Duplicate range [1-525]
- Line 76: Duplicate range [1-525]
- Line 79: Duplicate range [1-525]
- Line 82: Duplicate range [1-525]
- Line 85: Duplicate range [1-525]
- Line 88: Duplicate range [1-525]
- Line 91: Duplicate range [1-525]
- Line 94: Duplicate range [1-525]
- Line 97: Duplicate range [1-525]
- Line 100: Duplicate range [1-525]
- Line 103: Duplicate range [1-525]
- Line 106: Duplicate range [1-525]
- Line 109: Duplicate range [1-525]
- Line 112: Duplicate range [1-525]
- Line 115: Duplicate range [1-525]
- Line 118: Duplicate range [1-525]
- Line 121: Duplicate range [1-525]
- Line 124: Duplicate range [1-525]
- Line 127: Duplicate range [1-525]
- Line 130: Duplicate range [1-525]
- Line 133: Duplicate range [1-525]
- Line 136: Duplicate range [1-525]
- Line 139: Duplicate range [1-525]
- Line 142: Duplicate range [1-525]
- Line 145: Duplicate range [1-525]
- Line 148: Duplicate range [1-525]
- Line 151: Duplicate range [1-525]
- Line 154: Duplicate range [1-525]
- Line 157: Duplicate range [1-525]
- Line 160: Duplicate range [1-525]
- Line 163: Duplicate range [1-525]
- Line 170: Duplicate range [1-525]
- Line 175: Duplicate range [1-525]
- Line 186: Duplicate range [1-525]
- Line 198: Duplicate range [1-525]
- Line 201: Duplicate range [1-525]
- Line 218: Duplicate range [1-525]
- Line 227: Duplicate range [1-525]
- Line 236: Duplicate range [1-525]
- Line 243: Duplicate range [1-525]
- Line 257: Duplicate range [1-525]

---

### File: dynamic/commentary/02-23-04-01.txt

**Errors:**
- Line 5: Duplicate range [1-391]
- Line 9: Duplicate range [1-391]
- Line 13: Duplicate range [1-391]
- Line 17: Duplicate range [1-391]
- Line 21: Duplicate range [1-391]
- Line 25: Duplicate range [1-391]
- Line 29: Duplicate range [1-391]
- Line 33: Duplicate range [1-391]
- Line 37: Duplicate range [1-391]
- Line 41: Duplicate range [1-391]
- Line 45: Duplicate range [1-391]
- Line 49: Duplicate range [1-391]
- Line 53: Duplicate range [1-391]
- Line 57: Duplicate range [1-391]
- Line 63: Duplicate range [1-391]
- Line 65: Duplicate range [1-391]
- Line 69: Duplicate range [1-391]
- Line 73: Duplicate range [1-391]
- Line 77: Duplicate range [1-391]
- Line 81: Duplicate range [1-391]
- Line 85: Duplicate range [1-391]
- Line 89: Duplicate range [1-391]
- Line 95: Duplicate range [1-391]
- Line 97: Duplicate range [1-391]
- Line 101: Duplicate range [1-391]
- Line 103: Duplicate range [1-391]
- Line 107: Duplicate range [1-391]
- Line 111: Duplicate range [1-391]
- Line 115: Duplicate range [1-391]
- Line 119: Duplicate range [1-391]
- Line 123: Duplicate range [1-391]
- Line 127: Duplicate range [1-391]
- Line 129: Duplicate range [1-391]
- Line 133: Duplicate range [1-391]
- Line 139: Duplicate range [1-391]
- Line 141: Duplicate range [1-391]
- Line 145: Duplicate range [1-391]
- Line 149: Duplicate range [1-391]
- Line 153: Duplicate range [1-391]
- Line 157: Duplicate range [1-391]
- Line 161: Duplicate range [1-391]
- Line 165: Duplicate range [1-391]
- Line 169: Duplicate range [1-391]
- Line 173: Duplicate range [1-391]
- Line 177: Duplicate range [1-391]
- Line 181: Duplicate range [1-391]
- Line 185: Duplicate range [1-391]
- Line 189: Duplicate range [1-391]
- Line 193: Duplicate range [1-391]
- Line 197: Duplicate range [1-391]
- Line 201: Duplicate range [1-391]
- Line 205: Duplicate range [1-391]
- Line 209: Duplicate range [1-391]
- Line 213: Duplicate range [1-391]
- Line 217: Duplicate range [1-391]
- Line 221: Duplicate range [1-391]
- Line 225: Duplicate range [1-391]
- Line 231: Duplicate range [1-391]
- Line 235: Duplicate range [1-391]
- Line 239: Duplicate range [1-391]
- Line 243: Duplicate range [1-391]
- Line 247: Duplicate range [1-391]
- Line 250: Duplicate range [1-391]
- Line 254: Duplicate range [1-391]
- Line 258: Duplicate range [1-391]
- Line 262: Duplicate range [1-391]
- Line 266: Duplicate range [1-391]
- Line 270: Duplicate range [1-391]
- Line 274: Duplicate range [1-391]
- Line 278: Duplicate range [1-391]

---

### File: dynamic/commentary/02-23-05-01.txt

**Errors:**
- Line 11: Duplicate range [1-6]

---

### File: dynamic/commentary/02-23-06-01.txt

**Errors:**
- Line 6: Duplicate range [1-499]
- Line 13: Duplicate range [1-499]
- Line 18: Duplicate range [1-499]
- Line 23: Duplicate range [1-499]
- Line 26: Duplicate range [1-499]
- Line 35: Duplicate range [1-499]
- Line 40: Duplicate range [1-499]
- Line 47: Duplicate range [1-499]
- Line 52: Duplicate range [1-499]
- Line 61: Duplicate range [1-499]
- Line 66: Duplicate range [1-499]
- Line 69: Duplicate range [1-499]
- Line 76: Duplicate range [1-499]
- Line 85: Duplicate range [1-499]
- Line 90: Duplicate range [1-499]
- Line 95: Duplicate range [1-499]
- Line 100: Duplicate range [1-499]
- Line 107: Duplicate range [1-499]
- Line 112: Duplicate range [1-499]
- Line 119: Duplicate range [1-499]
- Line 122: Duplicate range [1-499]
- Line 127: Duplicate range [1-499]
- Line 136: Duplicate range [1-499]
- Line 143: Duplicate range [1-499]
- Line 148: Duplicate range [1-499]
- Line 157: Duplicate range [1-499]
- Line 162: Duplicate range [1-499]
- Line 169: Duplicate range [1-499]
- Line 174: Duplicate range [1-499]
- Line 183: Duplicate range [1-499]
- Line 192: Duplicate range [1-499]
- Line 197: Duplicate range [1-499]
- Line 202: Duplicate range [1-499]
- Line 207: Duplicate range [1-499]
- Line 210: Duplicate range [1-499]
- Line 217: Duplicate range [1-499]
- Line 234: Duplicate range [1-499]
- Line 239: Duplicate range [1-499]
- Line 242: Duplicate range [1-499]
- Line 247: Duplicate range [1-499]
- Line 252: Duplicate range [1-499]
- Line 259: Duplicate range [1-499]
- Line 268: Duplicate range [1-499]
- Line 273: Duplicate range [1-499]
- Line 283: Duplicate range [1-499]
- Line 292: Duplicate range [1-499]
- Line 297: Duplicate range [1-499]
- Line 304: Duplicate range [1-499]
- Line 307: Duplicate range [1-499]
- Line 316: Duplicate range [1-499]
- Line 321: Duplicate range [1-499]
- Line 328: Duplicate range [1-499]
- Line 333: Duplicate range [1-499]
- Line 338: Duplicate range [1-499]
- Line 347: Duplicate range [1-499]
- Line 352: Duplicate range [1-499]
- Line 359: Duplicate range [1-499]
- Line 364: Duplicate range [1-499]
- Line 369: Duplicate range [1-499]
- Line 372: Duplicate range [1-499]
- Line 381: Duplicate range [1-499]
- Line 386: Duplicate range [1-499]
- Line 393: Duplicate range [1-499]
- Line 404: Duplicate range [1-499]
- Line 409: Duplicate range [1-499]
- Line 422: Duplicate range [1-499]
- Line 429: Duplicate range [1-499]
- Line 436: Duplicate range [1-499]
- Line 441: Duplicate range [1-499]
- Line 454: Duplicate range [1-499]
- Line 459: Duplicate range [1-499]
- Line 464: Duplicate range [1-499]
- Line 473: Duplicate range [1-499]
- Line 482: Duplicate range [1-499]
- Line 493: Duplicate range [1-499]
- Line 500: Duplicate range [1-499]
- Line 509: Duplicate range [1-499]
- Line 518: Duplicate range [1-499]
- Line 525: Duplicate range [1-499]
- Line 530: Duplicate range [1-499]
- Line 535: Duplicate range [1-499]
- Line 544: Duplicate range [1-499]
- Line 551: Duplicate range [1-499]
- Line 554: Duplicate range [1-499]
- Line 559: Duplicate range [1-499]
- Line 566: Duplicate range [1-499]
- Line 571: Duplicate range [1-499]
- Line 576: Duplicate range [1-499]
- Line 583: Duplicate range [1-499]
- Line 590: Duplicate range [1-499]
- Line 595: Duplicate range [1-499]
- Line 604: Duplicate range [1-499]
- Line 613: Duplicate range [1-499]
- Line 620: Duplicate range [1-499]
- Line 625: Duplicate range [1-499]
- Line 632: Duplicate range [1-499]
- Line 637: Duplicate range [1-499]
- Line 650: Duplicate range [1-499]
- Line 655: Duplicate range [1-499]
- Line 662: Duplicate range [1-499]
- Line 669: Duplicate range [1-499]
- Line 678: Duplicate range [1-499]
- Line 687: Duplicate range [1-499]
- Line 696: Duplicate range [1-499]
- Line 701: Duplicate range [1-499]
- Line 708: Duplicate range [1-499]
- Line 713: Duplicate range [1-499]
- Line 720: Duplicate range [1-499]
- Line 725: Duplicate range [1-499]
- Line 734: Duplicate range [1-499]
- Line 737: Duplicate range [1-499]
- Line 744: Duplicate range [1-499]
- Line 751: Duplicate range [1-499]
- Line 758: Duplicate range [1-499]
- Line 765: Duplicate range [1-499]
- Line 772: Duplicate range [1-499]
- Line 779: Duplicate range [1-499]
- Line 786: Duplicate range [1-499]
- Line 789: Duplicate range [1-499]
- Line 796: Duplicate range [1-499]
- Line 803: Duplicate range [1-499]
- Line 808: Duplicate range [1-499]
- Line 812: Duplicate range [1-499]
- Line 816: Duplicate range [1-499]
- Line 820: Duplicate range [1-499]
- Line 824: Duplicate range [1-499]
- Line 828: Duplicate range [1-499]

---

### File: dynamic/commentary/02-23-06-02.txt

**Errors:**
- Line 4: Duplicate range [1-78]
- Line 9: Duplicate range [1-78]
- Line 14: Duplicate range [1-78]
- Line 19: Duplicate range [1-78]
- Line 26: Duplicate range [1-78]
- Line 31: Duplicate range [1-78]
- Line 38: Duplicate range [1-78]
- Line 43: Duplicate range [1-78]
- Line 50: Duplicate range [1-78]
- Line 55: Duplicate range [1-78]
- Line 60: Duplicate range [1-78]
- Line 67: Duplicate range [1-78]
- Line 76: Duplicate range [1-78]
- Line 83: Duplicate range [1-78]
- Line 94: Duplicate range [1-78]
- Line 111: Duplicate range [1-78]
- Line 116: Duplicate range [1-78]
- Line 121: Duplicate range [1-78]
- Line 126: Duplicate range [1-78]
- Line 131: Duplicate range [1-78]
- Line 140: Duplicate range [1-78]
- Line 151: Duplicate range [1-78]

---

### File: dynamic/commentary/02-23-07-01.txt

**Errors:**
- Line 4: Duplicate range [1-310]
- Line 18: Duplicate range [1-310]
- Line 27: Duplicate range [1-310]
- Line 32: Duplicate range [1-310]
- Line 39: Duplicate range [1-310]
- Line 42: Duplicate range [1-310]
- Line 51: Duplicate range [1-310]
- Line 58: Duplicate range [1-310]
- Line 67: Duplicate range [1-310]
- Line 74: Duplicate range [1-310]
- Line 83: Duplicate range [1-310]
- Line 90: Duplicate range [1-310]
- Line 99: Duplicate range [1-310]
- Line 106: Duplicate range [1-310]
- Line 115: Duplicate range [1-310]
- Line 124: Duplicate range [1-310]
- Line 133: Duplicate range [1-310]
- Line 138: Duplicate range [1-310]
- Line 145: Duplicate range [1-310]
- Line 154: Duplicate range [1-310]
- Line 161: Duplicate range [1-310]
- Line 170: Duplicate range [1-310]
- Line 181: Duplicate range [1-310]
- Line 186: Duplicate range [1-310]
- Line 189: Duplicate range [1-310]
- Line 196: Duplicate range [1-310]
- Line 205: Duplicate range [1-310]
- Line 210: Duplicate range [1-310]
- Line 217: Duplicate range [1-310]
- Line 222: Duplicate range [1-310]
- Line 235: Duplicate range [1-310]
- Line 242: Duplicate range [1-310]
- Line 247: Duplicate range [1-310]
- Line 250: Duplicate range [1-310]
- Line 255: Duplicate range [1-310]
- Line 262: Duplicate range [1-310]
- Line 267: Duplicate range [1-310]
- Line 276: Duplicate range [1-310]
- Line 281: Duplicate range [1-310]
- Line 286: Duplicate range [1-310]
- Line 293: Duplicate range [1-310]
- Line 298: Duplicate range [1-310]
- Line 305: Duplicate range [1-310]
- Line 310: Duplicate range [1-310]
- Line 319: Duplicate range [1-310]
- Line 324: Duplicate range [1-310]
- Line 329: Duplicate range [1-310]
- Line 336: Duplicate range [1-310]
- Line 345: Duplicate range [1-310]
- Line 352: Duplicate range [1-310]
- Line 357: Duplicate range [1-310]
- Line 366: Duplicate range [1-310]
- Line 371: Duplicate range [1-310]
- Line 374: Duplicate range [1-310]
- Line 379: Duplicate range [1-310]
- Line 384: Duplicate range [1-310]
- Line 393: Duplicate range [1-310]
- Line 400: Duplicate range [1-310]
- Line 405: Duplicate range [1-310]
- Line 412: Duplicate range [1-310]
- Line 419: Duplicate range [1-310]
- Line 424: Duplicate range [1-310]
- Line 433: Duplicate range [1-310]
- Line 442: Duplicate range [1-310]

---

### File: dynamic/commentary/02-23-08-01.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 15: Duplicate range [1-1]

---

### File: dynamic/commentary/02-23-08-02.txt

**Errors:**
- Line 3: Duplicate range [1-1]

---

### File: dynamic/commentary/02-23-08-03.txt

**Errors:**
- Line 4: Duplicate range [1-50]
- Line 7: Duplicate range [1-50]
- Line 13: Duplicate range [1-50]
- Line 16: Duplicate range [1-50]
- Line 19: Duplicate range [1-50]
- Line 22: Duplicate range [1-50]
- Line 25: Duplicate range [1-50]
- Line 28: Duplicate range [1-50]
- Line 31: Duplicate range [1-50]
- Line 34: Duplicate range [1-50]
- Line 37: Duplicate range [1-50]
- Line 40: Duplicate range [1-50]
- Line 43: Duplicate range [1-50]
- Line 46: Duplicate range [1-50]
- Line 52: Duplicate range [1-50]
- Line 58: Duplicate range [1-50]
- Line 61: Duplicate range [1-50]

---

### File: dynamic/commentary/02-23-08-04.txt

**Errors:**
- Line 6: Duplicate range [1-2]
- Line 11: Duplicate range [1-2]
- Line 15: Duplicate range [1-2]

---

### File: dynamic/commentary/02-23-08-05.txt

**Errors:**
- Line 8: Duplicate range [1-108]
- Line 15: Duplicate range [1-108]
- Line 20: Duplicate range [1-108]
- Line 25: Duplicate range [1-108]
- Line 30: Duplicate range [1-108]
- Line 35: Duplicate range [1-108]

---

### File: dynamic/commentary/02-23-08-06.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 15: Duplicate range [1-1]

---

### File: dynamic/commentary/02-23-08-07.txt

**Errors:**
- Line 6: Duplicate range [1-1]
- Line 11: Duplicate range [1-1]
- Line 14: Duplicate range [1-1]

---

### File: dynamic/commentary/02-23-08-08.txt

**Errors:**
- Line 8: Duplicate range [1-1]

---

### File: dynamic/commentary/02-23-08-09.txt

**Errors:**
- Line 5: Duplicate range [1-70]
- Line 7: Duplicate range [1-70]
- Line 11: Duplicate range [1-70]
- Line 15: Duplicate range [1-70]
- Line 19: Duplicate range [1-70]
- Line 23: Duplicate range [1-70]
- Line 27: Duplicate range [1-70]
- Line 31: Duplicate range [1-70]
- Line 35: Duplicate range [1-70]
- Line 39: Duplicate range [1-70]
- Line 43: Duplicate range [1-70]

---

### File: dynamic/commentary/02-23-09-01.txt

**Errors:**
- Line 4: Duplicate range [1-452]
- Line 13: Duplicate range [1-452]
- Line 20: Duplicate range [1-452]
- Line 27: Duplicate range [1-452]
- Line 42: Duplicate range [1-452]
- Line 53: Duplicate range [1-452]
- Line 62: Duplicate range [1-452]
- Line 81: Duplicate range [1-452]
- Line 88: Duplicate range [1-452]
- Line 93: Duplicate range [1-452]
- Line 104: Duplicate range [1-452]
- Line 109: Duplicate range [1-452]
- Line 118: Duplicate range [1-452]
- Line 129: Duplicate range [1-452]
- Line 136: Duplicate range [1-452]
- Line 143: Duplicate range [1-452]
- Line 152: Duplicate range [1-452]
- Line 157: Duplicate range [1-452]
- Line 164: Duplicate range [1-452]
- Line 171: Duplicate range [1-452]
- Line 176: Duplicate range [1-452]
- Line 189: Duplicate range [1-452]
- Line 194: Duplicate range [1-452]
- Line 201: Duplicate range [1-452]
- Line 210: Duplicate range [1-452]
- Line 215: Duplicate range [1-452]
- Line 222: Duplicate range [1-452]
- Line 227: Duplicate range [1-452]
- Line 232: Duplicate range [1-452]
- Line 237: Duplicate range [1-452]
- Line 244: Duplicate range [1-452]
- Line 249: Duplicate range [1-452]
- Line 260: Duplicate range [1-452]
- Line 269: Duplicate range [1-452]
- Line 280: Duplicate range [1-452]
- Line 287: Duplicate range [1-452]
- Line 294: Duplicate range [1-452]
- Line 303: Duplicate range [1-452]
- Line 306: Duplicate range [1-452]
- Line 317: Duplicate range [1-452]
- Line 324: Duplicate range [1-452]
- Line 329: Duplicate range [1-452]
- Line 334: Duplicate range [1-452]
- Line 341: Duplicate range [1-452]
- Line 350: Duplicate range [1-452]
- Line 355: Duplicate range [1-452]
- Line 364: Duplicate range [1-452]
- Line 373: Duplicate range [1-452]
- Line 378: Duplicate range [1-452]
- Line 383: Duplicate range [1-452]
- Line 394: Duplicate range [1-452]
- Line 403: Duplicate range [1-452]
- Line 412: Duplicate range [1-452]
- Line 417: Duplicate range [1-452]
- Line 422: Duplicate range [1-452]
- Line 427: Duplicate range [1-452]
- Line 432: Duplicate range [1-452]
- Line 437: Duplicate range [1-452]
- Line 442: Duplicate range [1-452]
- Line 447: Duplicate range [1-452]
- Line 452: Duplicate range [1-452]
- Line 463: Duplicate range [1-452]
- Line 470: Duplicate range [1-452]
- Line 477: Duplicate range [1-452]
- Line 484: Duplicate range [1-452]
- Line 489: Duplicate range [1-452]
- Line 498: Duplicate range [1-452]
- Line 505: Duplicate range [1-452]
- Line 514: Duplicate range [1-452]

---

### File: dynamic/commentary/02-24-01-01.txt

**Errors:**
- Line 4: Duplicate range [1-360]
- Line 11: Duplicate range [1-360]
- Line 24: Duplicate range [1-360]
- Line 33: Duplicate range [1-360]
- Line 38: Duplicate range [1-360]
- Line 53: Duplicate range [1-360]
- Line 58: Duplicate range [1-360]
- Line 65: Duplicate range [1-360]
- Line 70: Duplicate range [1-360]
- Line 75: Duplicate range [1-360]
- Line 86: Duplicate range [1-360]
- Line 95: Duplicate range [1-360]
- Line 102: Duplicate range [1-360]
- Line 113: Duplicate range [1-360]
- Line 124: Duplicate range [1-360]
- Line 133: Duplicate range [1-360]
- Line 138: Duplicate range [1-360]
- Line 147: Duplicate range [1-360]
- Line 156: Duplicate range [1-360]
- Line 165: Duplicate range [1-360]
- Line 172: Duplicate range [1-360]
- Line 179: Duplicate range [1-360]
- Line 184: Duplicate range [1-360]
- Line 193: Duplicate range [1-360]
- Line 198: Duplicate range [1-360]
- Line 203: Duplicate range [1-360]
- Line 212: Duplicate range [1-360]
- Line 221: Duplicate range [1-360]
- Line 230: Duplicate range [1-360]
- Line 237: Duplicate range [1-360]
- Line 246: Duplicate range [1-360]
- Line 253: Duplicate range [1-360]
- Line 258: Duplicate range [1-360]
- Line 263: Duplicate range [1-360]
- Line 270: Duplicate range [1-360]
- Line 279: Duplicate range [1-360]
- Line 294: Duplicate range [1-360]
- Line 299: Duplicate range [1-360]
- Line 324: Duplicate range [1-360]
- Line 335: Duplicate range [1-360]
- Line 348: Duplicate range [1-360]
- Line 351: Duplicate range [1-360]
- Line 356: Duplicate range [1-360]
- Line 391: Duplicate range [1-360]
- Line 410: Duplicate range [1-360]
- Line 415: Duplicate range [1-360]
- Line 424: Duplicate range [1-360]
- Line 443: Duplicate range [1-360]
- Line 448: Duplicate range [1-360]
- Line 453: Duplicate range [1-360]
- Line 476: Duplicate range [1-360]
- Line 481: Duplicate range [1-360]
- Line 484: Duplicate range [1-360]
- Line 505: Duplicate range [1-360]
- Line 510: Duplicate range [1-360]
- Line 521: Duplicate range [1-360]

---

### File: dynamic/commentary/02-25-01-01.txt

**Errors:**
- Line 8: Duplicate range [1-694]
- Line 15: Duplicate range [1-694]
- Line 22: Duplicate range [1-694]
- Line 28: Duplicate range [1-694]
- Line 34: Duplicate range [1-694]
- Line 41: Duplicate range [1-694]
- Line 47: Duplicate range [1-694]
- Line 53: Duplicate range [1-694]
- Line 59: Duplicate range [1-694]
- Line 65: Duplicate range [1-694]
- Line 71: Duplicate range [1-694]
- Line 77: Duplicate range [1-694]
- Line 89: Duplicate range [1-694]
- Line 96: Duplicate range [1-694]
- Line 103: Duplicate range [1-694]
- Line 109: Duplicate range [1-694]
- Line 115: Duplicate range [1-694]
- Line 121: Duplicate range [1-694]
- Line 127: Duplicate range [1-694]
- Line 134: Duplicate range [1-694]
- Line 140: Duplicate range [1-694]
- Line 146: Duplicate range [1-694]
- Line 158: Duplicate range [1-694]
- Line 166: Duplicate range [1-694]
- Line 173: Duplicate range [1-694]
- Line 179: Duplicate range [1-694]
- Line 185: Duplicate range [1-694]
- Line 189: Duplicate range [1-694]
- Line 193: Duplicate range [1-694]
- Line 197: Duplicate range [1-694]
- Line 201: Duplicate range [1-694]
- Line 205: Duplicate range [1-694]
- Line 209: Duplicate range [1-694]
- Line 213: Duplicate range [1-694]
- Line 217: Duplicate range [1-694]
- Line 221: Duplicate range [1-694]
- Line 229: Duplicate range [1-694]
- Line 247: Duplicate range [1-694]
- Line 253: Duplicate range [1-694]
- Line 259: Duplicate range [1-694]
- Line 264: Duplicate range [1-694]
- Line 278: Duplicate range [1-694]
- Line 284: Duplicate range [1-694]
- Line 288: Duplicate range [1-694]
- Line 292: Duplicate range [1-694]
- Line 296: Duplicate range [1-694]
- Line 300: Duplicate range [1-694]
- Line 304: Duplicate range [1-694]
- Line 308: Duplicate range [1-694]
- Line 312: Duplicate range [1-694]
- Line 323: Duplicate range [1-694]
- Line 334: Duplicate range [1-694]
- Line 358: Duplicate range [1-694]
- Line 405: Duplicate range [1-694]
- Line 420: Duplicate range [1-694]
- Line 457: Duplicate range [1-694]
- Line 514: Duplicate range [1-694]
- Line 552: Duplicate range [1-694]

---

### File: dynamic/commentary/02-25-02-01.txt

**Errors:**
- Line 4: Duplicate range [1-31]
- Line 9: Duplicate range [1-31]
- Line 14: Duplicate range [1-31]

---

### File: dynamic/commentary/02-25-03-01.txt

**Errors:**
- Line 4: Duplicate range [1-49]
- Line 9: Duplicate range [1-49]
- Line 12: Duplicate range [1-49]
- Line 21: Duplicate range [1-49]
- Line 26: Duplicate range [1-49]

---

### File: dynamic/commentary/02-25-04-01.txt

**Errors:**
- Line 4: Duplicate range [1-27]
- Line 11: Duplicate range [1-27]
- Line 16: Duplicate range [1-27]
- Line 19: Duplicate range [1-27]

---

### File: dynamic/commentary/02-25-05-01.txt

**Errors:**
- Line 4: Duplicate range [1-283]
- Line 9: Duplicate range [1-283]
- Line 16: Duplicate range [1-283]
- Line 21: Duplicate range [1-283]
- Line 26: Duplicate range [1-283]
- Line 32: Duplicate range [1-283]
- Line 38: Duplicate range [1-283]
- Line 43: Duplicate range [1-283]
- Line 50: Duplicate range [1-283]
- Line 57: Duplicate range [1-283]
- Line 68: Duplicate range [1-283]
- Line 75: Duplicate range [1-283]
- Line 90: Duplicate range [1-283]
- Line 105: Duplicate range [1-283]
- Line 134: Duplicate range [1-283]
- Line 157: Duplicate range [1-283]
- Line 169: Duplicate range [1-283]
- Line 213: Duplicate range [1-283]
- Line 229: Duplicate range [1-283]
- Line 258: Duplicate range [1-283]

---

### File: dynamic/commentary/02-25-06-01.txt

**Errors:**
- Line 4: Duplicate range [1-51]
- Line 20: Duplicate range [1-51]
- Line 30: Duplicate range [1-51]
- Line 35: Duplicate range [1-51]

---

### File: dynamic/commentary/02-25-06-02.txt

**Errors:**
- Line 41: Duplicate range [1-202]
- Line 75: Duplicate range [1-202]
- Line 80: Duplicate range [1-202]
- Line 99: Duplicate range [1-202]
- Line 129: Duplicate range [1-202]
- Line 150: Duplicate range [1-202]
- Line 179: Duplicate range [1-202]
- Line 186: Duplicate range [1-202]
- Line 209: Duplicate range [1-202]
- Line 259: Duplicate range [1-202]
- Line 309: Duplicate range [1-202]
- Line 326: Duplicate range [1-202]
- Line 342: Duplicate range [1-202]

---

### File: dynamic/commentary/02-25-07-01.txt

**Errors:**
- Line 8: Duplicate range [1-359]
- Line 34: Duplicate range [1-359]
- Line 43: Duplicate range [1-359]
- Line 71: Duplicate range [1-359]
- Line 92: Duplicate range [1-359]
- Line 112: Duplicate range [1-359]
- Line 124: Duplicate range [1-359]
- Line 144: Duplicate range [1-359]
- Line 152: Duplicate range [1-359]
- Line 165: Duplicate range [1-359]
- Line 181: Duplicate range [1-359]
- Line 203: Duplicate range [1-359]
- Line 210: Duplicate range [1-359]
- Line 217: Duplicate range [1-359]
- Line 224: Duplicate range [1-359]
- Line 229: Duplicate range [1-359]
- Line 238: Duplicate range [1-359]
- Line 245: Duplicate range [1-359]
- Line 250: Duplicate range [1-359]
- Line 255: Duplicate range [1-359]
- Line 262: Duplicate range [1-359]
- Line 269: Duplicate range [1-359]
- Line 276: Duplicate range [1-359]
- Line 287: Duplicate range [1-359]
- Line 294: Duplicate range [1-359]
- Line 301: Duplicate range [1-359]
- Line 306: Duplicate range [1-359]
- Line 313: Duplicate range [1-359]
- Line 318: Duplicate range [1-359]
- Line 323: Duplicate range [1-359]
- Line 328: Duplicate range [1-359]
- Line 335: Duplicate range [1-359]
- Line 342: Duplicate range [1-359]
- Line 347: Duplicate range [1-359]
- Line 354: Duplicate range [1-359]
- Line 361: Duplicate range [1-359]
- Line 368: Duplicate range [1-359]

---

### File: dynamic/commentary_BACKUP/01-01-01-01.txt

**Errors:**
- Line 190: Non-sequential range [1-80] - Start (1) < Previous start (169)
- Line 220: Non-sequential range [1-189] - Start (1) < Previous start (161)
- Line 192: Duplicate range [1-80]
- Line 194: Duplicate range [1-80]
- Line 196: Duplicate range [1-80]
- Line 200: Duplicate range [81-120]
- Line 202: Duplicate range [81-120]
- Line 204: Duplicate range [81-120]
- Line 208: Duplicate range [121-160]
- Line 210: Duplicate range [121-160]
- Line 212: Duplicate range [121-160]
- Line 216: Duplicate range [161-189]
- Line 218: Duplicate range [161-189]
- Line 222: Duplicate range [1-189]
- Line 224: Duplicate range [1-189]
- Line 226: Duplicate range [1-189]
- Line 228: Duplicate range [1-189]
- Line 230: Duplicate range [1-189]
- Line 232: Duplicate range [1-189]
- Line 234: Duplicate range [1-189]
- Line 236: Duplicate range [1-189]
- Line 238: Duplicate range [1-189]
- Line 240: Duplicate range [1-189]
- Line 242: Duplicate range [1-189]
- Line 244: Duplicate range [1-189]
- Line 246: Duplicate range [1-189]
- Line 248: Duplicate range [1-189]
- Line 250: Duplicate range [1-189]
- Line 252: Duplicate range [1-189]
- Line 254: Duplicate range [1-189]
- Line 256: Duplicate range [1-189]
- Line 258: Duplicate range [1-189]
- Line 260: Duplicate range [1-189]
- Line 262: Duplicate range [1-189]
- Line 264: Duplicate range [1-189]
- Line 266: Duplicate range [1-189]
- Line 268: Duplicate range [1-189]
- Line 270: Duplicate range [1-189]
- Line 272: Duplicate range [1-189]
- Line 274: Duplicate range [1-189]
- Line 276: Duplicate range [1-189]
- Line 278: Duplicate range [1-189]
- Line 280: Duplicate range [1-189]
- Line 282: Duplicate range [1-189]
- Line 284: Duplicate range [1-189]
- Line 286: Duplicate range [1-80]
- Line 288: Duplicate range [12-15]
- Line 290: Duplicate range [12-15]
- Line 292: Duplicate range [16-19]
- Line 294: Duplicate range [16-19]
- Line 296: Duplicate range [20-23]
- Line 298: Duplicate range [20-23]
- Line 300: Duplicate range [24-27]
- Line 302: Duplicate range [24-27]
- Line 306: Duplicate range [28-36]
- Line 310: Duplicate range [37-80]
- Line 312: Duplicate range [37-80]
- Line 314: Duplicate range [37-80]
- Line 316: Duplicate range [37-80]
- Line 318: Duplicate range [37-80]

---

### File: dynamic/commentary_BACKUP/01-01-03-01.txt

**Errors:**
- Line 30: Non-sequential range [578-634] - Start (578) < Previous start (619)
- Line 8: Duplicate range [578-583]
- Line 13: Duplicate range [578-583]
- Line 39: Duplicate range [578-578]
- Line 42: Duplicate range [578-578]
- Line 45: Duplicate range [578-578]
- Line 48: Duplicate range [578-578]

---

### File: dynamic/commentary_BACKUP/01-02-01-05.txt

**Errors:**
- Line 351: Non-sequential range [999-1005] - Start (999) < Previous start (1541)
- Line 486: Non-sequential range [999-1560] - Start (999) < Previous start (1541)
- Line 626: Non-sequential range [999-1560] - Start (999) < Previous start (1541)
- Line 766: Non-sequential range [999-1560] - Start (999) < Previous start (1541)
- Line 11: Duplicate range [1006-1012]
- Line 21: Duplicate range [1013-1026]
- Line 31: Duplicate range [1027-1041]
- Line 46: Duplicate range [1055-1061]
- Line 56: Duplicate range [1062-1076]
- Line 66: Duplicate range [1077-1096]
- Line 71: Duplicate range [1077-1096]
- Line 81: Duplicate range [1097-1118]
- Line 86: Duplicate range [1097-1118]
- Line 96: Duplicate range [1119-1140]
- Line 101: Duplicate range [1119-1140]
- Line 111: Duplicate range [1141-1164]
- Line 116: Duplicate range [1141-1164]
- Line 121: Duplicate range [1141-1164]
- Line 131: Duplicate range [1165-1188]
- Line 136: Duplicate range [1165-1188]
- Line 146: Duplicate range [1189-1210]
- Line 151: Duplicate range [1189-1210]
- Line 161: Duplicate range [1211-1236]
- Line 166: Duplicate range [1211-1236]
- Line 171: Duplicate range [1211-1236]
- Line 181: Duplicate range [1237-1260]
- Line 191: Duplicate range [1261-1296]
- Line 196: Duplicate range [1261-1296]
- Line 206: Duplicate range [1297-1322]
- Line 216: Duplicate range [1323-1350]
- Line 221: Duplicate range [1323-1350]
- Line 231: Duplicate range [1351-1400]
- Line 236: Duplicate range [1351-1400]
- Line 246: Duplicate range [1401-1423]
- Line 251: Duplicate range [1401-1423]
- Line 261: Duplicate range [1424-1448]
- Line 266: Duplicate range [1424-1448]
- Line 276: Duplicate range [1449-1460]
- Line 281: Duplicate range [1449-1460]
- Line 291: Duplicate range [1461-1478]
- Line 296: Duplicate range [1461-1478]
- Line 306: Duplicate range [1479-1500]
- Line 311: Duplicate range [1479-1500]
- Line 321: Duplicate range [1501-1520]
- Line 326: Duplicate range [1501-1520]
- Line 336: Duplicate range [1521-1540]
- Line 341: Duplicate range [1521-1540]
- Line 351: Duplicate range [999-1005]
- Line 356: Duplicate range [1006-1012]
- Line 361: Duplicate range [1013-1026]
- Line 366: Duplicate range [1027-1041]
- Line 371: Duplicate range [1042-1054]
- Line 376: Duplicate range [1055-1061]
- Line 381: Duplicate range [1062-1076]
- Line 386: Duplicate range [1077-1096]
- Line 391: Duplicate range [1097-1118]
- Line 396: Duplicate range [1119-1140]
- Line 401: Duplicate range [1141-1164]
- Line 406: Duplicate range [1165-1188]
- Line 411: Duplicate range [1189-1210]
- Line 416: Duplicate range [1211-1236]
- Line 421: Duplicate range [1237-1260]
- Line 426: Duplicate range [1261-1296]
- Line 431: Duplicate range [1297-1322]
- Line 436: Duplicate range [1323-1350]
- Line 441: Duplicate range [1351-1400]
- Line 446: Duplicate range [1401-1423]
- Line 451: Duplicate range [1424-1448]
- Line 466: Duplicate range [1479-1500]
- Line 471: Duplicate range [1501-1520]
- Line 476: Duplicate range [1521-1540]
- Line 481: Duplicate range [1541-1560]
- Line 491: Duplicate range [999-1005]
- Line 496: Duplicate range [1006-1012]
- Line 501: Duplicate range [1013-1026]
- Line 506: Duplicate range [1027-1041]
- Line 511: Duplicate range [1042-1054]
- Line 516: Duplicate range [1055-1061]
- Line 521: Duplicate range [1062-1076]
- Line 526: Duplicate range [1077-1096]
- Line 531: Duplicate range [1097-1118]
- Line 536: Duplicate range [1119-1140]
- Line 541: Duplicate range [1141-1164]
- Line 546: Duplicate range [1165-1188]
- Line 551: Duplicate range [1189-1210]
- Line 556: Duplicate range [1211-1236]
- Line 561: Duplicate range [1237-1260]
- Line 566: Duplicate range [1261-1296]
- Line 571: Duplicate range [1297-1322]
- Line 576: Duplicate range [1323-1350]
- Line 581: Duplicate range [1351-1400]
- Line 586: Duplicate range [1401-1423]
- Line 591: Duplicate range [1424-1448]
- Line 596: Duplicate range [1449-1468]
- Line 601: Duplicate range [1469-1478]
- Line 606: Duplicate range [1479-1500]
- Line 611: Duplicate range [1501-1520]
- Line 616: Duplicate range [1521-1540]
- Line 621: Duplicate range [1541-1560]
- Line 626: Duplicate range [999-1560]
- Line 631: Duplicate range [999-1005]
- Line 636: Duplicate range [1006-1012]
- Line 641: Duplicate range [1013-1026]
- Line 646: Duplicate range [1027-1041]
- Line 651: Duplicate range [1042-1054]
- Line 656: Duplicate range [1055-1061]
- Line 661: Duplicate range [1062-1076]
- Line 666: Duplicate range [1077-1096]
- Line 671: Duplicate range [1097-1118]
- Line 676: Duplicate range [1119-1140]
- Line 681: Duplicate range [1141-1164]
- Line 686: Duplicate range [1165-1188]
- Line 691: Duplicate range [1189-1210]
- Line 696: Duplicate range [1211-1236]
- Line 701: Duplicate range [1237-1260]
- Line 706: Duplicate range [1261-1296]
- Line 711: Duplicate range [1297-1322]
- Line 716: Duplicate range [1323-1350]
- Line 721: Duplicate range [1351-1400]
- Line 726: Duplicate range [1401-1423]
- Line 731: Duplicate range [1424-1448]
- Line 736: Duplicate range [1449-1468]
- Line 741: Duplicate range [1469-1478]
- Line 746: Duplicate range [1479-1500]
- Line 751: Duplicate range [1501-1520]
- Line 756: Duplicate range [1521-1540]
- Line 761: Duplicate range [1541-1560]
- Line 766: Duplicate range [999-1560]
- Line 771: Duplicate range [999-1005]
- Line 776: Duplicate range [1006-1012]
- Line 781: Duplicate range [1013-1026]
- Line 786: Duplicate range [1027-1041]
- Line 791: Duplicate range [1042-1054]
- Line 796: Duplicate range [1055-1061]
- Line 801: Duplicate range [1062-1076]
- Line 806: Duplicate range [1077-1096]
- Line 811: Duplicate range [1097-1118]
- Line 816: Duplicate range [1119-1140]
- Line 821: Duplicate range [1141-1164]
- Line 826: Duplicate range [1165-1188]
- Line 831: Duplicate range [1189-1210]
- Line 836: Duplicate range [1211-1236]
- Line 841: Duplicate range [1237-1260]
- Line 846: Duplicate range [1261-1296]
- Line 851: Duplicate range [1297-1322]
- Line 856: Duplicate range [1323-1350]
- Line 861: Duplicate range [1351-1400]
- Line 866: Duplicate range [1401-1423]
- Line 871: Duplicate range [1424-1448]
- Line 876: Duplicate range [1449-1468]
- Line 881: Duplicate range [1469-1478]
- Line 886: Duplicate range [1479-1500]
- Line 891: Duplicate range [1501-1520]
- Line 896: Duplicate range [1521-1540]
- Line 901: Duplicate range [1541-1560]

---

### File: dynamic/commentary_BACKUP/01-02-02-01.txt

**Errors:**
- Line 26: Non-sequential range [1424-1424] - Start (1424) < Previous start (1454)
- Line 29: Duplicate range [1424-1424]
- Line 34: Duplicate range [1424-1424]
- Line 41: Duplicate range [1424-1424]
- Line 46: Duplicate range [1424-1424]
- Line 53: Duplicate range [1424-1424]
- Line 56: Duplicate range [1424-1424]

---

### File: dynamic/commentary_BACKUP/01-02-02-02.txt

**Errors:**
- Line 6: Duplicate range [1463-1480]

---

### File: dynamic/commentary_BACKUP/01-03-02-01.txt

**Errors:**
- Line 6: Duplicate range [1671-1680]
- Line 9: Duplicate range [1671-1680]
- Line 17: Duplicate range [1681-1690]
- Line 25: Duplicate range [1691-1700]
- Line 33: Duplicate range [1701-1710]
- Line 39: Duplicate range [1711-1720]
- Line 42: Duplicate range [1711-1720]
- Line 50: Duplicate range [1721-1731]
- Line 53: Duplicate range [1721-1731]

---

### File: dynamic/commentary_BACKUP/01-04-01-01.txt

**Errors:**
- Line 278: Non-sequential range [1902-2101] - Start (1902) < Previous start (2099)
- Line 300: Non-sequential range [1902-2101] - Start (1902) < Previous start (2017)
- Line 312: Non-sequential range [1902-2101] - Start (1902) < Previous start (1936)
- Line 349: Non-sequential range [2112-2127] - Start (2112) < Previous start (2119)
- Line 427: Non-sequential range [2102-2201] - Start (2102) < Previous start (2198)
- Line 446: Non-sequential range [1902-2201] - Start (1902) < Previous start (2102)
- Line 470: Non-sequential range [1902-2201] - Start (1902) < Previous start (2201)
- Line 510: Non-sequential range [1902-2201] - Start (1902) < Previous start (2102)
- Line 568: Non-sequential range [1902-1910] - Start (1902) < Previous start (2201)
- Line 600: Non-sequential range [1902-2201] - Start (1902) < Previous start (2102)
- Line 673: Non-sequential range [1902-1910] - Start (1902) < Previous start (2201)
- Line 739: Non-sequential range [1902-2201] - Start (1902) < Previous start (2178)
- Line 778: Non-sequential range [1902-2201] - Start (1902) < Previous start (2201)
- Line 799: Non-sequential range [1902-2201] - Start (1902) < Previous start (1943)
- Line 814: Non-sequential range [1902-2201] - Start (1902) < Previous start (2201)
- Line 266: Duplicate range [2084-2098]
- Line 300: Duplicate range [1902-2101]
- Line 312: Duplicate range [1902-2101]
- Line 324: Duplicate range [2099-2101]
- Line 362: Duplicate range [2128-2137]
- Line 374: Duplicate range [2138-2147]
- Line 386: Duplicate range [2148-2157]
- Line 404: Duplicate range [2168-2177]
- Line 415: Duplicate range [2178-2197]
- Line 433: Duplicate range [2102-2201]
- Line 440: Duplicate range [2102-2201]
- Line 452: Duplicate range [1902-2201]
- Line 459: Duplicate range [1902-2201]
- Line 470: Duplicate range [1902-2201]
- Line 477: Duplicate range [1910-1935]
- Line 490: Duplicate range [1943-2016]
- Line 497: Duplicate range [2017-2101]
- Line 504: Duplicate range [2102-2201]
- Line 510: Duplicate range [1902-2201]
- Line 518: Duplicate range [1902-2201]
- Line 525: Duplicate range [1902-2201]
- Line 531: Duplicate range [1902-2201]
- Line 537: Duplicate range [1902-2201]
- Line 541: Duplicate range [1902-2201]
- Line 548: Duplicate range [1902-2201]
- Line 554: Duplicate range [1902-2201]
- Line 561: Duplicate range [2201-2201]
- Line 568: Duplicate range [1902-1910]
- Line 582: Duplicate range [1936-2050]
- Line 595: Duplicate range [2102-2201]
- Line 600: Duplicate range [1902-2201]
- Line 606: Duplicate range [1902-2201]
- Line 612: Duplicate range [1902-2201]
- Line 618: Duplicate range [1902-2201]
- Line 624: Duplicate range [1902-2201]
- Line 630: Duplicate range [1902-2201]
- Line 637: Duplicate range [1902-2201]
- Line 644: Duplicate range [1902-2201]
- Line 651: Duplicate range [1902-2201]
- Line 657: Duplicate range [1902-2201]
- Line 663: Duplicate range [1902-2201]
- Line 670: Duplicate range [2201-2201]
- Line 673: Duplicate range [1902-1910]
- Line 692: Duplicate range [1936-2050]
- Line 699: Duplicate range [2051-2101]
- Line 706: Duplicate range [2102-2118]
- Line 739: Duplicate range [1902-2201]
- Line 745: Duplicate range [1902-2201]
- Line 751: Duplicate range [1902-2201]
- Line 758: Duplicate range [1902-2201]
- Line 765: Duplicate range [1902-2201]
- Line 772: Duplicate range [2201-2201]
- Line 778: Duplicate range [1902-2201]
- Line 785: Duplicate range [1910-1935]
- Line 799: Duplicate range [1902-2201]
- Line 804: Duplicate range [1902-2201]
- Line 811: Duplicate range [2201-2201]
- Line 814: Duplicate range [1902-2201]

---

### File: dynamic/commentary_BACKUP/01-04-02-01.txt

**Errors:**
- Line 46: Non-sequential range [2539-2832] - Start (2539) < Previous start (2618)
- Line 67: Non-sequential range [2539-2832] - Start (2539) < Previous start (2832)
- Line 238: Non-sequential range [2539-2832] - Start (2539) < Previous start (2832)
- Line 274: Non-sequential range [2539-2832] - Start (2539) < Previous start (2832)
- Line 4: Duplicate range [2539-2546]
- Line 7: Duplicate range [2539-2546]
- Line 13: Duplicate range [2547-2556]
- Line 16: Duplicate range [2547-2556]
- Line 22: Duplicate range [2557-2579]
- Line 25: Duplicate range [2557-2579]
- Line 31: Duplicate range [2580-2596]
- Line 37: Duplicate range [2597-2617]
- Line 43: Duplicate range [2618-2832]
- Line 49: Duplicate range [2539-2832]
- Line 52: Duplicate range [2539-2832]
- Line 55: Duplicate range [2539-2832]
- Line 58: Duplicate range [2539-2832]
- Line 61: Duplicate range [2539-2832]
- Line 67: Duplicate range [2539-2832]
- Line 74: Duplicate range [2539-2832]
- Line 81: Duplicate range [2539-2832]
- Line 87: Duplicate range [2539-2832]
- Line 94: Duplicate range [2539-2832]
- Line 102: Duplicate range [2539-2832]
- Line 108: Duplicate range [2539-2832]
- Line 115: Duplicate range [2539-2832]
- Line 122: Duplicate range [2539-2832]
- Line 128: Duplicate range [2539-2832]
- Line 133: Duplicate range [2539-2832]
- Line 139: Duplicate range [2539-2832]
- Line 145: Duplicate range [2539-2832]
- Line 152: Duplicate range [2539-2832]
- Line 158: Duplicate range [2539-2832]
- Line 164: Duplicate range [2539-2832]
- Line 170: Duplicate range [2539-2832]
- Line 176: Duplicate range [2539-2832]
- Line 182: Duplicate range [2539-2832]
- Line 187: Duplicate range [2539-2832]
- Line 192: Duplicate range [2539-2832]
- Line 197: Duplicate range [2539-2832]
- Line 203: Duplicate range [2539-2832]
- Line 209: Duplicate range [2539-2832]
- Line 214: Duplicate range [2539-2832]
- Line 219: Duplicate range [2539-2832]
- Line 224: Duplicate range [2539-2832]
- Line 230: Duplicate range [2539-2832]
- Line 235: Duplicate range [2832-2832]
- Line 238: Duplicate range [2539-2832]
- Line 244: Duplicate range [2539-2832]
- Line 250: Duplicate range [2539-2832]
- Line 256: Duplicate range [2539-2832]
- Line 261: Duplicate range [2539-2832]
- Line 266: Duplicate range [2539-2832]
- Line 271: Duplicate range [2832-2832]
- Line 274: Duplicate range [2539-2832]
- Line 282: Duplicate range [2539-2832]
- Line 288: Duplicate range [2539-2832]
- Line 295: Duplicate range [2539-2832]
- Line 302: Duplicate range [2539-2832]
- Line 308: Duplicate range [2539-2832]
- Line 315: Duplicate range [2539-2832]
- Line 321: Duplicate range [2539-2832]
- Line 327: Duplicate range [2539-2832]
- Line 333: Duplicate range [2539-2832]
- Line 339: Duplicate range [2539-2832]
- Line 345: Duplicate range [2832-2832]

---

### File: dynamic/commentary_BACKUP/01-04-03-01.txt

**Errors:**
- Line 25: Duplicate range [2833-2835]
- Line 28: Duplicate range [2833-2835]
- Line 31: Duplicate range [2833-2835]
- Line 34: Duplicate range [2833-2835]
- Line 37: Duplicate range [2833-2835]

---

### File: dynamic/commentary_BACKUP/01-04-04-01.txt

**Errors:**
- Line 28: Non-sequential range [2843-2848] - Start (2843) < Previous start (2846)
- Line 43: Non-sequential range [2836-2848] - Start (2836) < Previous start (2843)
- Line 19: Duplicate range [2843-2845]
- Line 25: Duplicate range [2846-2848]
- Line 28: Duplicate range [2843-2848]
- Line 31: Duplicate range [2843-2848]
- Line 34: Duplicate range [2843-2848]
- Line 37: Duplicate range [2843-2848]
- Line 40: Duplicate range [2843-2848]
- Line 43: Duplicate range [2836-2848]

---

### File: dynamic/commentary_BACKUP/01-04-05-01.txt

**Errors:**
- Line 16: Non-sequential range [2849-2861] - Start (2849) < Previous start (2858)
- Line 38: Non-sequential range [2849-2872] - Start (2849) < Previous start (2870)
- Line 46: Non-sequential range [2849-2872] - Start (2849) < Previous start (2862)
- Line 23: Duplicate range [2854-2861]
- Line 43: Duplicate range [2862-2872]
- Line 46: Duplicate range [2849-2872]

---

### File: dynamic/commentary_BACKUP/01-04-06-01.txt

**Errors:**
- Line 3: Duplicate range [2873-2880]
- Line 5: Duplicate range [2873-2880]
- Line 9: Duplicate range [2881-2887]
- Line 11: Duplicate range [2881-2887]
- Line 15: Duplicate range [2888-2903]
- Line 17: Duplicate range [2888-2903]
- Line 19: Duplicate range [2888-2903]
- Line 23: Duplicate range [2904-2913]
- Line 25: Duplicate range [2904-2913]
- Line 29: Duplicate range [2914-2930]
- Line 31: Duplicate range [2914-2930]
- Line 35: Duplicate range [2931-2950]
- Line 37: Duplicate range [2931-2950]
- Line 41: Duplicate range [2951-2978]
- Line 43: Duplicate range [2951-2978]
- Line 47: Duplicate range [2979-2982]
- Line 51: Duplicate range [2983-2990]
- Line 53: Duplicate range [2983-2990]
- Line 57: Duplicate range [2991-2995]
- Line 59: Duplicate range [2991-2995]

---

### File: dynamic/commentary_BACKUP/01-04-07-01.txt

**Errors:**
- Line 28: Non-sequential range [2983-2988] - Start (2983) < Previous start (2985)
- Line 28: Duplicate range [2983-2988]
- Line 31: Duplicate range [2983-2988]
- Line 34: Duplicate range [2983-2988]
- Line 37: Duplicate range [2983-2988]
- Line 40: Duplicate range [2983-2988]
- Line 43: Duplicate range [2983-2988]

---

### File: dynamic/commentary_BACKUP/01-04-08-01.txt

**Errors:**
- Line 20: Non-sequential range [2995-2998] - Start (2995) < Previous start (3004)
- Line 47: Non-sequential range [3009-3016] - Start (3009) < Previous start (3015)
- Line 20: Duplicate range [2995-2998]
- Line 52: Duplicate range [3015-3016]

---

### File: dynamic/commentary_BACKUP/01-04-09-01.txt

**Errors:**
- Line 11: Duplicate range [3017-3027]
- Line 31: Duplicate range [3028-3034]

---

### File: dynamic/commentary_BACKUP/01-04-10-01.txt

**Errors:**
- Line 25: Non-sequential range [3037-3039] - Start (3037) < Previous start (3038)
- Line 25: Duplicate range [3037-3039]
- Line 28: Duplicate range [3037-3039]
- Line 31: Duplicate range [3037-3039]
- Line 34: Duplicate range [3037-3039]
- Line 37: Duplicate range [3037-3039]
- Line 40: Duplicate range [3037-3039]
- Line 43: Duplicate range [3037-3039]

---

### File: dynamic/commentary_BACKUP/01-04-11-01.txt

**Errors:**
- Line 15: Duplicate range [3040-3056]
- Line 46: Duplicate range [3057-3061]
- Line 53: Duplicate range [3057-3061]

---

### File: dynamic/commentary_BACKUP/01-04-12-01.txt

**Errors:**
- Line 164: Non-sequential range [3132-3158] - Start (3132) < Previous start (3288)
- Line 206: Non-sequential range [3062-3131] - Start (3062) < Previous start (3246)
- Line 220: Non-sequential range [3119-3125] - Start (3119) < Previous start (3132)
- Line 227: Non-sequential range [3077-3118] - Start (3077) < Previous start (3119)
- Line 234: Non-sequential range [3062-3310] - Start (3062) < Previous start (3077)
- Line 262: Non-sequential range [3132-3158] - Start (3132) < Previous start (3285)
- Line 269: Non-sequential range [3119-3131] - Start (3119) < Previous start (3132)
- Line 276: Non-sequential range [3062-3076] - Start (3062) < Previous start (3119)
- Line 290: Non-sequential range [3062-3310] - Start (3062) < Previous start (3102)
- Line 304: Non-sequential range [3062-3118] - Start (3062) < Previous start (3132)
- Line 318: Non-sequential range [3062-3310] - Start (3062) < Previous start (3119)
- Line 332: Non-sequential range [3062-3076] - Start (3062) < Previous start (3246)
- Line 367: Non-sequential range [3062-3310] - Start (3062) < Previous start (3246)
- Line 381: Non-sequential range [3062-3118] - Start (3062) < Previous start (3119)
- Line 395: Non-sequential range [3062-3076] - Start (3062) < Previous start (3132)
- Line 423: Non-sequential range [3062-3310] - Start (3062) < Previous start (3102)
- Line 437: Non-sequential range [3062-3310] - Start (3062) < Previous start (3132)
- Line 451: Non-sequential range [3062-3118] - Start (3062) < Previous start (3119)
- Line 10: Duplicate range [3062-3076]
- Line 52: Duplicate range [3092-3101]
- Line 108: Duplicate range [3132-3158]
- Line 164: Duplicate range [3132-3158]
- Line 178: Duplicate range [3177-3184]
- Line 192: Duplicate range [3235-3245]
- Line 199: Duplicate range [3246-3310]
- Line 220: Duplicate range [3119-3125]
- Line 241: Duplicate range [3185-3234]
- Line 255: Duplicate range [3285-3310]
- Line 262: Duplicate range [3132-3158]
- Line 269: Duplicate range [3119-3131]
- Line 276: Duplicate range [3062-3076]
- Line 283: Duplicate range [3102-3113]
- Line 290: Duplicate range [3062-3310]
- Line 297: Duplicate range [3132-3310]
- Line 311: Duplicate range [3119-3125]
- Line 318: Duplicate range [3062-3310]
- Line 325: Duplicate range [3246-3310]
- Line 332: Duplicate range [3062-3076]
- Line 346: Duplicate range [3062-3310]
- Line 353: Duplicate range [3132-3158]
- Line 360: Duplicate range [3246-3310]
- Line 367: Duplicate range [3062-3310]
- Line 374: Duplicate range [3119-3131]
- Line 381: Duplicate range [3062-3118]
- Line 388: Duplicate range [3132-3310]
- Line 395: Duplicate range [3062-3076]
- Line 409: Duplicate range [3062-3310]
- Line 416: Duplicate range [3102-3113]
- Line 423: Duplicate range [3062-3310]
- Line 430: Duplicate range [3132-3158]
- Line 437: Duplicate range [3062-3310]
- Line 444: Duplicate range [3119-3125]
- Line 451: Duplicate range [3062-3118]
- Line 458: Duplicate range [3062-3310]

---

### File: dynamic/commentary_BACKUP/01-04-13-01.txt

**Errors:**
- Line 10: Duplicate range [3313-3313]
- Line 21: Duplicate range [3313-3313]
- Line 32: Duplicate range [3313-3313]
- Line 39: Duplicate range [3313-3313]
- Line 50: Duplicate range [3313-3313]
- Line 74: Duplicate range [3313-3313]
- Line 81: Duplicate range [3313-3313]

---

### File: dynamic/commentary_BACKUP/01-04-14-01.txt

**Errors:**
- Line 8: Duplicate range [3341-3361]
- Line 16: Duplicate range [3362-3370]
- Line 24: Duplicate range [3371-3410]
- Line 36: Duplicate range [3411-3450]
- Line 46: Duplicate range [3451-3492]
- Line 58: Duplicate range [3493-3522]
- Line 70: Duplicate range [3523-3553]
- Line 82: Duplicate range [3554-3595]
- Line 92: Duplicate range [3596-3612]
- Line 102: Duplicate range [3613-3692]

---

### File: dynamic/commentary_BACKUP/01-04-16-01.txt

**Errors:**
- Line 17: Non-sequential range [3766-3791] - Start (3766) < Previous start (3772)
- Line 114: Non-sequential range [3766-3869] - Start (3766) < Previous start (3859)
- Line 116: Duplicate range [3766-3869]
- Line 118: Duplicate range [3766-3869]
- Line 120: Duplicate range [3766-3869]
- Line 122: Duplicate range [3766-3869]
- Line 124: Duplicate range [3766-3869]
- Line 126: Duplicate range [3766-3869]
- Line 128: Duplicate range [3766-3869]
- Line 130: Duplicate range [3766-3869]
- Line 132: Duplicate range [3766-3869]
- Line 134: Duplicate range [3766-3869]

---

### File: dynamic/commentary_BACKUP/01-04-18-01.txt

**Errors:**
- Line 8: Duplicate range [3888-3892]
- Line 13: Duplicate range [3888-3892]

---

### File: dynamic/commentary_BACKUP/01-04-18-02.txt

**Errors:**
- Line 118: Non-sequential range [3950-3971] - Start (3950) < Previous start (3989)
- Line 8: Duplicate range [3950-3967]
- Line 17: Duplicate range [3950-3967]
- Line 24: Duplicate range [3950-3967]
- Line 74: Duplicate range [3972-3984]
- Line 120: Duplicate range [3950-3971]
- Line 122: Duplicate range [3950-3971]
- Line 124: Duplicate range [3950-3971]
- Line 126: Duplicate range [3950-3971]
- Line 128: Duplicate range [3950-3971]
- Line 130: Duplicate range [3950-3971]
- Line 132: Duplicate range [3950-3971]
- Line 134: Duplicate range [3950-3971]
- Line 136: Duplicate range [3950-3971]
- Line 138: Duplicate range [3950-3971]
- Line 140: Duplicate range [3950-3971]
- Line 142: Duplicate range [3950-3971]
- Line 144: Duplicate range [3950-3971]
- Line 146: Duplicate range [3950-3971]
- Line 148: Duplicate range [3950-3971]
- Line 150: Duplicate range [3950-3971]
- Line 152: Duplicate range [3950-3971]
- Line 154: Duplicate range [3950-3971]
- Line 156: Duplicate range [3950-3971]
- Line 158: Duplicate range [3950-3971]
- Line 160: Duplicate range [3950-3971]
- Line 162: Duplicate range [3950-3971]
- Line 164: Duplicate range [3950-3971]
- Line 166: Duplicate range [3950-3971]
- Line 168: Duplicate range [3950-3971]

---

### File: dynamic/commentary_BACKUP/01-04-19-01.txt

**Errors:**
- Line 90: Duplicate range [4151-4170]

---

### File: dynamic/commentary_BACKUP/01-05-02-01.txt

**Errors:**
- Line 166: Non-sequential range [4283-4303] - Start (4283) < Previous start (4621)
- Line 251: Non-sequential range [4283-4303] - Start (4283) < Previous start (4621)
- Line 336: Non-sequential range [4283-4637] - Start (4283) < Previous start (4621)
- Line 431: Non-sequential range [4283-4637] - Start (4283) < Previous start (4621)
- Line 21: Duplicate range [4304-4327]
- Line 31: Duplicate range [4328-4350]
- Line 56: Duplicate range [4383-4400]
- Line 66: Duplicate range [4401-4420]
- Line 76: Duplicate range [4421-4440]
- Line 86: Duplicate range [4441-4460]
- Line 96: Duplicate range [4461-4480]
- Line 106: Duplicate range [4481-4500]
- Line 116: Duplicate range [4501-4520]
- Line 126: Duplicate range [4521-4540]
- Line 136: Duplicate range [4541-4560]
- Line 151: Duplicate range [4581-4600]
- Line 166: Duplicate range [4283-4303]
- Line 171: Duplicate range [4304-4327]
- Line 176: Duplicate range [4328-4350]
- Line 181: Duplicate range [4351-4375]
- Line 191: Duplicate range [4401-4420]
- Line 196: Duplicate range [4421-4440]
- Line 201: Duplicate range [4441-4460]
- Line 206: Duplicate range [4461-4480]
- Line 211: Duplicate range [4481-4500]
- Line 216: Duplicate range [4501-4520]
- Line 221: Duplicate range [4521-4540]
- Line 226: Duplicate range [4541-4560]
- Line 231: Duplicate range [4561-4580]
- Line 236: Duplicate range [4581-4600]
- Line 241: Duplicate range [4601-4620]
- Line 246: Duplicate range [4621-4637]
- Line 251: Duplicate range [4283-4303]
- Line 256: Duplicate range [4304-4327]
- Line 261: Duplicate range [4328-4350]
- Line 266: Duplicate range [4351-4375]
- Line 271: Duplicate range [4376-4400]
- Line 276: Duplicate range [4401-4420]
- Line 281: Duplicate range [4421-4440]
- Line 286: Duplicate range [4441-4460]
- Line 291: Duplicate range [4461-4480]
- Line 296: Duplicate range [4481-4500]
- Line 301: Duplicate range [4501-4520]
- Line 306: Duplicate range [4521-4540]
- Line 311: Duplicate range [4541-4560]
- Line 316: Duplicate range [4561-4580]
- Line 321: Duplicate range [4581-4600]
- Line 326: Duplicate range [4601-4620]
- Line 331: Duplicate range [4621-4637]
- Line 341: Duplicate range [4283-4637]
- Line 346: Duplicate range [4283-4303]
- Line 351: Duplicate range [4304-4327]
- Line 356: Duplicate range [4328-4350]
- Line 361: Duplicate range [4351-4375]
- Line 366: Duplicate range [4376-4400]
- Line 371: Duplicate range [4401-4420]
- Line 376: Duplicate range [4421-4440]
- Line 381: Duplicate range [4441-4460]
- Line 386: Duplicate range [4461-4480]
- Line 391: Duplicate range [4481-4500]
- Line 396: Duplicate range [4501-4520]
- Line 401: Duplicate range [4521-4540]
- Line 406: Duplicate range [4541-4560]
- Line 411: Duplicate range [4561-4580]
- Line 416: Duplicate range [4581-4600]
- Line 421: Duplicate range [4601-4620]
- Line 426: Duplicate range [4621-4637]
- Line 431: Duplicate range [4283-4637]
- Line 436: Duplicate range [4283-4637]
- Line 441: Duplicate range [4283-4637]

---

### File: dynamic/commentary_BACKUP/01-05-03-01.txt

**Errors:**
- Line 123: Non-sequential range [4639-4810] - Start (4639) < Previous start (4791)
- Line 3: Duplicate range [4639-4642]
- Line 5: Duplicate range [4639-4642]
- Line 7: Duplicate range [4639-4642]
- Line 9: Duplicate range [4639-4642]
- Line 13: Duplicate range [4643-4646]
- Line 15: Duplicate range [4643-4646]
- Line 17: Duplicate range [4643-4646]
- Line 21: Duplicate range [4647-4650]
- Line 23: Duplicate range [4647-4650]
- Line 25: Duplicate range [4647-4650]
- Line 29: Duplicate range [4651-4654]
- Line 31: Duplicate range [4651-4654]
- Line 33: Duplicate range [4651-4654]
- Line 37: Duplicate range [4655-4658]
- Line 39: Duplicate range [4655-4658]
- Line 41: Duplicate range [4655-4658]
- Line 45: Duplicate range [4659-4662]
- Line 47: Duplicate range [4659-4662]
- Line 49: Duplicate range [4659-4662]
- Line 53: Duplicate range [4663-4666]
- Line 55: Duplicate range [4663-4666]
- Line 57: Duplicate range [4663-4666]
- Line 61: Duplicate range [4667-4670]
- Line 63: Duplicate range [4667-4670]
- Line 65: Duplicate range [4667-4670]
- Line 69: Duplicate range [4671-4690]
- Line 71: Duplicate range [4671-4690]
- Line 73: Duplicate range [4671-4690]
- Line 77: Duplicate range [4691-4710]
- Line 79: Duplicate range [4691-4710]
- Line 81: Duplicate range [4691-4710]
- Line 85: Duplicate range [4711-4730]
- Line 87: Duplicate range [4711-4730]
- Line 89: Duplicate range [4711-4730]
- Line 93: Duplicate range [4731-4750]
- Line 95: Duplicate range [4731-4750]
- Line 97: Duplicate range [4731-4750]
- Line 101: Duplicate range [4751-4770]
- Line 103: Duplicate range [4751-4770]
- Line 105: Duplicate range [4751-4770]
- Line 109: Duplicate range [4771-4790]
- Line 111: Duplicate range [4771-4790]
- Line 113: Duplicate range [4771-4790]
- Line 117: Duplicate range [4791-4810]
- Line 119: Duplicate range [4791-4810]
- Line 121: Duplicate range [4791-4810]
- Line 125: Duplicate range [4639-4810]
- Line 127: Duplicate range [4639-4810]
- Line 129: Duplicate range [4639-4810]
- Line 131: Duplicate range [4639-4810]
- Line 133: Duplicate range [4639-4810]
- Line 135: Duplicate range [4639-4810]
- Line 137: Duplicate range [4639-4810]
- Line 139: Duplicate range [4639-4810]
- Line 141: Duplicate range [4639-4810]
- Line 143: Duplicate range [4639-4810]
- Line 145: Duplicate range [4639-4810]
- Line 147: Duplicate range [4639-4810]
- Line 149: Duplicate range [4639-4810]
- Line 151: Duplicate range [4639-4810]
- Line 153: Duplicate range [4639-4810]
- Line 155: Duplicate range [4639-4810]
- Line 157: Duplicate range [4639-4810]
- Line 159: Duplicate range [4639-4810]
- Line 161: Duplicate range [4639-4810]
- Line 163: Duplicate range [4639-4810]
- Line 165: Duplicate range [4639-4810]
- Line 167: Duplicate range [4639-4810]

---

### File: dynamic/commentary_BACKUP/01-05-04-01.txt

**Errors:**
- Line 106: Non-sequential range [4929-4978] - Start (4929) < Previous start (4946)
- Line 226: Non-sequential range [4848-6419] - Start (4848) < Previous start (6401)
- Line 321: Non-sequential range [4848-6419] - Start (4848) < Previous start (6201)
- Line 426: Non-sequential range [4848-6419] - Start (4848) < Previous start (6201)
- Line 521: Non-sequential range [5135-5200] - Start (5135) < Previous start (6101)
- Line 641: Non-sequential range [4848-4878] - Start (4848) < Previous start (6101)
- Line 731: Non-sequential range [4848-4878] - Start (4848) < Previous start (6201)
- Line 816: Non-sequential range [5135-5200] - Start (5135) < Previous start (6101)
- Line 901: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 991: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 1081: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 1171: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 1261: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 1356: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 1451: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 1546: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 1641: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 1736: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 1831: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 1926: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 2021: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 2116: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 2211: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 2306: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 2401: Non-sequential range [4848-6419] - Start (4848) < Previous start (6101)
- Line 16: Duplicate range [4856-4878]
- Line 26: Duplicate range [4879-4928]
- Line 116: Duplicate range [4979-5030]
- Line 131: Duplicate range [5083-5134]
- Line 141: Duplicate range [5135-5200]
- Line 151: Duplicate range [5201-5300]
- Line 161: Duplicate range [5301-5400]
- Line 171: Duplicate range [5401-5500]
- Line 231: Duplicate range [4848-4878]
- Line 236: Duplicate range [4879-4928]
- Line 241: Duplicate range [4929-4978]
- Line 246: Duplicate range [4979-5030]
- Line 251: Duplicate range [5031-5082]
- Line 256: Duplicate range [5083-5134]
- Line 261: Duplicate range [5135-5200]
- Line 266: Duplicate range [5201-5300]
- Line 271: Duplicate range [5301-5400]
- Line 276: Duplicate range [5401-5500]
- Line 281: Duplicate range [5501-5600]
- Line 286: Duplicate range [5601-5700]
- Line 291: Duplicate range [5701-5800]
- Line 296: Duplicate range [5801-5900]
- Line 301: Duplicate range [5901-6000]
- Line 306: Duplicate range [6001-6100]
- Line 311: Duplicate range [6101-6200]
- Line 321: Duplicate range [4848-6419]
- Line 326: Duplicate range [4848-6419]
- Line 331: Duplicate range [4848-6419]
- Line 336: Duplicate range [4848-4878]
- Line 341: Duplicate range [4879-4928]
- Line 346: Duplicate range [4929-4978]
- Line 351: Duplicate range [4979-5030]
- Line 356: Duplicate range [5031-5082]
- Line 361: Duplicate range [5083-5134]
- Line 366: Duplicate range [5135-5200]
- Line 371: Duplicate range [5201-5300]
- Line 376: Duplicate range [5301-5400]
- Line 381: Duplicate range [5401-5500]
- Line 386: Duplicate range [5501-5600]
- Line 391: Duplicate range [5601-5700]
- Line 396: Duplicate range [5701-5800]
- Line 401: Duplicate range [5801-5900]
- Line 406: Duplicate range [5901-6000]
- Line 411: Duplicate range [6001-6100]
- Line 416: Duplicate range [6101-6200]
- Line 421: Duplicate range [6201-6419]
- Line 426: Duplicate range [4848-6419]
- Line 431: Duplicate range [4848-6419]
- Line 436: Duplicate range [4848-4878]
- Line 441: Duplicate range [4879-4928]
- Line 446: Duplicate range [4929-4978]
- Line 451: Duplicate range [4979-5030]
- Line 456: Duplicate range [5031-5082]
- Line 461: Duplicate range [5083-5134]
- Line 466: Duplicate range [5135-5200]
- Line 471: Duplicate range [5201-5300]
- Line 476: Duplicate range [5301-5400]
- Line 481: Duplicate range [5401-5500]
- Line 486: Duplicate range [5501-5600]
- Line 491: Duplicate range [5601-5700]
- Line 496: Duplicate range [5701-5800]
- Line 501: Duplicate range [5801-5900]
- Line 506: Duplicate range [5901-6000]
- Line 511: Duplicate range [6001-6100]
- Line 521: Duplicate range [5135-5200]
- Line 526: Duplicate range [5135-5200]
- Line 531: Duplicate range [5135-5200]
- Line 536: Duplicate range [5135-5200]
- Line 541: Duplicate range [5201-5300]
- Line 546: Duplicate range [5201-5300]
- Line 551: Duplicate range [5201-5300]
- Line 556: Duplicate range [5201-5300]
- Line 561: Duplicate range [5201-5300]
- Line 566: Duplicate range [5201-5300]
- Line 571: Duplicate range [5301-5400]
- Line 576: Duplicate range [5301-5400]
- Line 581: Duplicate range [5301-5400]
- Line 586: Duplicate range [5301-5400]
- Line 591: Duplicate range [5401-5500]
- Line 596: Duplicate range [5401-5500]
- Line 601: Duplicate range [5401-5500]
- Line 606: Duplicate range [5601-5700]
- Line 611: Duplicate range [5601-5700]
- Line 616: Duplicate range [5701-5800]
- Line 621: Duplicate range [5801-5900]
- Line 626: Duplicate range [5901-6000]
- Line 631: Duplicate range [6001-6100]
- Line 636: Duplicate range [6101-6419]
- Line 641: Duplicate range [4848-4878]
- Line 646: Duplicate range [4879-4928]
- Line 651: Duplicate range [4929-4978]
- Line 656: Duplicate range [4979-5030]
- Line 661: Duplicate range [5031-5082]
- Line 666: Duplicate range [5083-5134]
- Line 671: Duplicate range [5135-5200]
- Line 676: Duplicate range [5201-5300]
- Line 681: Duplicate range [5301-5400]
- Line 686: Duplicate range [5401-5500]
- Line 691: Duplicate range [5501-5600]
- Line 696: Duplicate range [5601-5700]
- Line 701: Duplicate range [5701-5800]
- Line 706: Duplicate range [5801-5900]
- Line 711: Duplicate range [5901-6000]
- Line 716: Duplicate range [6001-6100]
- Line 721: Duplicate range [6101-6200]
- Line 726: Duplicate range [6201-6419]
- Line 731: Duplicate range [4848-4878]
- Line 736: Duplicate range [4879-4928]
- Line 741: Duplicate range [4929-4978]
- Line 746: Duplicate range [4979-5030]
- Line 751: Duplicate range [5031-5082]
- Line 756: Duplicate range [5083-5134]
- Line 761: Duplicate range [5135-5200]
- Line 766: Duplicate range [5201-5300]
- Line 771: Duplicate range [5301-5400]
- Line 776: Duplicate range [5401-5500]
- Line 781: Duplicate range [5501-5600]
- Line 786: Duplicate range [5601-5700]
- Line 791: Duplicate range [5701-5800]
- Line 796: Duplicate range [5801-5900]
- Line 801: Duplicate range [5901-6000]
- Line 806: Duplicate range [6001-6100]
- Line 811: Duplicate range [6101-6419]
- Line 816: Duplicate range [5135-5200]
- Line 821: Duplicate range [5135-5200]
- Line 826: Duplicate range [5201-5300]
- Line 831: Duplicate range [5201-5300]
- Line 836: Duplicate range [5301-5400]
- Line 841: Duplicate range [5301-5400]
- Line 846: Duplicate range [5301-5400]
- Line 851: Duplicate range [5301-5400]
- Line 856: Duplicate range [5401-5500]
- Line 861: Duplicate range [5401-5500]
- Line 866: Duplicate range [5401-5500]
- Line 871: Duplicate range [5601-5700]
- Line 876: Duplicate range [5701-5800]
- Line 881: Duplicate range [5801-5900]
- Line 886: Duplicate range [5901-6000]
- Line 891: Duplicate range [6001-6100]
- Line 896: Duplicate range [6101-6419]
- Line 901: Duplicate range [4848-6419]
- Line 906: Duplicate range [4848-4878]
- Line 911: Duplicate range [4879-4928]
- Line 916: Duplicate range [4929-4978]
- Line 921: Duplicate range [4979-5030]
- Line 926: Duplicate range [5031-5082]
- Line 931: Duplicate range [5083-5134]
- Line 936: Duplicate range [5135-5200]
- Line 941: Duplicate range [5201-5300]
- Line 946: Duplicate range [5301-5400]
- Line 951: Duplicate range [5401-5500]
- Line 956: Duplicate range [5501-5600]
- Line 961: Duplicate range [5601-5700]
- Line 966: Duplicate range [5701-5800]
- Line 971: Duplicate range [5801-5900]
- Line 976: Duplicate range [5901-6000]
- Line 981: Duplicate range [6001-6100]
- Line 986: Duplicate range [6101-6419]
- Line 991: Duplicate range [4848-6419]
- Line 996: Duplicate range [4848-4878]
- Line 1001: Duplicate range [4879-4928]
- Line 1006: Duplicate range [4929-4978]
- Line 1011: Duplicate range [4979-5030]
- Line 1016: Duplicate range [5031-5082]
- Line 1021: Duplicate range [5083-5134]
- Line 1026: Duplicate range [5135-5200]
- Line 1031: Duplicate range [5201-5300]
- Line 1036: Duplicate range [5301-5400]
- Line 1041: Duplicate range [5401-5500]
- Line 1046: Duplicate range [5501-5600]
- Line 1051: Duplicate range [5601-5700]
- Line 1056: Duplicate range [5701-5800]
- Line 1061: Duplicate range [5801-5900]
- Line 1066: Duplicate range [5901-6000]
- Line 1071: Duplicate range [6001-6100]
- Line 1076: Duplicate range [6101-6419]
- Line 1081: Duplicate range [4848-6419]
- Line 1086: Duplicate range [4848-4878]
- Line 1091: Duplicate range [4879-4928]
- Line 1096: Duplicate range [4929-4978]
- Line 1101: Duplicate range [4979-5030]
- Line 1106: Duplicate range [5031-5082]
- Line 1111: Duplicate range [5083-5134]
- Line 1116: Duplicate range [5135-5200]
- Line 1121: Duplicate range [5201-5300]
- Line 1126: Duplicate range [5301-5400]
- Line 1131: Duplicate range [5401-5500]
- Line 1136: Duplicate range [5501-5600]
- Line 1141: Duplicate range [5601-5700]
- Line 1146: Duplicate range [5701-5800]
- Line 1151: Duplicate range [5801-5900]
- Line 1156: Duplicate range [5901-6000]
- Line 1161: Duplicate range [6001-6100]
- Line 1166: Duplicate range [6101-6419]
- Line 1171: Duplicate range [4848-6419]
- Line 1176: Duplicate range [4848-4878]
- Line 1181: Duplicate range [4879-4928]
- Line 1186: Duplicate range [4929-4978]
- Line 1191: Duplicate range [4979-5030]
- Line 1196: Duplicate range [5031-5082]
- Line 1201: Duplicate range [5083-5134]
- Line 1206: Duplicate range [5135-5200]
- Line 1211: Duplicate range [5201-5300]
- Line 1216: Duplicate range [5301-5400]
- Line 1221: Duplicate range [5401-5500]
- Line 1226: Duplicate range [5501-5600]
- Line 1231: Duplicate range [5601-5700]
- Line 1236: Duplicate range [5701-5800]
- Line 1241: Duplicate range [5801-5900]
- Line 1246: Duplicate range [5901-6000]
- Line 1251: Duplicate range [6001-6100]
- Line 1256: Duplicate range [6101-6419]
- Line 1261: Duplicate range [4848-6419]
- Line 1266: Duplicate range [4848-6419]
- Line 1271: Duplicate range [4848-4878]
- Line 1276: Duplicate range [4879-4928]
- Line 1281: Duplicate range [4929-4978]
- Line 1286: Duplicate range [4979-5030]
- Line 1291: Duplicate range [5031-5082]
- Line 1296: Duplicate range [5083-5134]
- Line 1301: Duplicate range [5135-5200]
- Line 1306: Duplicate range [5201-5300]
- Line 1311: Duplicate range [5301-5400]
- Line 1316: Duplicate range [5401-5500]
- Line 1321: Duplicate range [5501-5600]
- Line 1326: Duplicate range [5601-5700]
- Line 1331: Duplicate range [5701-5800]
- Line 1336: Duplicate range [5801-5900]
- Line 1341: Duplicate range [5901-6000]
- Line 1346: Duplicate range [6001-6100]
- Line 1351: Duplicate range [6101-6419]
- Line 1356: Duplicate range [4848-6419]
- Line 1361: Duplicate range [4848-6419]
- Line 1366: Duplicate range [4848-4878]
- Line 1371: Duplicate range [4879-4928]
- Line 1376: Duplicate range [4929-4978]
- Line 1381: Duplicate range [4979-5030]
- Line 1386: Duplicate range [5031-5082]
- Line 1391: Duplicate range [5083-5134]
- Line 1396: Duplicate range [5135-5200]
- Line 1401: Duplicate range [5201-5300]
- Line 1406: Duplicate range [5301-5400]
- Line 1411: Duplicate range [5401-5500]
- Line 1416: Duplicate range [5501-5600]
- Line 1421: Duplicate range [5601-5700]
- Line 1426: Duplicate range [5701-5800]
- Line 1431: Duplicate range [5801-5900]
- Line 1436: Duplicate range [5901-6000]
- Line 1441: Duplicate range [6001-6100]
- Line 1446: Duplicate range [6101-6419]
- Line 1451: Duplicate range [4848-6419]
- Line 1456: Duplicate range [4848-6419]
- Line 1461: Duplicate range [4848-4878]
- Line 1466: Duplicate range [4879-4928]
- Line 1471: Duplicate range [4929-4978]
- Line 1476: Duplicate range [4979-5030]
- Line 1481: Duplicate range [5031-5082]
- Line 1486: Duplicate range [5083-5134]
- Line 1491: Duplicate range [5135-5200]
- Line 1496: Duplicate range [5201-5300]
- Line 1501: Duplicate range [5301-5400]
- Line 1506: Duplicate range [5401-5500]
- Line 1511: Duplicate range [5501-5600]
- Line 1516: Duplicate range [5601-5700]
- Line 1521: Duplicate range [5701-5800]
- Line 1526: Duplicate range [5801-5900]
- Line 1531: Duplicate range [5901-6000]
- Line 1536: Duplicate range [6001-6100]
- Line 1541: Duplicate range [6101-6419]
- Line 1546: Duplicate range [4848-6419]
- Line 1551: Duplicate range [4848-6419]
- Line 1556: Duplicate range [4848-4878]
- Line 1561: Duplicate range [4879-4928]
- Line 1566: Duplicate range [4929-4978]
- Line 1571: Duplicate range [4979-5030]
- Line 1576: Duplicate range [5031-5082]
- Line 1581: Duplicate range [5083-5134]
- Line 1586: Duplicate range [5135-5200]
- Line 1591: Duplicate range [5201-5300]
- Line 1596: Duplicate range [5301-5400]
- Line 1601: Duplicate range [5401-5500]
- Line 1606: Duplicate range [5501-5600]
- Line 1611: Duplicate range [5601-5700]
- Line 1616: Duplicate range [5701-5800]
- Line 1621: Duplicate range [5801-5900]
- Line 1626: Duplicate range [5901-6000]
- Line 1631: Duplicate range [6001-6100]
- Line 1636: Duplicate range [6101-6419]
- Line 1641: Duplicate range [4848-6419]
- Line 1646: Duplicate range [4848-6419]
- Line 1651: Duplicate range [4848-4878]
- Line 1656: Duplicate range [4879-4928]
- Line 1661: Duplicate range [4929-4978]
- Line 1666: Duplicate range [4979-5030]
- Line 1671: Duplicate range [5031-5082]
- Line 1676: Duplicate range [5083-5134]
- Line 1681: Duplicate range [5135-5200]
- Line 1686: Duplicate range [5201-5300]
- Line 1691: Duplicate range [5301-5400]
- Line 1696: Duplicate range [5401-5500]
- Line 1701: Duplicate range [5501-5600]
- Line 1706: Duplicate range [5601-5700]
- Line 1711: Duplicate range [5701-5800]
- Line 1716: Duplicate range [5801-5900]
- Line 1721: Duplicate range [5901-6000]
- Line 1726: Duplicate range [6001-6100]
- Line 1731: Duplicate range [6101-6419]
- Line 1736: Duplicate range [4848-6419]
- Line 1741: Duplicate range [4848-6419]
- Line 1746: Duplicate range [4848-4878]
- Line 1751: Duplicate range [4879-4928]
- Line 1756: Duplicate range [4929-4978]
- Line 1761: Duplicate range [4979-5030]
- Line 1766: Duplicate range [5031-5082]
- Line 1771: Duplicate range [5083-5134]
- Line 1776: Duplicate range [5135-5200]
- Line 1781: Duplicate range [5201-5300]
- Line 1786: Duplicate range [5301-5400]
- Line 1791: Duplicate range [5401-5500]
- Line 1796: Duplicate range [5501-5600]
- Line 1801: Duplicate range [5601-5700]
- Line 1806: Duplicate range [5701-5800]
- Line 1811: Duplicate range [5801-5900]
- Line 1816: Duplicate range [5901-6000]
- Line 1821: Duplicate range [6001-6100]
- Line 1826: Duplicate range [6101-6419]
- Line 1831: Duplicate range [4848-6419]
- Line 1836: Duplicate range [4848-6419]
- Line 1841: Duplicate range [4848-4878]
- Line 1846: Duplicate range [4879-4928]
- Line 1851: Duplicate range [4929-4978]
- Line 1856: Duplicate range [4979-5030]
- Line 1861: Duplicate range [5031-5082]
- Line 1866: Duplicate range [5083-5134]
- Line 1871: Duplicate range [5135-5200]
- Line 1876: Duplicate range [5201-5300]
- Line 1881: Duplicate range [5301-5400]
- Line 1886: Duplicate range [5401-5500]
- Line 1891: Duplicate range [5501-5600]
- Line 1896: Duplicate range [5601-5700]
- Line 1901: Duplicate range [5701-5800]
- Line 1906: Duplicate range [5801-5900]
- Line 1911: Duplicate range [5901-6000]
- Line 1916: Duplicate range [6001-6100]
- Line 1921: Duplicate range [6101-6419]
- Line 1926: Duplicate range [4848-6419]
- Line 1931: Duplicate range [4848-6419]
- Line 1936: Duplicate range [4848-4878]
- Line 1941: Duplicate range [4879-4928]
- Line 1946: Duplicate range [4929-4978]
- Line 1951: Duplicate range [4979-5030]
- Line 1956: Duplicate range [5031-5082]
- Line 1961: Duplicate range [5083-5134]
- Line 1966: Duplicate range [5135-5200]
- Line 1971: Duplicate range [5201-5300]
- Line 1976: Duplicate range [5301-5400]
- Line 1981: Duplicate range [5401-5500]
- Line 1986: Duplicate range [5501-5600]
- Line 1991: Duplicate range [5601-5700]
- Line 1996: Duplicate range [5701-5800]
- Line 2001: Duplicate range [5801-5900]
- Line 2006: Duplicate range [5901-6000]
- Line 2011: Duplicate range [6001-6100]
- Line 2016: Duplicate range [6101-6419]
- Line 2021: Duplicate range [4848-6419]
- Line 2026: Duplicate range [4848-6419]
- Line 2031: Duplicate range [4848-4878]
- Line 2036: Duplicate range [4879-4928]
- Line 2041: Duplicate range [4929-4978]
- Line 2046: Duplicate range [4979-5030]
- Line 2051: Duplicate range [5031-5082]
- Line 2056: Duplicate range [5083-5134]
- Line 2061: Duplicate range [5135-5200]
- Line 2066: Duplicate range [5201-5300]
- Line 2071: Duplicate range [5301-5400]
- Line 2076: Duplicate range [5401-5500]
- Line 2081: Duplicate range [5501-5600]
- Line 2086: Duplicate range [5601-5700]
- Line 2091: Duplicate range [5701-5800]
- Line 2096: Duplicate range [5801-5900]
- Line 2101: Duplicate range [5901-6000]
- Line 2106: Duplicate range [6001-6100]
- Line 2111: Duplicate range [6101-6419]
- Line 2116: Duplicate range [4848-6419]
- Line 2121: Duplicate range [4848-6419]
- Line 2126: Duplicate range [4848-4878]
- Line 2131: Duplicate range [4879-4928]
- Line 2136: Duplicate range [4929-4978]
- Line 2141: Duplicate range [4979-5030]
- Line 2146: Duplicate range [5031-5082]
- Line 2151: Duplicate range [5083-5134]
- Line 2156: Duplicate range [5135-5200]
- Line 2161: Duplicate range [5201-5300]
- Line 2166: Duplicate range [5301-5400]
- Line 2171: Duplicate range [5401-5500]
- Line 2176: Duplicate range [5501-5600]
- Line 2181: Duplicate range [5601-5700]
- Line 2186: Duplicate range [5701-5800]
- Line 2191: Duplicate range [5801-5900]
- Line 2196: Duplicate range [5901-6000]
- Line 2201: Duplicate range [6001-6100]
- Line 2206: Duplicate range [6101-6419]
- Line 2211: Duplicate range [4848-6419]
- Line 2216: Duplicate range [4848-6419]
- Line 2221: Duplicate range [4848-4878]
- Line 2226: Duplicate range [4879-4928]
- Line 2231: Duplicate range [4929-4978]
- Line 2236: Duplicate range [4979-5030]
- Line 2241: Duplicate range [5031-5082]
- Line 2246: Duplicate range [5083-5134]
- Line 2251: Duplicate range [5135-5200]
- Line 2256: Duplicate range [5201-5300]
- Line 2261: Duplicate range [5301-5400]
- Line 2266: Duplicate range [5401-5500]
- Line 2271: Duplicate range [5501-5600]
- Line 2276: Duplicate range [5601-5700]
- Line 2281: Duplicate range [5701-5800]
- Line 2286: Duplicate range [5801-5900]
- Line 2291: Duplicate range [5901-6000]
- Line 2296: Duplicate range [6001-6100]
- Line 2301: Duplicate range [6101-6419]
- Line 2306: Duplicate range [4848-6419]
- Line 2311: Duplicate range [4848-6419]
- Line 2316: Duplicate range [4848-4878]
- Line 2321: Duplicate range [4879-4928]
- Line 2326: Duplicate range [4929-4978]
- Line 2331: Duplicate range [4979-5030]
- Line 2336: Duplicate range [5031-5082]
- Line 2341: Duplicate range [5083-5134]
- Line 2346: Duplicate range [5135-5200]
- Line 2351: Duplicate range [5201-5300]
- Line 2356: Duplicate range [5301-5400]
- Line 2361: Duplicate range [5401-5500]
- Line 2366: Duplicate range [5501-5600]
- Line 2371: Duplicate range [5601-5700]
- Line 2376: Duplicate range [5701-5800]
- Line 2381: Duplicate range [5801-5900]
- Line 2386: Duplicate range [5901-6000]
- Line 2391: Duplicate range [6001-6100]
- Line 2396: Duplicate range [6101-6419]
- Line 2401: Duplicate range [4848-6419]

---

### File: dynamic/commentary_BACKUP/01-05-04-02.txt

**Errors:**
- Line 3: Duplicate range [6420-6420]
- Line 5: Duplicate range [6420-6420]
- Line 7: Duplicate range [6420-6420]
- Line 9: Duplicate range [6420-6420]
- Line 11: Duplicate range [6420-6420]
- Line 13: Duplicate range [6420-6420]
- Line 15: Duplicate range [6420-6420]
- Line 17: Duplicate range [6420-6420]
- Line 19: Duplicate range [6420-6420]
- Line 21: Duplicate range [6420-6420]

---

### File: dynamic/commentary_BACKUP/01-05-04-03.txt

**Errors:**
- Line 6: Duplicate range [6421-6421]
- Line 11: Duplicate range [6421-6421]
- Line 16: Duplicate range [6421-6421]
- Line 20: Duplicate range [6421-6421]

---

### File: dynamic/commentary_BACKUP/01-05-04-04.txt

**Errors:**
- Line 6: Duplicate range [6422-6422]
- Line 12: Duplicate range [6422-6422]
- Line 17: Duplicate range [6422-6422]
- Line 21: Duplicate range [6422-6422]

---

### File: dynamic/commentary_BACKUP/01-05-04-05.txt

**Errors:**
- Line 6: Duplicate range [6423-6423]
- Line 11: Duplicate range [6423-6423]
- Line 16: Duplicate range [6423-6423]
- Line 20: Duplicate range [6423-6423]

---

### File: dynamic/commentary_BACKUP/01-05-04-06.txt

**Errors:**
- Line 169: Non-sequential range [6626-6710] - Start (6626) < Previous start (7501)

---

### File: dynamic/commentary_BACKUP/01-05-05-01.txt

**Errors:**
- Line 7: Non-sequential range [6759-6759] - Start (6759) < Previous start (6786)
- Line 10: Duplicate range [6759-6759]
- Line 17: Duplicate range [6759-6759]
- Line 24: Duplicate range [6759-6759]
- Line 31: Duplicate range [6759-6759]
- Line 36: Duplicate range [6759-6759]
- Line 41: Duplicate range [6759-6759]
- Line 46: Duplicate range [6759-6759]
- Line 53: Duplicate range [6759-6759]
- Line 56: Duplicate range [6759-6759]
- Line 61: Duplicate range [6759-6759]
- Line 62: Duplicate range [6759-6759]

---

### File: dynamic/commentary_BACKUP/01-06-01-01.txt

**Errors:**
- Line 46: Non-sequential range [6801-7000] - Start (6801) < Previous start (6899)
- Line 61: Non-sequential range [6801-7000] - Start (6801) < Previous start (7000)
- Line 161: Non-sequential range [6801-7000] - Start (6801) < Previous start (7000)
- Line 236: Non-sequential range [6801-7000] - Start (6801) < Previous start (7000)
- Line 299: Non-sequential range [6801-7000] - Start (6801) < Previous start (7000)
- Line 356: Non-sequential range [6801-7000] - Start (6801) < Previous start (7000)
- Line 363: Non-sequential range [6801-7000] - Start (6801) < Previous start (7000)
- Line 4: Duplicate range [6801-6804]
- Line 10: Duplicate range [6805-6814]
- Line 16: Duplicate range [6815-6830]
- Line 22: Duplicate range [6831-6852]
- Line 28: Duplicate range [6845-6871]
- Line 34: Duplicate range [6872-6898]
- Line 40: Duplicate range [6886-6898]
- Line 49: Duplicate range [6801-7000]
- Line 52: Duplicate range [6801-7000]
- Line 55: Duplicate range [6801-7000]
- Line 61: Duplicate range [6801-7000]
- Line 68: Duplicate range [6801-7000]
- Line 74: Duplicate range [6801-7000]
- Line 80: Duplicate range [6801-7000]
- Line 86: Duplicate range [6801-7000]
- Line 92: Duplicate range [6801-7000]
- Line 97: Duplicate range [6801-7000]
- Line 103: Duplicate range [6801-7000]
- Line 109: Duplicate range [6801-7000]
- Line 115: Duplicate range [6801-7000]
- Line 120: Duplicate range [6801-7000]
- Line 126: Duplicate range [6801-7000]
- Line 132: Duplicate range [6801-7000]
- Line 137: Duplicate range [6801-7000]
- Line 143: Duplicate range [6801-7000]
- Line 148: Duplicate range [6801-7000]
- Line 153: Duplicate range [6801-7000]
- Line 158: Duplicate range [7000-7000]
- Line 161: Duplicate range [6801-7000]
- Line 167: Duplicate range [6801-7000]
- Line 172: Duplicate range [6801-7000]
- Line 178: Duplicate range [6801-7000]
- Line 183: Duplicate range [6801-7000]
- Line 189: Duplicate range [6801-7000]
- Line 195: Duplicate range [6801-7000]
- Line 201: Duplicate range [6801-7000]
- Line 206: Duplicate range [6801-7000]
- Line 212: Duplicate range [6801-7000]
- Line 218: Duplicate range [6801-7000]
- Line 223: Duplicate range [6801-7000]
- Line 228: Duplicate range [6801-7000]
- Line 233: Duplicate range [7000-7000]
- Line 236: Duplicate range [6801-7000]
- Line 242: Duplicate range [6801-7000]
- Line 248: Duplicate range [6801-7000]
- Line 254: Duplicate range [6801-7000]
- Line 262: Duplicate range [6801-7000]
- Line 268: Duplicate range [6801-7000]
- Line 274: Duplicate range [6801-7000]
- Line 281: Duplicate range [6801-7000]
- Line 286: Duplicate range [6801-7000]
- Line 291: Duplicate range [6801-7000]
- Line 296: Duplicate range [7000-7000]
- Line 299: Duplicate range [6801-7000]
- Line 305: Duplicate range [6801-7000]
- Line 311: Duplicate range [6801-7000]
- Line 317: Duplicate range [6801-7000]
- Line 323: Duplicate range [6801-7000]
- Line 329: Duplicate range [6801-7000]
- Line 335: Duplicate range [6801-7000]
- Line 340: Duplicate range [6801-7000]
- Line 343: Duplicate range [6801-7000]
- Line 348: Duplicate range [6801-7000]
- Line 353: Duplicate range [7000-7000]
- Line 356: Duplicate range [6801-7000]
- Line 360: Duplicate range [7000-7000]
- Line 363: Duplicate range [6801-7000]
- Line 368: Duplicate range [6801-7000]
- Line 371: Duplicate range [6801-7000]
- Line 374: Duplicate range [7000-7000]

---

### File: dynamic/commentary_BACKUP/01-06-02-01.txt

**Errors:**
- Line 149: Non-sequential range [7401-7420] - Start (7401) < Previous start (10401)

---

### File: dynamic/commentary_BACKUP/01-06-03-01.txt

**Errors:**
- Line 5: Duplicate range [8112-8112]
- Line 6: Duplicate range [8112-8112]

---

### File: dynamic/commentary_BACKUP/01-06-04-01.txt

**Errors:**
- Line 194: Non-sequential range [8281-8400] - Start (8281) < Previous start (8501)

---

### File: dynamic/commentary_BACKUP/01-06-05-01.txt

**Errors:**
- Line 7: Duplicate range [8672-8673]
- Line 13: Duplicate range [8672-8673]
- Line 19: Duplicate range [8672-8673]
- Line 22: Duplicate range [8672-8673]

---

### File: dynamic/commentary_BACKUP/01-06-05-02.txt

**Errors:**
- Line 6: Duplicate range [8674-8674]
- Line 11: Duplicate range [8674-8674]
- Line 15: Duplicate range [8674-8674]
- Line 20: Duplicate range [8674-8674]

---

### File: dynamic/commentary_BACKUP/01-06-05-03.txt

**Errors:**
- Line 7: Duplicate range [8675-8675]
- Line 12: Duplicate range [8675-8675]
- Line 17: Duplicate range [8675-8675]
- Line 22: Duplicate range [8675-8675]

---

### File: dynamic/commentary_BACKUP/01-06-05-04.txt

**Errors:**
- Line 7: Duplicate range [8676-8676]
- Line 13: Duplicate range [8676-8676]
- Line 18: Duplicate range [8676-8676]
- Line 23: Duplicate range [8676-8676]
- Line 28: Duplicate range [8676-8676]
- Line 33: Duplicate range [8676-8676]
- Line 37: Duplicate range [8676-8676]

---

### File: dynamic/commentary_BACKUP/01-06-05-05.txt

**Errors:**
- Line 7: Duplicate range [8677-8679]
- Line 12: Duplicate range [8677-8679]
- Line 16: Duplicate range [8677-8679]
- Line 20: Duplicate range [8677-8679]
- Line 25: Duplicate range [8677-8679]

---

### File: dynamic/commentary_BACKUP/01-06-06-01.txt

**Errors:**
- Line 7: Duplicate range [8680-8686]
- Line 13: Duplicate range [8680-8686]
- Line 19: Duplicate range [8680-8686]
- Line 23: Duplicate range [8680-8686]
- Line 29: Duplicate range [8680-8686]
- Line 35: Duplicate range [8680-8686]

---

### File: dynamic/commentary_BACKUP/01-06-07-01.txt

**Errors:**
- Line 9: Non-sequential range [8683-8692] - Start (8683) < Previous start (8687)
- Line 6: Duplicate range [8687-8692]
- Line 17: Duplicate range [8693-8696]
- Line 25: Duplicate range [8697-8702]
- Line 33: Duplicate range [8703-8715]
- Line 36: Duplicate range [8703-8715]
- Line 47: Duplicate range [8716-8720]
- Line 55: Duplicate range [8721-8723]

---

### File: dynamic/commentary_BACKUP/01-06-07-02.txt

**Errors:**
- Line 6: Duplicate range [8724-8724]
- Line 11: Duplicate range [8724-8724]
- Line 16: Duplicate range [8724-8724]
- Line 20: Duplicate range [8724-8724]

---

### File: dynamic/commentary_BACKUP/01-06-07-03.txt

**Errors:**
- Line 6: Duplicate range [8725-8733]
- Line 9: Duplicate range [8725-8733]
- Line 17: Duplicate range [8734-8739]
- Line 20: Duplicate range [8734-8739]
- Line 28: Duplicate range [8740-8750]
- Line 31: Duplicate range [8740-8750]
- Line 34: Duplicate range [8740-8750]
- Line 42: Duplicate range [8751-8753]
- Line 50: Duplicate range [8754-8767]
- Line 53: Duplicate range [8754-8767]
- Line 61: Duplicate range [8768-8769]

---

### File: dynamic/commentary_BACKUP/01-06-08-01.txt

**Errors:**
- Line 6: Duplicate range [8770-8770]
- Line 9: Duplicate range [8770-8770]
- Line 12: Duplicate range [8770-8770]
- Line 15: Duplicate range [8770-8770]
- Line 18: Duplicate range [8770-8770]

---

### File: dynamic/commentary_BACKUP/01-06-10-01.txt

**Errors:**
- Line 25: Non-sequential range [8841-8841] - Start (8841) < Previous start (8863)
- Line 30: Duplicate range [8841-8841]
- Line 37: Duplicate range [8841-8841]
- Line 44: Duplicate range [8841-8841]
- Line 51: Duplicate range [8841-8841]
- Line 54: Duplicate range [8841-8841]
- Line 57: Duplicate range [8841-8841]
- Line 60: Duplicate range [8841-8841]
- Line 67: Duplicate range [8841-8841]
- Line 74: Duplicate range [8841-8841]

---

### File: dynamic/commentary_BACKUP/01-06-11-01.txt

**Errors:**
- Line 27: Non-sequential range [8965-8972] - Start (8965) < Previous start (8973)
- Line 60: Non-sequential range [8873-8873] - Start (8873) < Previous start (9005)
- Line 65: Duplicate range [8873-8873]

---

### File: dynamic/commentary_BACKUP/01-06-12-01.txt

**Errors:**
- Line 126: Non-sequential range [9015-9026] - Start (9015) < Previous start (9411)
- Line 296: Non-sequential range [9015-9455] - Start (9015) < Previous start (9446)
- Line 366: Non-sequential range [9015-9516] - Start (9015) < Previous start (9485)
- Line 381: Non-sequential range [9015-9516] - Start (9015) < Previous start (9275)
- Line 471: Non-sequential range [9015-9516] - Start (9015) < Previous start (9485)
- Line 516: Non-sequential range [9015-9516] - Start (9015) < Previous start (9449)
- Line 126: Duplicate range [9015-9026]
- Line 136: Duplicate range [9020-9030]
- Line 146: Duplicate range [9034-9047]
- Line 156: Duplicate range [9070-9080]
- Line 161: Duplicate range [9070-9080]
- Line 166: Duplicate range [9081-9103]
- Line 171: Duplicate range [9081-9103]
- Line 176: Duplicate range [9104-9117]
- Line 181: Duplicate range [9118-9128]
- Line 186: Duplicate range [9129-9140]
- Line 191: Duplicate range [9141-9149]
- Line 196: Duplicate range [9141-9149]
- Line 201: Duplicate range [9150-9169]
- Line 206: Duplicate range [9150-9169]
- Line 216: Duplicate range [9344-9358]
- Line 221: Duplicate range [9344-9358]
- Line 226: Duplicate range [9349-9358]
- Line 231: Duplicate range [9349-9358]
- Line 236: Duplicate range [9359-9368]
- Line 241: Duplicate range [9359-9368]
- Line 246: Duplicate range [9369-9375]
- Line 251: Duplicate range [9369-9375]
- Line 306: Duplicate range [9275-9294]
- Line 316: Duplicate range [9295-9314]
- Line 361: Duplicate range [9485-9516]
- Line 371: Duplicate range [9015-9516]
- Line 381: Duplicate range [9015-9516]
- Line 386: Duplicate range [9015-9516]
- Line 391: Duplicate range [9015-9516]
- Line 446: Duplicate range [9339-9368]
- Line 451: Duplicate range [9369-9404]
- Line 466: Duplicate range [9485-9516]
- Line 471: Duplicate range [9015-9516]
- Line 476: Duplicate range [9015-9516]
- Line 481: Duplicate range [9015-9516]
- Line 491: Duplicate range [9275-9294]
- Line 496: Duplicate range [9295-9338]
- Line 506: Duplicate range [9405-9448]
- Line 516: Duplicate range [9015-9516]
- Line 521: Duplicate range [9015-9516]
- Line 526: Duplicate range [9015-9516]
- Line 531: Duplicate range [9015-9516]
- Line 536: Duplicate range [9015-9516]
- Line 541: Duplicate range [9015-9516]
- Line 546: Duplicate range [9015-9516]
- Line 551: Duplicate range [9015-9516]
- Line 556: Duplicate range [9015-9516]
- Line 561: Duplicate range [9015-9516]
- Line 566: Duplicate range [9015-9516]
- Line 571: Duplicate range [9015-9516]
- Line 576: Duplicate range [9015-9516]
- Line 581: Duplicate range [9015-9516]
- Line 586: Duplicate range [9015-9516]
- Line 591: Duplicate range [9015-9516]
- Line 596: Duplicate range [9015-9516]
- Line 601: Duplicate range [9015-9516]
- Line 606: Duplicate range [9015-9516]
- Line 611: Duplicate range [9015-9516]
- Line 614: Duplicate range [9015-9516]

---

### File: dynamic/commentary_BACKUP/01-06-14-01.txt

**Errors:**
- Line 7: Duplicate range [9703-9703]
- Line 13: Duplicate range [9703-9703]
- Line 19: Duplicate range [9703-9703]
- Line 24: Duplicate range [9703-9703]

---

### File: dynamic/commentary_BACKUP/01-07-01-01.txt

**Errors:**
- Line 3: Duplicate range [9704-9707]
- Line 5: Duplicate range [9704-9707]
- Line 7: Duplicate range [9704-9707]
- Line 9: Duplicate range [9704-9707]
- Line 11: Duplicate range [9704-9707]
- Line 13: Duplicate range [9704-9707]
- Line 15: Duplicate range [9704-9707]
- Line 19: Duplicate range [9708-9713]
- Line 21: Duplicate range [9708-9713]
- Line 23: Duplicate range [9708-9713]
- Line 25: Duplicate range [9708-9713]
- Line 27: Duplicate range [9708-9713]
- Line 29: Duplicate range [9708-9713]
- Line 31: Duplicate range [9708-9713]
- Line 35: Duplicate range [9714-9723]
- Line 37: Duplicate range [9714-9723]
- Line 39: Duplicate range [9714-9723]
- Line 41: Duplicate range [9714-9723]
- Line 43: Duplicate range [9714-9723]
- Line 45: Duplicate range [9714-9723]
- Line 47: Duplicate range [9714-9723]
- Line 51: Duplicate range [9724-9744]
- Line 53: Duplicate range [9724-9744]
- Line 55: Duplicate range [9724-9744]
- Line 57: Duplicate range [9724-9744]
- Line 59: Duplicate range [9724-9744]
- Line 61: Duplicate range [9724-9744]
- Line 63: Duplicate range [9724-9744]
- Line 67: Duplicate range [9745-9756]
- Line 69: Duplicate range [9745-9756]
- Line 71: Duplicate range [9745-9756]
- Line 73: Duplicate range [9745-9756]
- Line 75: Duplicate range [9745-9756]
- Line 77: Duplicate range [9745-9756]
- Line 79: Duplicate range [9745-9756]
- Line 83: Duplicate range [9757-9785]
- Line 85: Duplicate range [9757-9785]
- Line 87: Duplicate range [9757-9785]
- Line 89: Duplicate range [9757-9785]
- Line 91: Duplicate range [9757-9785]
- Line 93: Duplicate range [9757-9785]
- Line 95: Duplicate range [9757-9785]
- Line 99: Duplicate range [9786-9796]
- Line 101: Duplicate range [9786-9796]
- Line 103: Duplicate range [9786-9796]
- Line 105: Duplicate range [9786-9796]
- Line 107: Duplicate range [9786-9796]
- Line 109: Duplicate range [9786-9796]
- Line 111: Duplicate range [9786-9796]

---

### File: dynamic/commentary_BACKUP/01-07-02-01.txt

**Errors:**
- Line 3: Duplicate range [9899-9921]
- Line 5: Duplicate range [9899-9921]
- Line 7: Duplicate range [9899-9921]
- Line 9: Duplicate range [9899-9921]
- Line 11: Duplicate range [9899-9921]
- Line 13: Duplicate range [9899-9921]
- Line 15: Duplicate range [9899-9921]
- Line 19: Duplicate range [9922-9935]
- Line 21: Duplicate range [9922-9935]
- Line 23: Duplicate range [9922-9935]
- Line 25: Duplicate range [9922-9935]
- Line 27: Duplicate range [9922-9935]
- Line 29: Duplicate range [9922-9935]
- Line 31: Duplicate range [9922-9935]
- Line 35: Duplicate range [9936-9955]
- Line 37: Duplicate range [9936-9955]
- Line 39: Duplicate range [9936-9955]
- Line 41: Duplicate range [9936-9955]
- Line 43: Duplicate range [9936-9955]
- Line 45: Duplicate range [9936-9955]
- Line 47: Duplicate range [9936-9955]
- Line 51: Duplicate range [9956-9987]
- Line 53: Duplicate range [9956-9987]
- Line 55: Duplicate range [9956-9987]
- Line 57: Duplicate range [9956-9987]
- Line 59: Duplicate range [9956-9987]
- Line 61: Duplicate range [9956-9987]
- Line 63: Duplicate range [9956-9987]
- Line 67: Duplicate range [9988-9989]
- Line 69: Duplicate range [9988-9989]
- Line 71: Duplicate range [9988-9989]
- Line 73: Duplicate range [9988-9989]
- Line 75: Duplicate range [9988-9989]
- Line 77: Duplicate range [9988-9989]
- Line 79: Duplicate range [9988-9989]

---

### File: dynamic/commentary_BACKUP/01-07-03-01.txt

**Errors:**
- Line 3: Duplicate range [9990-10004]
- Line 5: Duplicate range [9990-10004]
- Line 7: Duplicate range [9990-10004]
- Line 9: Duplicate range [9990-10004]
- Line 11: Duplicate range [9990-10004]
- Line 13: Duplicate range [9990-10004]
- Line 15: Duplicate range [9990-10004]
- Line 19: Duplicate range [10005-10035]
- Line 21: Duplicate range [10005-10035]
- Line 23: Duplicate range [10005-10035]
- Line 25: Duplicate range [10005-10035]
- Line 27: Duplicate range [10005-10035]
- Line 29: Duplicate range [10005-10035]
- Line 31: Duplicate range [10005-10035]
- Line 35: Duplicate range [10036-10083]
- Line 37: Duplicate range [10036-10083]
- Line 39: Duplicate range [10036-10083]
- Line 41: Duplicate range [10036-10083]
- Line 43: Duplicate range [10036-10083]
- Line 45: Duplicate range [10036-10083]
- Line 47: Duplicate range [10036-10083]
- Line 51: Duplicate range [10041-10083]
- Line 53: Duplicate range [10041-10083]
- Line 55: Duplicate range [10041-10083]
- Line 57: Duplicate range [10041-10083]
- Line 59: Duplicate range [10041-10083]
- Line 61: Duplicate range [10041-10083]
- Line 63: Duplicate range [10041-10083]
- Line 67: Duplicate range [10084-10085]
- Line 69: Duplicate range [10084-10085]
- Line 71: Duplicate range [10084-10085]
- Line 73: Duplicate range [10084-10085]
- Line 75: Duplicate range [10084-10085]
- Line 77: Duplicate range [10084-10085]
- Line 79: Duplicate range [10084-10085]

---

### File: dynamic/commentary_BACKUP/01-07-05-01.txt

**Errors:**
- Line 3: Duplicate range [10471-10471]
- Line 5: Duplicate range [10471-10471]
- Line 7: Duplicate range [10471-10471]
- Line 9: Duplicate range [10471-10471]
- Line 11: Duplicate range [10471-10471]

---

### File: dynamic/commentary_BACKUP/01-08-01-01.txt

**Errors:**
- Line 56: Non-sequential range [10472-10547] - Start (10472) < Previous start (10546)
- Line 36: Duplicate range [10498-10508]
- Line 44: Duplicate range [10509-10535]
- Line 50: Duplicate range [10536-10547]
- Line 62: Duplicate range [10472-10547]
- Line 64: Duplicate range [10472-10547]
- Line 66: Duplicate range [10472-10547]
- Line 68: Duplicate range [10472-10547]
- Line 70: Duplicate range [10472-10547]
- Line 72: Duplicate range [10472-10547]
- Line 74: Duplicate range [10472-10547]
- Line 76: Duplicate range [10472-10547]
- Line 78: Duplicate range [10472-10547]
- Line 80: Duplicate range [10472-10547]
- Line 82: Duplicate range [10472-10547]
- Line 84: Duplicate range [10472-10547]

---

### File: dynamic/commentary_BACKUP/01-08-02-01.txt

**Errors:**
- Line 18: Non-sequential range [10548-10560] - Start (10548) < Previous start (10550)
- Line 48: Non-sequential range [10548-10607] - Start (10548) < Previous start (10594)

---

### File: dynamic/commentary_BACKUP/01-08-04-01.txt

**Errors:**
- Line 6: Duplicate range [10722-10723]
- Line 11: Duplicate range [10722-10723]

---

### File: dynamic/commentary_BACKUP/01-08-04-02.txt

**Errors:**
- Line 46: Non-sequential range [10724-10724] - Start (10724) < Previous start (10755)
- Line 51: Duplicate range [10724-10724]

---

### File: dynamic/commentary_BACKUP/01-08-06-01.txt

**Errors:**
- Line 7: Duplicate range [10775-10781]
- Line 13: Duplicate range [10775-10781]
- Line 19: Duplicate range [10775-10781]
- Line 23: Duplicate range [10775-10781]
- Line 28: Duplicate range [10775-10781]
- Line 33: Duplicate range [10775-10781]

---

### File: dynamic/commentary_BACKUP/01-08-07-01.txt

**Errors:**
- Line 61: Non-sequential range [10782-10830] - Start (10782) < Previous start (10830)
- Line 106: Non-sequential range [10782-10830] - Start (10782) < Previous start (10820)
- Line 276: Non-sequential range [10782-11430] - Start (10782) < Previous start (11411)
- Line 56: Duplicate range [10830-10850]
- Line 66: Duplicate range [10782-10830]
- Line 71: Duplicate range [10788-10794]
- Line 76: Duplicate range [10790-10794]
- Line 81: Duplicate range [10795-10800]
- Line 86: Duplicate range [10801-10808]
- Line 91: Duplicate range [10808-10814]
- Line 96: Duplicate range [10815-10824]
- Line 101: Duplicate range [10820-10830]
- Line 106: Duplicate range [10782-10830]
- Line 111: Duplicate range [10782-10830]
- Line 116: Duplicate range [10782-10830]
- Line 126: Duplicate range [10831-10850]
- Line 281: Duplicate range [10782-11430]
- Line 286: Duplicate range [10782-11430]
- Line 291: Duplicate range [10782-11430]
- Line 296: Duplicate range [10782-11430]
- Line 301: Duplicate range [10782-11430]
- Line 306: Duplicate range [10782-11430]
- Line 311: Duplicate range [10782-11430]
- Line 316: Duplicate range [10782-11430]
- Line 321: Duplicate range [10782-11430]
- Line 326: Duplicate range [10782-11430]
- Line 331: Duplicate range [10782-11430]
- Line 336: Duplicate range [10782-11430]
- Line 341: Duplicate range [10782-11430]
- Line 346: Duplicate range [10782-11430]
- Line 351: Duplicate range [10782-11430]
- Line 356: Duplicate range [10782-11430]
- Line 361: Duplicate range [10782-11430]
- Line 366: Duplicate range [10782-11430]
- Line 371: Duplicate range [10782-11430]
- Line 376: Duplicate range [10782-11430]
- Line 381: Duplicate range [10782-11430]
- Line 386: Duplicate range [10782-11430]
- Line 391: Duplicate range [10782-11430]
- Line 396: Duplicate range [10782-11430]
- Line 401: Duplicate range [10782-11430]
- Line 406: Duplicate range [10782-11430]
- Line 411: Duplicate range [10782-11430]
- Line 416: Duplicate range [10782-11430]
- Line 421: Duplicate range [10782-11430]
- Line 426: Duplicate range [10782-11430]
- Line 431: Duplicate range [10782-11430]
- Line 436: Duplicate range [10782-11430]
- Line 441: Duplicate range [10782-11430]
- Line 446: Duplicate range [10782-11430]
- Line 451: Duplicate range [10782-11430]
- Line 456: Duplicate range [10782-11430]
- Line 461: Duplicate range [10782-11430]
- Line 466: Duplicate range [10782-11430]
- Line 471: Duplicate range [10782-11430]
- Line 476: Duplicate range [10782-11430]
- Line 481: Duplicate range [10782-11430]
- Line 486: Duplicate range [10782-11430]
- Line 489: Duplicate range [10782-11430]
- Line 494: Duplicate range [10782-11430]
- Line 497: Duplicate range [10782-11430]
- Line 499: Duplicate range [10782-11430]

---

### File: dynamic/commentary_BACKUP/01-08-08-01.txt

**Errors:**
- Line 6: Duplicate range [11334-11334]
- Line 10: Duplicate range [11334-11334]
- Line 14: Duplicate range [11334-11334]
- Line 18: Duplicate range [11334-11334]

---

### File: dynamic/commentary_BACKUP/01-09-01-01.txt

**Errors:**
- Line 140: Non-sequential range [11335-11434] - Start (11335) < Previous start (11428)
- Line 318: Non-sequential range [11335-11600] - Start (11335) < Previous start (11535)
- Line 839: Non-sequential range [11335-12000] - Start (11335) < Previous start (11901)
- Line 855: Non-sequential range [11535-11544] - Start (11535) < Previous start (12000)
- Line 919: Non-sequential range [11605-11634] - Start (11605) < Previous start (11629)
- Line 946: Non-sequential range [11335-11634] - Start (11335) < Previous start (11605)
- Line 977: Non-sequential range [11335-11634] - Start (11335) < Previous start (11634)
- Line 1132: Non-sequential range [11335-11634] - Start (11335) < Previous start (11634)
- Line 143: Duplicate range [11335-11434]
- Line 148: Duplicate range [11335-11434]
- Line 153: Duplicate range [11335-11434]
- Line 159: Duplicate range [11335-11434]
- Line 165: Duplicate range [11335-11434]
- Line 171: Duplicate range [11335-11434]
- Line 177: Duplicate range [11335-11434]
- Line 180: Duplicate range [11335-11434]
- Line 268: Duplicate range [11535-11600]
- Line 274: Duplicate range [11535-11600]
- Line 280: Duplicate range [11535-11600]
- Line 286: Duplicate range [11535-11600]
- Line 292: Duplicate range [11535-11600]
- Line 297: Duplicate range [11535-11600]
- Line 302: Duplicate range [11535-11600]
- Line 307: Duplicate range [11535-11600]
- Line 312: Duplicate range [11535-11600]
- Line 324: Duplicate range [11335-11600]
- Line 329: Duplicate range [11335-11600]
- Line 335: Duplicate range [11335-11600]
- Line 341: Duplicate range [11335-11600]
- Line 346: Duplicate range [11335-11600]
- Line 351: Duplicate range [11335-11600]
- Line 357: Duplicate range [11335-11600]
- Line 362: Duplicate range [11335-11600]
- Line 368: Duplicate range [11335-11600]
- Line 374: Duplicate range [11335-11600]
- Line 380: Duplicate range [11335-11600]
- Line 386: Duplicate range [11335-11600]
- Line 392: Duplicate range [11335-11600]
- Line 398: Duplicate range [11335-11600]
- Line 404: Duplicate range [11335-11600]
- Line 410: Duplicate range [11335-11600]
- Line 416: Duplicate range [11335-11600]
- Line 422: Duplicate range [11335-11600]
- Line 425: Duplicate range [11335-11600]
- Line 432: Duplicate range [11335-11600]
- Line 448: Duplicate range [11601-11700]
- Line 455: Duplicate range [11601-11700]
- Line 461: Duplicate range [11601-11700]
- Line 467: Duplicate range [11601-11700]
- Line 473: Duplicate range [11601-11700]
- Line 480: Duplicate range [11601-11700]
- Line 486: Duplicate range [11601-11700]
- Line 492: Duplicate range [11601-11700]
- Line 498: Duplicate range [11601-11700]
- Line 503: Duplicate range [11601-11700]
- Line 509: Duplicate range [11601-11700]
- Line 515: Duplicate range [11601-11700]
- Line 521: Duplicate range [11601-11700]
- Line 527: Duplicate range [11601-11700]
- Line 533: Duplicate range [11601-11700]
- Line 539: Duplicate range [11601-11700]
- Line 545: Duplicate range [11601-11700]
- Line 551: Duplicate range [11601-11700]
- Line 557: Duplicate range [11601-11700]
- Line 563: Duplicate range [11601-11700]
- Line 569: Duplicate range [11601-11700]
- Line 575: Duplicate range [11601-11700]
- Line 581: Duplicate range [11601-11700]
- Line 586: Duplicate range [11601-11700]
- Line 603: Duplicate range [11701-11800]
- Line 610: Duplicate range [11701-11800]
- Line 617: Duplicate range [11701-11800]
- Line 623: Duplicate range [11701-11800]
- Line 629: Duplicate range [11701-11800]
- Line 635: Duplicate range [11701-11800]
- Line 641: Duplicate range [11701-11800]
- Line 647: Duplicate range [11701-11800]
- Line 653: Duplicate range [11701-11800]
- Line 659: Duplicate range [11701-11800]
- Line 665: Duplicate range [11701-11800]
- Line 671: Duplicate range [11701-11800]
- Line 677: Duplicate range [11701-11800]
- Line 683: Duplicate range [11701-11800]
- Line 689: Duplicate range [11701-11800]
- Line 695: Duplicate range [11701-11800]
- Line 701: Duplicate range [11701-11800]
- Line 707: Duplicate range [11701-11800]
- Line 713: Duplicate range [11701-11800]
- Line 719: Duplicate range [11701-11800]
- Line 725: Duplicate range [11701-11800]
- Line 731: Duplicate range [11701-11800]
- Line 747: Duplicate range [11801-11900]
- Line 753: Duplicate range [11801-11900]
- Line 759: Duplicate range [11801-11900]
- Line 765: Duplicate range [11801-11900]
- Line 771: Duplicate range [11801-11900]
- Line 777: Duplicate range [11801-11900]
- Line 783: Duplicate range [11801-11900]
- Line 789: Duplicate range [11801-11900]
- Line 794: Duplicate range [11801-11900]
- Line 799: Duplicate range [11801-11900]
- Line 811: Duplicate range [11901-12000]
- Line 818: Duplicate range [11901-12000]
- Line 824: Duplicate range [11901-12000]
- Line 830: Duplicate range [11901-12000]
- Line 835: Duplicate range [11901-12000]
- Line 845: Duplicate range [11335-12000]
- Line 862: Duplicate range [11535-11544]
- Line 877: Duplicate range [11545-11571]
- Line 926: Duplicate range [11605-11634]
- Line 933: Duplicate range [11605-11634]
- Line 940: Duplicate range [11605-11634]
- Line 952: Duplicate range [11335-11634]
- Line 957: Duplicate range [11335-11634]
- Line 963: Duplicate range [11335-11634]
- Line 968: Duplicate range [11335-11634]
- Line 977: Duplicate range [11335-11634]
- Line 986: Duplicate range [11335-11634]
- Line 993: Duplicate range [11335-11634]
- Line 999: Duplicate range [11335-11634]
- Line 1005: Duplicate range [11335-11634]
- Line 1012: Duplicate range [11335-11634]
- Line 1019: Duplicate range [11335-11634]
- Line 1025: Duplicate range [11335-11634]
- Line 1031: Duplicate range [11335-11634]
- Line 1036: Duplicate range [11335-11634]
- Line 1041: Duplicate range [11335-11634]
- Line 1047: Duplicate range [11335-11634]
- Line 1052: Duplicate range [11335-11634]
- Line 1058: Duplicate range [11335-11634]
- Line 1063: Duplicate range [11335-11634]
- Line 1069: Duplicate range [11335-11634]
- Line 1075: Duplicate range [11335-11634]
- Line 1081: Duplicate range [11335-11634]
- Line 1087: Duplicate range [11335-11634]
- Line 1093: Duplicate range [11335-11634]
- Line 1099: Duplicate range [11335-11634]
- Line 1105: Duplicate range [11335-11634]
- Line 1111: Duplicate range [11335-11634]
- Line 1117: Duplicate range [11335-11634]
- Line 1123: Duplicate range [11335-11634]
- Line 1129: Duplicate range [11634-11634]
- Line 1132: Duplicate range [11335-11634]
- Line 1139: Duplicate range [11335-11634]
- Line 1145: Duplicate range [11335-11634]
- Line 1151: Duplicate range [11335-11634]
- Line 1158: Duplicate range [11335-11634]
- Line 1164: Duplicate range [11335-11634]
- Line 1170: Duplicate range [11335-11634]
- Line 1177: Duplicate range [11335-11634]
- Line 1183: Duplicate range [11335-11634]
- Line 1189: Duplicate range [11335-11634]
- Line 1196: Duplicate range [11335-11634]
- Line 1202: Duplicate range [11335-11634]
- Line 1208: Duplicate range [11335-11634]
- Line 1215: Duplicate range [11335-11634]
- Line 1221: Duplicate range [11335-11634]
- Line 1227: Duplicate range [11335-11634]
- Line 1234: Duplicate range [11335-11634]
- Line 1240: Duplicate range [11335-11634]
- Line 1246: Duplicate range [11335-11634]
- Line 1253: Duplicate range [11335-11634]
- Line 1259: Duplicate range [11335-11634]
- Line 1265: Duplicate range [11335-11634]
- Line 1272: Duplicate range [11335-11634]
- Line 1278: Duplicate range [11335-11634]
- Line 1284: Duplicate range [11335-11634]
- Line 1291: Duplicate range [11335-11634]
- Line 1297: Duplicate range [11335-11634]
- Line 1303: Duplicate range [11335-11634]
- Line 1310: Duplicate range [11335-11634]
- Line 1316: Duplicate range [11335-11634]
- Line 1322: Duplicate range [11335-11634]
- Line 1329: Duplicate range [11335-11634]
- Line 1335: Duplicate range [11335-11634]
- Line 1341: Duplicate range [11335-11634]
- Line 1348: Duplicate range [11335-11634]
- Line 1354: Duplicate range [11335-11634]
- Line 1360: Duplicate range [11335-11634]
- Line 1367: Duplicate range [11335-11634]
- Line 1373: Duplicate range [11335-11634]
- Line 1379: Duplicate range [11335-11634]
- Line 1386: Duplicate range [11335-11634]
- Line 1392: Duplicate range [11335-11634]
- Line 1398: Duplicate range [11335-11634]
- Line 1405: Duplicate range [11335-11634]
- Line 1411: Duplicate range [11335-11634]
- Line 1417: Duplicate range [11335-11634]
- Line 1424: Duplicate range [11335-11634]
- Line 1430: Duplicate range [11335-11634]
- Line 1436: Duplicate range [11335-11634]
- Line 1443: Duplicate range [11335-11634]
- Line 1449: Duplicate range [11335-11634]
- Line 1455: Duplicate range [11335-11634]
- Line 1462: Duplicate range [11335-11634]
- Line 1468: Duplicate range [11335-11634]
- Line 1474: Duplicate range [11335-11634]
- Line 1481: Duplicate range [11335-11634]
- Line 1487: Duplicate range [11335-11634]
- Line 1493: Duplicate range [11335-11634]
- Line 1500: Duplicate range [11335-11634]
- Line 1506: Duplicate range [11335-11634]
- Line 1512: Duplicate range [11335-11634]
- Line 1519: Duplicate range [11335-11634]
- Line 1525: Duplicate range [11335-11634]
- Line 1531: Duplicate range [11335-11634]
- Line 1538: Duplicate range [11335-11634]
- Line 1544: Duplicate range [11335-11634]
- Line 1550: Duplicate range [11335-11634]
- Line 1557: Duplicate range [11335-11634]
- Line 1563: Duplicate range [11335-11634]
- Line 1569: Duplicate range [11335-11634]
- Line 1576: Duplicate range [11335-11634]
- Line 1582: Duplicate range [11335-11634]
- Line 1588: Duplicate range [11335-11634]
- Line 1595: Duplicate range [11335-11634]
- Line 1601: Duplicate range [11335-11634]
- Line 1607: Duplicate range [11335-11634]
- Line 1614: Duplicate range [11335-11634]
- Line 1620: Duplicate range [11335-11634]
- Line 1626: Duplicate range [11335-11634]
- Line 1633: Duplicate range [11335-11634]
- Line 1639: Duplicate range [11335-11634]
- Line 1645: Duplicate range [11335-11634]
- Line 1652: Duplicate range [11335-11634]
- Line 1658: Duplicate range [11335-11634]
- Line 1664: Duplicate range [11335-11634]
- Line 1671: Duplicate range [11335-11634]
- Line 1677: Duplicate range [11335-11634]
- Line 1683: Duplicate range [11335-11634]
- Line 1690: Duplicate range [11335-11634]
- Line 1696: Duplicate range [11335-11634]
- Line 1702: Duplicate range [11335-11634]
- Line 1707: Duplicate range [11335-11634]
- Line 1714: Duplicate range [11335-11634]
- Line 1719: Duplicate range [11335-11634]
- Line 1725: Duplicate range [11335-11634]
- Line 1731: Duplicate range [11634-11634]

---

### File: dynamic/commentary_BACKUP/01-09-02-01.txt

**Errors:**
- Line 8: Duplicate range [12478-12499]
- Line 14: Duplicate range [12478-12499]
- Line 20: Duplicate range [12478-12499]
- Line 26: Duplicate range [12478-12499]
- Line 32: Duplicate range [12478-12499]
- Line 36: Duplicate range [12478-12499]

---

### File: dynamic/commentary_BACKUP/01-11-01-01.txt

**Errors:**
- Line 4: Duplicate range [13104-13108]
- Line 17: Duplicate range [13109-13115]
- Line 30: Duplicate range [13116-13121]
- Line 43: Duplicate range [13122-13127]
- Line 57: Duplicate range [13128-13135]
- Line 69: Duplicate range [13136-13141]
- Line 81: Duplicate range [13142-13148]
- Line 93: Duplicate range [13149-13157]
- Line 106: Duplicate range [13158-13165]
- Line 118: Duplicate range [13166-13175]
- Line 131: Duplicate range [13176-13181]
- Line 144: Duplicate range [13182-13191]
- Line 157: Duplicate range [13192-13202]
- Line 172: Duplicate range [13203-13212]
- Line 185: Duplicate range [13213-13220]
- Line 198: Duplicate range [13221-13232]
- Line 210: Duplicate range [13233-13243]
- Line 223: Duplicate range [13244-13255]
- Line 236: Duplicate range [13256-13270]
- Line 249: Duplicate range [13271-13280]
- Line 262: Duplicate range [13281-13290]
- Line 275: Duplicate range [13291-13305]
- Line 288: Duplicate range [13306-13316]
- Line 301: Duplicate range [13317-13327]
- Line 315: Duplicate range [13328-13341]
- Line 328: Duplicate range [13342-13356]
- Line 341: Duplicate range [13357-13372]
- Line 354: Duplicate range [13373-13384]
- Line 367: Duplicate range [13385-13404]
- Line 381: Duplicate range [13405-13417]
- Line 394: Duplicate range [13418-13430]

---

### File: dynamic/commentary_BACKUP/01-11-02-01.txt

**Errors:**
- Line 106: Non-sequential range [13432-13432] - Start (13432) < Previous start (13826)
- Line 111: Duplicate range [13432-13432]
- Line 116: Duplicate range [13432-13432]
- Line 121: Duplicate range [13432-13432]
- Line 126: Duplicate range [13432-13432]
- Line 131: Duplicate range [13432-13432]
- Line 136: Duplicate range [13432-13432]
- Line 141: Duplicate range [13432-13432]
- Line 146: Duplicate range [13432-13432]
- Line 151: Duplicate range [13432-13432]

---

### File: dynamic/commentary_BACKUP/01-12-01-01.txt

**Errors:**
- Line 253: Non-sequential range [14551-14700] - Start (14551) < Previous start (15651)

---

### File: dynamic/commentary_BACKUP/01-12-02-01.txt

**Errors:**
- Line 98: Non-sequential range [14528-14814] - Start (14528) < Previous start (14814)
- Line 61: Duplicate range [14754-14761]
- Line 69: Duplicate range [14762-14778]
- Line 79: Duplicate range [14779-14793]
- Line 100: Duplicate range [14528-14814]
- Line 102: Duplicate range [14528-14814]
- Line 104: Duplicate range [14528-14814]
- Line 106: Duplicate range [14528-14814]
- Line 108: Duplicate range [14528-14814]
- Line 110: Duplicate range [14528-14814]
- Line 112: Duplicate range [14528-14814]
- Line 114: Duplicate range [14528-14814]
- Line 116: Duplicate range [14528-14814]
- Line 118: Duplicate range [14528-14814]
- Line 120: Duplicate range [14528-14814]

---

### File: dynamic/commentary_BACKUP/01-12-04-01.txt

**Errors:**
- Line 81: Non-sequential range [15069-15083] - Start (15069) < Previous start (15211)

---

### File: dynamic/commentary_BACKUP/01-12-05-01.txt

**Errors:**
- Line 137: Non-sequential range [15415-15628] - Start (15415) < Previous start (15611)
- Line 3: Duplicate range [15415-15417]
- Line 5: Duplicate range [15415-15417]
- Line 7: Duplicate range [15415-15417]
- Line 11: Duplicate range [15418-15421]
- Line 13: Duplicate range [15418-15421]
- Line 15: Duplicate range [15418-15421]
- Line 19: Duplicate range [15422-15427]
- Line 21: Duplicate range [15422-15427]
- Line 23: Duplicate range [15422-15427]
- Line 27: Duplicate range [15428-15431]
- Line 29: Duplicate range [15428-15431]
- Line 31: Duplicate range [15428-15431]
- Line 35: Duplicate range [15432-15445]
- Line 37: Duplicate range [15432-15445]
- Line 39: Duplicate range [15432-15445]
- Line 43: Duplicate range [15446-15455]
- Line 45: Duplicate range [15446-15455]
- Line 47: Duplicate range [15446-15455]
- Line 51: Duplicate range [15456-15465]
- Line 53: Duplicate range [15456-15465]
- Line 55: Duplicate range [15456-15465]
- Line 59: Duplicate range [15466-15475]
- Line 61: Duplicate range [15466-15475]
- Line 63: Duplicate range [15466-15475]
- Line 67: Duplicate range [15476-15494]
- Line 69: Duplicate range [15476-15494]
- Line 71: Duplicate range [15476-15494]
- Line 75: Duplicate range [15495-15502]
- Line 77: Duplicate range [15495-15502]
- Line 79: Duplicate range [15495-15502]
- Line 83: Duplicate range [15503-15520]
- Line 85: Duplicate range [15503-15520]
- Line 87: Duplicate range [15503-15520]
- Line 91: Duplicate range [15521-15544]
- Line 93: Duplicate range [15521-15544]
- Line 95: Duplicate range [15521-15544]
- Line 99: Duplicate range [15545-15562]
- Line 101: Duplicate range [15545-15562]
- Line 103: Duplicate range [15545-15562]
- Line 107: Duplicate range [15563-15569]
- Line 109: Duplicate range [15563-15569]
- Line 111: Duplicate range [15563-15569]
- Line 115: Duplicate range [15570-15586]
- Line 117: Duplicate range [15570-15586]
- Line 119: Duplicate range [15570-15586]
- Line 123: Duplicate range [15587-15610]
- Line 125: Duplicate range [15587-15610]
- Line 127: Duplicate range [15587-15610]
- Line 131: Duplicate range [15611-15628]
- Line 133: Duplicate range [15611-15628]
- Line 135: Duplicate range [15611-15628]
- Line 139: Duplicate range [15415-15628]
- Line 141: Duplicate range [15415-15628]
- Line 143: Duplicate range [15415-15628]
- Line 145: Duplicate range [15415-15628]
- Line 147: Duplicate range [15415-15628]
- Line 149: Duplicate range [15415-15628]
- Line 151: Duplicate range [15415-15628]
- Line 153: Duplicate range [15415-15628]
- Line 155: Duplicate range [15415-15628]
- Line 157: Duplicate range [15415-15628]
- Line 159: Duplicate range [15415-15628]
- Line 161: Duplicate range [15415-15628]
- Line 163: Duplicate range [15415-15628]
- Line 165: Duplicate range [15415-15628]
- Line 167: Duplicate range [15415-15628]
- Line 169: Duplicate range [15415-15628]
- Line 171: Duplicate range [15415-15628]
- Line 173: Duplicate range [15415-15628]
- Line 175: Duplicate range [15415-15628]
- Line 177: Duplicate range [15415-15628]
- Line 179: Duplicate range [15415-15628]
- Line 181: Duplicate range [15415-15628]

---

### File: dynamic/commentary_BACKUP/01-12-05-02.txt

**Errors:**
- Line 39: Non-sequential range [15750-15768] - Start (15750) < Previous start (15764)
- Line 52: Non-sequential range [15629-15629] - Start (15629) < Previous start (15750)
- Line 55: Duplicate range [15629-15629]
- Line 60: Duplicate range [15629-15768]
- Line 62: Duplicate range [15629-15768]
- Line 64: Duplicate range [15629-15768]
- Line 66: Duplicate range [15629-15768]
- Line 68: Duplicate range [15629-15768]
- Line 70: Duplicate range [15629-15768]
- Line 72: Duplicate range [15629-15768]
- Line 74: Duplicate range [15629-15768]
- Line 76: Duplicate range [15629-15768]
- Line 78: Duplicate range [15629-15768]
- Line 80: Duplicate range [15629-15768]
- Line 82: Duplicate range [15629-15768]
- Line 84: Duplicate range [15629-15768]

---

### File: dynamic/commentary_BACKUP/01-12-06-01.txt

**Errors:**
- Line 8: Duplicate range [15769-15777]
- Line 13: Duplicate range [15769-15777]

---

### File: dynamic/commentary_BACKUP/01-13-03-01.txt

**Errors:**
- Line 112: Non-sequential range [16711-16716] - Start (16711) < Previous start (17201)

---

### File: dynamic/commentary_BACKUP/01-13-04-01.txt

**Errors:**
- Line 3: Duplicate range [16769-16771]
- Line 7: Duplicate range [16772-16777]
- Line 11: Duplicate range [16778-16783]
- Line 15: Duplicate range [16784-16788]
- Line 19: Duplicate range [16789-16796]
- Line 23: Duplicate range [16797-16802]
- Line 27: Duplicate range [16803-16808]
- Line 31: Duplicate range [16809-16814]
- Line 35: Duplicate range [16815-16820]
- Line 39: Duplicate range [16821-16828]
- Line 43: Duplicate range [16829-16835]
- Line 49: Duplicate range [16842-16848]
- Line 55: Duplicate range [16854-16862]

---

### File: dynamic/commentary_BACKUP/01-13-05-01.txt

**Errors:**
- Line 34: Duplicate range [16903-16908]

---

### File: dynamic/commentary_BACKUP/01-14-02-01.txt

**Errors:**
- Line 80: Non-sequential range [17624-17650] - Start (17624) < Previous start (17645)

---

### File: dynamic/commentary_BACKUP/01-14-03-02.txt

**Errors:**
- Line 7: Duplicate range [18262-18273]
- Line 12: Duplicate range [18262-18273]
- Line 17: Duplicate range [18262-18273]
- Line 21: Duplicate range [18262-18273]
- Line 26: Duplicate range [18262-18273]

---

### File: dynamic/commentary_BACKUP/01-14-05-01.txt

**Errors:**
- Line 146: Non-sequential range [18610-18830] - Start (18610) < Previous start (18810)
- Line 241: Non-sequential range [18610-18830] - Start (18610) < Previous start (18810)
- Line 281: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 326: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 366: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 411: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 456: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 501: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 546: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 591: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 636: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 681: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 726: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 771: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 816: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 861: Non-sequential range [18610-18830] - Start (18610) < Previous start (18695)
- Line 6: Duplicate range [18610-18615]
- Line 16: Duplicate range [18616-18620]
- Line 26: Duplicate range [18620-18631]
- Line 31: Duplicate range [18620-18631]
- Line 41: Duplicate range [18631-18641]
- Line 46: Duplicate range [18631-18641]
- Line 56: Duplicate range [18642-18659]
- Line 61: Duplicate range [18642-18659]
- Line 71: Duplicate range [18650-18670]
- Line 76: Duplicate range [18650-18670]
- Line 86: Duplicate range [18670-18695]
- Line 96: Duplicate range [18695-18720]
- Line 106: Duplicate range [18720-18745]
- Line 116: Duplicate range [18745-18770]
- Line 126: Duplicate range [18770-18790]
- Line 136: Duplicate range [18790-18810]
- Line 156: Duplicate range [18610-18620]
- Line 161: Duplicate range [18620-18631]
- Line 166: Duplicate range [18620-18631]
- Line 171: Duplicate range [18631-18641]
- Line 176: Duplicate range [18631-18641]
- Line 181: Duplicate range [18642-18659]
- Line 186: Duplicate range [18642-18659]
- Line 191: Duplicate range [18650-18670]
- Line 196: Duplicate range [18650-18670]
- Line 201: Duplicate range [18650-18670]
- Line 206: Duplicate range [18670-18695]
- Line 211: Duplicate range [18695-18720]
- Line 216: Duplicate range [18720-18745]
- Line 221: Duplicate range [18745-18770]
- Line 226: Duplicate range [18770-18790]
- Line 231: Duplicate range [18790-18810]
- Line 236: Duplicate range [18810-18830]
- Line 241: Duplicate range [18610-18830]
- Line 246: Duplicate range [18610-18620]
- Line 251: Duplicate range [18620-18631]
- Line 256: Duplicate range [18631-18641]
- Line 261: Duplicate range [18642-18659]
- Line 266: Duplicate range [18650-18670]
- Line 271: Duplicate range [18670-18695]
- Line 281: Duplicate range [18610-18830]
- Line 286: Duplicate range [18610-18615]
- Line 291: Duplicate range [18616-18620]
- Line 296: Duplicate range [18620-18631]
- Line 301: Duplicate range [18631-18641]
- Line 306: Duplicate range [18642-18659]
- Line 311: Duplicate range [18650-18670]
- Line 316: Duplicate range [18670-18695]
- Line 321: Duplicate range [18695-18830]
- Line 326: Duplicate range [18610-18830]
- Line 331: Duplicate range [18610-18620]
- Line 336: Duplicate range [18620-18631]
- Line 341: Duplicate range [18631-18641]
- Line 346: Duplicate range [18642-18659]
- Line 351: Duplicate range [18650-18670]
- Line 356: Duplicate range [18670-18695]
- Line 361: Duplicate range [18695-18830]
- Line 366: Duplicate range [18610-18830]
- Line 371: Duplicate range [18610-18615]
- Line 376: Duplicate range [18616-18620]
- Line 381: Duplicate range [18620-18631]
- Line 386: Duplicate range [18631-18641]
- Line 391: Duplicate range [18642-18659]
- Line 396: Duplicate range [18650-18670]
- Line 401: Duplicate range [18670-18695]
- Line 406: Duplicate range [18695-18830]
- Line 411: Duplicate range [18610-18830]
- Line 416: Duplicate range [18610-18830]
- Line 421: Duplicate range [18610-18620]
- Line 426: Duplicate range [18620-18631]
- Line 431: Duplicate range [18631-18641]
- Line 436: Duplicate range [18642-18659]
- Line 441: Duplicate range [18650-18670]
- Line 446: Duplicate range [18670-18695]
- Line 451: Duplicate range [18695-18830]
- Line 456: Duplicate range [18610-18830]
- Line 461: Duplicate range [18610-18615]
- Line 466: Duplicate range [18616-18620]
- Line 471: Duplicate range [18620-18631]
- Line 476: Duplicate range [18631-18641]
- Line 481: Duplicate range [18642-18659]
- Line 486: Duplicate range [18650-18670]
- Line 491: Duplicate range [18670-18695]
- Line 496: Duplicate range [18695-18830]
- Line 501: Duplicate range [18610-18830]
- Line 506: Duplicate range [18610-18830]
- Line 511: Duplicate range [18610-18620]
- Line 516: Duplicate range [18620-18631]
- Line 521: Duplicate range [18631-18641]
- Line 526: Duplicate range [18642-18659]
- Line 531: Duplicate range [18650-18670]
- Line 536: Duplicate range [18670-18695]
- Line 541: Duplicate range [18695-18830]
- Line 546: Duplicate range [18610-18830]
- Line 551: Duplicate range [18610-18830]
- Line 556: Duplicate range [18610-18620]
- Line 561: Duplicate range [18620-18631]
- Line 566: Duplicate range [18631-18641]
- Line 571: Duplicate range [18642-18659]
- Line 576: Duplicate range [18650-18670]
- Line 581: Duplicate range [18670-18695]
- Line 586: Duplicate range [18695-18830]
- Line 591: Duplicate range [18610-18830]
- Line 596: Duplicate range [18610-18830]
- Line 601: Duplicate range [18610-18620]
- Line 606: Duplicate range [18620-18631]
- Line 611: Duplicate range [18631-18641]
- Line 616: Duplicate range [18642-18659]
- Line 621: Duplicate range [18650-18670]
- Line 626: Duplicate range [18670-18695]
- Line 631: Duplicate range [18695-18830]
- Line 636: Duplicate range [18610-18830]
- Line 641: Duplicate range [18610-18830]
- Line 646: Duplicate range [18610-18620]
- Line 651: Duplicate range [18620-18631]
- Line 656: Duplicate range [18631-18641]
- Line 661: Duplicate range [18642-18659]
- Line 666: Duplicate range [18650-18670]
- Line 671: Duplicate range [18670-18695]
- Line 676: Duplicate range [18695-18830]
- Line 681: Duplicate range [18610-18830]
- Line 686: Duplicate range [18610-18830]
- Line 691: Duplicate range [18610-18620]
- Line 696: Duplicate range [18620-18631]
- Line 701: Duplicate range [18631-18641]
- Line 706: Duplicate range [18642-18659]
- Line 711: Duplicate range [18650-18670]
- Line 716: Duplicate range [18670-18695]
- Line 721: Duplicate range [18695-18830]
- Line 726: Duplicate range [18610-18830]
- Line 731: Duplicate range [18610-18830]
- Line 736: Duplicate range [18610-18620]
- Line 741: Duplicate range [18620-18631]
- Line 746: Duplicate range [18631-18641]
- Line 751: Duplicate range [18642-18659]
- Line 756: Duplicate range [18650-18670]
- Line 761: Duplicate range [18670-18695]
- Line 766: Duplicate range [18695-18830]
- Line 771: Duplicate range [18610-18830]
- Line 776: Duplicate range [18610-18830]
- Line 781: Duplicate range [18610-18620]
- Line 786: Duplicate range [18620-18631]
- Line 791: Duplicate range [18631-18641]
- Line 796: Duplicate range [18642-18659]
- Line 801: Duplicate range [18650-18670]
- Line 806: Duplicate range [18670-18695]
- Line 811: Duplicate range [18695-18830]
- Line 816: Duplicate range [18610-18830]
- Line 821: Duplicate range [18610-18830]
- Line 826: Duplicate range [18610-18620]
- Line 831: Duplicate range [18620-18631]
- Line 836: Duplicate range [18631-18641]
- Line 841: Duplicate range [18642-18659]
- Line 846: Duplicate range [18650-18670]
- Line 851: Duplicate range [18670-18695]
- Line 856: Duplicate range [18695-18830]
- Line 861: Duplicate range [18610-18830]
- Line 866: Duplicate range [18610-18830]
- Line 871: Duplicate range [18610-18830]
- Line 874: Duplicate range [18610-18830]
- Line 875: Duplicate range [18610-18830]

---

### File: dynamic/commentary_BACKUP/01-14-06-01.txt

**Errors:**
- Line 87: Non-sequential range [19303-19303] - Start (19303) < Previous start (19400)
- Line 90: Duplicate range [19303-19303]
- Line 94: Duplicate range [19303-19303]

---

### File: dynamic/commentary_BACKUP/01-14-07-01.txt

**Errors:**
- Line 6: Duplicate range [19404-19404]
- Line 11: Duplicate range [19404-19404]
- Line 15: Duplicate range [19404-19404]
- Line 19: Duplicate range [19404-19404]

---

### File: dynamic/commentary_BACKUP/01-14-07-02.txt

**Errors:**
- Line 6: Duplicate range [19405-19405]
- Line 11: Duplicate range [19405-19405]
- Line 15: Duplicate range [19405-19405]
- Line 19: Duplicate range [19405-19405]

---

### File: dynamic/commentary_BACKUP/01-14-07-03.txt

**Errors:**
- Line 10: Duplicate range [19406-19420]
- Line 15: Duplicate range [19406-19420]

---

### File: dynamic/commentary_BACKUP/01-14-10-01.txt

**Errors:**
- Line 79: Non-sequential range [19975-19975] - Start (19975) < Previous start (20140)
- Line 82: Duplicate range [19975-19975]
- Line 85: Duplicate range [19975-19975]
- Line 97: Duplicate range [19975-20146]
- Line 99: Duplicate range [19975-20146]
- Line 101: Duplicate range [19975-20146]
- Line 103: Duplicate range [19975-20146]
- Line 105: Duplicate range [19975-20146]
- Line 107: Duplicate range [19975-20146]
- Line 109: Duplicate range [19975-20146]
- Line 111: Duplicate range [19975-20146]
- Line 113: Duplicate range [19975-20146]
- Line 115: Duplicate range [19975-20146]
- Line 117: Duplicate range [19975-20146]

---

### File: dynamic/commentary_BACKUP/01-14-11-01.txt

**Errors:**
- Line 46: Non-sequential range [20147-20147] - Start (20147) < Previous start (20200)
- Line 49: Duplicate range [20147-20147]
- Line 56: Duplicate range [20147-20147]
- Line 65: Duplicate range [20147-20147]
- Line 68: Duplicate range [20147-20147]
- Line 73: Duplicate range [20147-20147]

---

### File: dynamic/commentary_BACKUP/01-14-12-01.txt

**Errors:**
- Line 53: Non-sequential range [20212-20212] - Start (20212) < Previous start (20280)
- Line 60: Duplicate range [20212-20212]
- Line 69: Duplicate range [20212-20212]
- Line 74: Duplicate range [20212-20212]
- Line 81: Duplicate range [20212-20212]
- Line 84: Duplicate range [20212-20212]

---

### File: dynamic/commentary_BACKUP/01-14-13-01.txt

**Errors:**
- Line 71: Non-sequential range [20285-20285] - Start (20285) < Previous start (20425)
- Line 78: Duplicate range [20285-20285]
- Line 89: Duplicate range [20285-20285]
- Line 98: Duplicate range [20285-20285]
- Line 103: Duplicate range [20285-20285]
- Line 110: Duplicate range [20285-20285]
- Line 115: Duplicate range [20285-20426]
- Line 117: Duplicate range [20285-20426]
- Line 119: Duplicate range [20285-20426]
- Line 121: Duplicate range [20285-20426]
- Line 123: Duplicate range [20285-20426]
- Line 125: Duplicate range [20285-20426]
- Line 127: Duplicate range [20285-20426]
- Line 129: Duplicate range [20285-20426]
- Line 131: Duplicate range [20285-20426]

---

### File: dynamic/commentary_BACKUP/02-15-01-01.txt

**Errors:**
- Line 263: Duplicate range [284-297]
- Line 278: Duplicate range [298-313]

---

### File: dynamic/commentary_BACKUP/02-15-02-01.txt

**Errors:**
- Line 82: Non-sequential range [474-668] - Start (474) < Previous start (664)
- Line 85: Duplicate range [474-668]

---

### File: dynamic/commentary_BACKUP/02-15-03-01.txt

**Errors:**
- Line 11: Non-sequential range [669-684] - Start (669) < Previous start (677)
- Line 14: Duplicate range [669-684]

---

### File: dynamic/commentary_BACKUP/02-16-01-01.txt

**Errors:**
- Line 6: Duplicate range [685-705]
- Line 23: Duplicate range [706-714]
- Line 39: Duplicate range [715-727]
- Line 54: Duplicate range [728-750]
- Line 67: Duplicate range [751-756]
- Line 80: Duplicate range [757-762]
- Line 96: Duplicate range [763-774]
- Line 110: Duplicate range [775-779]
- Line 122: Duplicate range [780-784]
- Line 134: Duplicate range [785-789]
- Line 147: Duplicate range [790-795]
- Line 158: Duplicate range [796-802]
- Line 170: Duplicate range [803-806]
- Line 183: Duplicate range [807-823]
- Line 196: Duplicate range [824-839]
- Line 209: Duplicate range [840-847]
- Line 222: Duplicate range [848-858]
- Line 235: Duplicate range [859-869]
- Line 250: Duplicate range [870-884]
- Line 262: Duplicate range [885-896]
- Line 275: Duplicate range [897-902]
- Line 287: Duplicate range [903-908]
- Line 300: Duplicate range [909-920]
- Line 313: Duplicate range [921-932]
- Line 326: Duplicate range [933-937]
- Line 345: Duplicate range [938-977]
- Line 357: Duplicate range [978-985]
- Line 372: Duplicate range [986-1014]
- Line 391: Duplicate range [1015-1020]

---

### File: dynamic/commentary_BACKUP/02-16-05-01.txt

**Errors:**
- Line 3: Duplicate range [1638-1650]
- Line 5: Duplicate range [1638-1650]
- Line 9: Duplicate range [1651-1660]
- Line 13: Duplicate range [1661-1670]
- Line 17: Duplicate range [1671-1680]
- Line 21: Duplicate range [1681-1690]
- Line 25: Duplicate range [1691-1700]
- Line 29: Duplicate range [1701-1710]
- Line 33: Duplicate range [1711-1720]
- Line 37: Duplicate range [1721-1730]
- Line 41: Duplicate range [1731-1740]
- Line 45: Duplicate range [1741-1750]

---

### File: dynamic/commentary_BACKUP/02-17-01-01.txt

**Errors:**
- Line 3: Duplicate range [1754-1766]
- Line 5: Duplicate range [1754-1766]
- Line 7: Duplicate range [1754-1766]
- Line 11: Duplicate range [1767-1781]
- Line 13: Duplicate range [1767-1781]
- Line 17: Duplicate range [1782-1808]
- Line 19: Duplicate range [1782-1808]
- Line 23: Duplicate range [1809-1846]
- Line 25: Duplicate range [1809-1846]
- Line 29: Duplicate range [1847-1858]
- Line 31: Duplicate range [1847-1858]
- Line 35: Duplicate range [1859-1860]
- Line 37: Duplicate range [1859-1860]

---

### File: dynamic/commentary_BACKUP/02-17-02-01.txt

**Errors:**
- Line 99: Non-sequential range [1921-1930] - Start (1921) < Previous start (2221)

---

### File: dynamic/commentary_BACKUP/02-17-03-01.txt

**Errors:**
- Line 3: Duplicate range [2051-2063]
- Line 5: Duplicate range [2051-2063]
- Line 7: Duplicate range [2051-2063]
- Line 11: Duplicate range [2061-2063]
- Line 13: Duplicate range [2061-2063]

---

### File: dynamic/commentary_BACKUP/02-17-04-01.txt

**Errors:**
- Line 182: Non-sequential range [2381-2400] - Start (2381) < Previous start (2391)

---

### File: dynamic/commentary_BACKUP/02-17-05-01.txt

**Errors:**
- Line 33: Non-sequential range [2689-2778] - Start (2689) < Previous start (2744)
- Line 3: Duplicate range [2689-2760]
- Line 5: Duplicate range [2689-2760]
- Line 7: Duplicate range [2689-2760]
- Line 9: Duplicate range [2689-2760]
- Line 13: Duplicate range [2711-2743]
- Line 15: Duplicate range [2711-2743]
- Line 19: Duplicate range [2744-2778]
- Line 21: Duplicate range [2744-2778]
- Line 35: Duplicate range [2689-2778]
- Line 37: Duplicate range [2689-2778]
- Line 39: Duplicate range [2689-2778]
- Line 41: Duplicate range [2689-2778]
- Line 43: Duplicate range [2689-2778]
- Line 45: Duplicate range [2689-2778]
- Line 47: Duplicate range [2689-2778]
- Line 49: Duplicate range [2689-2778]

---

### File: dynamic/commentary_BACKUP/02-17-06-01.txt

**Errors:**
- Line 76: Non-sequential range [2779-3004] - Start (2779) < Previous start (2984)
- Line 85: Non-sequential range [2779-3004] - Start (2779) < Previous start (3004)
- Line 149: Non-sequential range [2779-3004] - Start (2779) < Previous start (3004)
- Line 4: Duplicate range [2779-2783]
- Line 7: Duplicate range [2779-2783]
- Line 13: Duplicate range [2784-2786]
- Line 19: Duplicate range [2787-2798]
- Line 28: Duplicate range [2799-2819]
- Line 31: Duplicate range [2799-2819]
- Line 37: Duplicate range [2820-2836]
- Line 43: Duplicate range [2836-2870]
- Line 49: Duplicate range [2871-2910]
- Line 55: Duplicate range [2911-2963]
- Line 61: Duplicate range [2963-2983]
- Line 67: Duplicate range [2984-3004]
- Line 70: Duplicate range [2984-3004]
- Line 73: Duplicate range [2984-3004]
- Line 79: Duplicate range [2779-3004]
- Line 85: Duplicate range [2779-3004]
- Line 91: Duplicate range [2779-3004]
- Line 98: Duplicate range [2779-3004]
- Line 104: Duplicate range [2779-3004]
- Line 109: Duplicate range [2779-3004]
- Line 114: Duplicate range [2779-3004]
- Line 119: Duplicate range [2779-3004]
- Line 124: Duplicate range [2779-3004]
- Line 129: Duplicate range [2779-3004]
- Line 135: Duplicate range [2779-3004]
- Line 141: Duplicate range [2779-3004]
- Line 146: Duplicate range [3004-3004]
- Line 149: Duplicate range [2779-3004]
- Line 156: Duplicate range [2779-3004]
- Line 162: Duplicate range [2779-3004]
- Line 168: Duplicate range [2779-3004]
- Line 175: Duplicate range [2779-3004]
- Line 182: Duplicate range [2779-3004]
- Line 188: Duplicate range [2779-3004]
- Line 195: Duplicate range [2779-3004]
- Line 202: Duplicate range [2779-3004]
- Line 208: Duplicate range [2779-3004]
- Line 214: Duplicate range [2779-3004]
- Line 220: Duplicate range [3004-3004]

---

### File: dynamic/commentary_BACKUP/02-17-09-01.txt

**Errors:**
- Line 3: Duplicate range [3124-3135]
- Line 5: Duplicate range [3124-3135]
- Line 7: Duplicate range [3124-3135]
- Line 11: Duplicate range [3136-3145]
- Line 15: Duplicate range [3146-3155]
- Line 17: Duplicate range [3146-3155]
- Line 21: Duplicate range [3156-3165]
- Line 25: Duplicate range [3166-3175]
- Line 29: Duplicate range [3176-3185]

---

### File: dynamic/commentary_BACKUP/02-17-10-01.txt

**Errors:**
- Line 48: Non-sequential range [3307-3353] - Start (3307) < Previous start (3345)
- Line 50: Duplicate range [3307-3353]
- Line 52: Duplicate range [3307-3353]
- Line 54: Duplicate range [3307-3353]
- Line 56: Duplicate range [3307-3353]
- Line 58: Duplicate range [3307-3353]
- Line 60: Duplicate range [3307-3353]
- Line 62: Duplicate range [3307-3353]
- Line 64: Duplicate range [3307-3353]
- Line 66: Duplicate range [3307-3353]
- Line 68: Duplicate range [3307-3353]
- Line 70: Duplicate range [3307-3353]

---

### File: dynamic/commentary_BACKUP/02-17-11-01.txt

**Errors:**
- Line 37: Non-sequential range [3354-3403] - Start (3354) < Previous start (3401)
- Line 55: Non-sequential range [3354-3403] - Start (3354) < Previous start (3403)
- Line 166: Non-sequential range [3354-3403] - Start (3354) < Previous start (3403)
- Line 223: Non-sequential range [3354-3403] - Start (3354) < Previous start (3403)
- Line 4: Duplicate range [3354-3371]
- Line 7: Duplicate range [3354-3371]
- Line 10: Duplicate range [3354-3371]
- Line 16: Duplicate range [3372-3388]
- Line 19: Duplicate range [3372-3388]
- Line 28: Duplicate range [3389-3403]
- Line 31: Duplicate range [3389-3403]
- Line 40: Duplicate range [3354-3403]
- Line 43: Duplicate range [3354-3403]
- Line 46: Duplicate range [3354-3403]
- Line 49: Duplicate range [3354-3403]
- Line 55: Duplicate range [3354-3403]
- Line 61: Duplicate range [3354-3403]
- Line 67: Duplicate range [3354-3403]
- Line 73: Duplicate range [3354-3403]
- Line 78: Duplicate range [3354-3403]
- Line 84: Duplicate range [3354-3403]
- Line 90: Duplicate range [3354-3403]
- Line 96: Duplicate range [3354-3403]
- Line 101: Duplicate range [3354-3403]
- Line 106: Duplicate range [3354-3403]
- Line 112: Duplicate range [3354-3403]
- Line 117: Duplicate range [3354-3403]
- Line 122: Duplicate range [3354-3403]
- Line 127: Duplicate range [3354-3403]
- Line 133: Duplicate range [3354-3403]
- Line 138: Duplicate range [3354-3403]
- Line 143: Duplicate range [3354-3403]
- Line 148: Duplicate range [3354-3403]
- Line 153: Duplicate range [3354-3403]
- Line 158: Duplicate range [3354-3403]
- Line 163: Duplicate range [3403-3403]
- Line 166: Duplicate range [3354-3403]
- Line 171: Duplicate range [3354-3403]
- Line 176: Duplicate range [3354-3403]
- Line 181: Duplicate range [3354-3403]
- Line 186: Duplicate range [3354-3403]
- Line 190: Duplicate range [3354-3403]
- Line 195: Duplicate range [3354-3403]
- Line 200: Duplicate range [3354-3403]
- Line 205: Duplicate range [3354-3403]
- Line 210: Duplicate range [3354-3403]
- Line 215: Duplicate range [3354-3403]
- Line 220: Duplicate range [3403-3403]
- Line 223: Duplicate range [3354-3403]
- Line 230: Duplicate range [3354-3403]
- Line 236: Duplicate range [3354-3403]
- Line 242: Duplicate range [3354-3403]
- Line 248: Duplicate range [3354-3403]
- Line 254: Duplicate range [3354-3403]
- Line 260: Duplicate range [3354-3403]
- Line 265: Duplicate range [3354-3403]
- Line 270: Duplicate range [3354-3403]
- Line 276: Duplicate range [3354-3403]
- Line 281: Duplicate range [3354-3403]
- Line 287: Duplicate range [3354-3403]
- Line 292: Duplicate range [3354-3403]
- Line 298: Duplicate range [3354-3403]
- Line 305: Duplicate range [3354-3403]
- Line 311: Duplicate range [3354-3403]
- Line 316: Duplicate range [3354-3403]
- Line 321: Duplicate range [3403-3403]

---

### File: dynamic/commentary_BACKUP/02-18-02-02.txt

**Errors:**
- Line 7: Duplicate range [4401-4405]
- Line 12: Duplicate range [4401-4405]
- Line 18: Duplicate range [4401-4405]
- Line 22: Duplicate range [4401-4405]
- Line 28: Duplicate range [4401-4405]

---

### File: dynamic/commentary_BACKUP/02-18-03-01.txt

**Errors:**
- Line 6: Duplicate range [4425-4425]
- Line 11: Duplicate range [4425-4425]
- Line 17: Duplicate range [4425-4425]
- Line 21: Duplicate range [4425-4425]

---

### File: dynamic/commentary_BACKUP/02-18-03-02.txt

**Errors:**
- Line 6: Duplicate range [4426-4426]
- Line 10: Duplicate range [4426-4426]
- Line 14: Duplicate range [4426-4426]
- Line 18: Duplicate range [4426-4426]

---

### File: dynamic/commentary_BACKUP/02-18-03-03.txt

**Errors:**
- Line 6: Duplicate range [4427-4427]
- Line 11: Duplicate range [4427-4427]
- Line 15: Duplicate range [4427-4427]
- Line 20: Duplicate range [4427-4427]

---

### File: dynamic/commentary_BACKUP/02-18-04-01.txt

**Errors:**
- Line 198: Non-sequential range [4468-4600] - Start (4468) < Previous start (4596)
- Line 18: Duplicate range [4470-4472]
- Line 205: Duplicate range [4468-4600]
- Line 211: Duplicate range [4468-4600]

---

### File: dynamic/commentary_BACKUP/02-18-06-01.txt

**Errors:**
- Line 74: Non-sequential range [4696-4750] - Start (4696) < Previous start (4741)
- Line 6: Duplicate range [4696-4704]
- Line 22: Duplicate range [4705-4711]
- Line 34: Duplicate range [4712-4730]
- Line 49: Duplicate range [4731-4740]
- Line 64: Duplicate range [4741-4750]
- Line 77: Duplicate range [4696-4750]
- Line 86: Duplicate range [4696-4750]
- Line 89: Duplicate range [4696-4750]

---

### File: dynamic/commentary_BACKUP/02-18-07-01.txt

**Errors:**
- Line 82: Non-sequential range [4747-4914] - Start (4747) < Previous start (4903)
- Line 94: Non-sequential range [4747-4914] - Start (4747) < Previous start (4914)
- Line 139: Non-sequential range [4747-4914] - Start (4747) < Previous start (4914)
- Line 7: Duplicate range [4747-4751]
- Line 13: Duplicate range [4752-4761]
- Line 43: Duplicate range [4802-4820]
- Line 85: Duplicate range [4747-4914]
- Line 88: Duplicate range [4747-4914]
- Line 94: Duplicate range [4747-4914]
- Line 100: Duplicate range [4747-4914]
- Line 106: Duplicate range [4747-4914]
- Line 111: Duplicate range [4747-4914]
- Line 116: Duplicate range [4747-4914]
- Line 121: Duplicate range [4747-4914]
- Line 126: Duplicate range [4747-4914]
- Line 131: Duplicate range [4747-4914]
- Line 136: Duplicate range [4914-4914]
- Line 139: Duplicate range [4747-4914]
- Line 145: Duplicate range [4747-4914]
- Line 151: Duplicate range [4747-4914]
- Line 157: Duplicate range [4747-4914]
- Line 163: Duplicate range [4747-4914]
- Line 169: Duplicate range [4747-4914]
- Line 174: Duplicate range [4747-4914]
- Line 180: Duplicate range [4747-4914]
- Line 185: Duplicate range [4747-4914]
- Line 190: Duplicate range [4747-4914]
- Line 196: Duplicate range [4747-4914]
- Line 202: Duplicate range [4747-4914]
- Line 207: Duplicate range [4747-4914]
- Line 213: Duplicate range [4747-4914]
- Line 218: Duplicate range [4914-4914]

---

### File: dynamic/commentary_BACKUP/02-18-08-01.txt

**Errors:**
- Line 59: Non-sequential range [4916-5034] - Start (4916) < Previous start (5026)
- Line 3: Duplicate range [4916-4925]
- Line 5: Duplicate range [4916-4925]
- Line 7: Duplicate range [4916-4925]
- Line 9: Duplicate range [4916-4925]
- Line 13: Duplicate range [4926-4945]
- Line 15: Duplicate range [4926-4945]
- Line 17: Duplicate range [4926-4945]
- Line 21: Duplicate range [4946-4965]
- Line 23: Duplicate range [4946-4965]
- Line 25: Duplicate range [4946-4965]
- Line 29: Duplicate range [4966-4985]
- Line 31: Duplicate range [4966-4985]
- Line 33: Duplicate range [4966-4985]
- Line 37: Duplicate range [4986-5005]
- Line 39: Duplicate range [4986-5005]
- Line 41: Duplicate range [4986-5005]
- Line 45: Duplicate range [5006-5025]
- Line 47: Duplicate range [5006-5025]
- Line 49: Duplicate range [5006-5025]
- Line 53: Duplicate range [5026-5034]
- Line 55: Duplicate range [5026-5034]
- Line 57: Duplicate range [5026-5034]
- Line 61: Duplicate range [4916-5034]
- Line 63: Duplicate range [4916-5034]
- Line 65: Duplicate range [4916-5034]
- Line 67: Duplicate range [4916-5034]
- Line 69: Duplicate range [4916-5034]
- Line 71: Duplicate range [4916-5034]
- Line 73: Duplicate range [4916-5034]
- Line 75: Duplicate range [4916-5034]
- Line 77: Duplicate range [4916-5034]
- Line 79: Duplicate range [4916-5034]
- Line 81: Duplicate range [4916-5034]
- Line 83: Duplicate range [4916-5034]
- Line 85: Duplicate range [4916-5034]
- Line 87: Duplicate range [4916-5034]
- Line 89: Duplicate range [4916-5034]
- Line 91: Duplicate range [4916-5034]
- Line 93: Duplicate range [4916-5034]
- Line 95: Duplicate range [4916-5034]
- Line 97: Duplicate range [4916-5034]
- Line 99: Duplicate range [4916-5034]
- Line 101: Duplicate range [4916-5034]
- Line 103: Duplicate range [4916-5034]
- Line 105: Duplicate range [4916-5034]

---

### File: dynamic/commentary_BACKUP/02-18-08-02.txt

**Errors:**
- Line 3: Duplicate range [5035-5036]
- Line 7: Duplicate range [5037-5038]
- Line 13: Duplicate range [5042-5048]
- Line 25: Duplicate range [5063-5069]
- Line 31: Duplicate range [5076-5084]

---

### File: dynamic/commentary_BACKUP/02-18-09-01.txt

**Errors:**
- Line 3: Duplicate range [5085-5088]
- Line 7: Duplicate range [5088-5090]
- Line 11: Duplicate range [5091-5100]
- Line 15: Duplicate range [5101-5106]
- Line 19: Duplicate range [5107-5113]
- Line 23: Duplicate range [5114-5124]

---

### File: dynamic/commentary_BACKUP/02-18-10-01.txt

**Errors:**
- Line 3: Duplicate range [5125-5137]
- Line 5: Duplicate range [5125-5137]
- Line 7: Duplicate range [5125-5137]
- Line 9: Duplicate range [5125-5137]
- Line 13: Duplicate range [5138-5151]
- Line 15: Duplicate range [5138-5151]
- Line 19: Duplicate range [5146-5156]
- Line 21: Duplicate range [5146-5156]

---

### File: dynamic/commentary_BACKUP/02-18-14-01.txt

**Errors:**
- Line 6: Duplicate range [5640-5644]
- Line 9: Duplicate range [5640-5644]
- Line 12: Duplicate range [5640-5644]
- Line 15: Duplicate range [5640-5644]

---

### File: dynamic/commentary_BACKUP/02-18-16-02.txt

**Errors:**
- Line 3: Duplicate range [5923-5924]
- Line 5: Duplicate range [5923-5924]
- Line 7: Duplicate range [5923-5924]
- Line 9: Duplicate range [5923-5924]
- Line 11: Duplicate range [5923-5924]
- Line 13: Duplicate range [5923-5924]
- Line 15: Duplicate range [5923-5924]
- Line 17: Duplicate range [5923-5924]
- Line 19: Duplicate range [5923-5924]
- Line 21: Duplicate range [5923-5924]
- Line 23: Duplicate range [5923-5924]

---

### File: dynamic/commentary_BACKUP/02-18-16-03.txt

**Errors:**
- Line 3: Duplicate range [5925-5927]
- Line 5: Duplicate range [5925-5927]
- Line 7: Duplicate range [5925-5927]
- Line 9: Duplicate range [5925-5927]
- Line 11: Duplicate range [5925-5927]
- Line 13: Duplicate range [5925-5927]
- Line 15: Duplicate range [5925-5927]
- Line 17: Duplicate range [5925-5927]
- Line 19: Duplicate range [5925-5927]
- Line 21: Duplicate range [5925-5927]
- Line 23: Duplicate range [5925-5927]
- Line 25: Duplicate range [5925-5927]
- Line 27: Duplicate range [5925-5927]

---

### File: dynamic/commentary_BACKUP/02-19-01-01.txt

**Errors:**
- Line 246: Non-sequential range [6826-6850] - Start (6826) < Previous start (8026)
- Line 454: Invalid range [7701-1669] - End < Start
- Line 547: Invalid range [10001-1669] - End < Start
- Line 658: Invalid range [31001-1669] - End < Start
- Line 702: Non-sequential range [8101-8200] - Start (8101) < Previous start (42001)
- Line 702: Duplicate range [8101-8200]
- Line 711: Duplicate range [8201-8300]
- Line 724: Duplicate range [8301-8400]
- Line 729: Duplicate range [8401-8500]
- Line 740: Duplicate range [8501-8600]
- Line 757: Duplicate range [8601-8700]
- Line 762: Duplicate range [8701-8800]
- Line 769: Duplicate range [8801-8900]
- Line 780: Duplicate range [8901-9000]
- Line 785: Duplicate range [9001-9100]
- Line 790: Duplicate range [9101-9200]
- Line 799: Duplicate range [9201-9300]
- Line 806: Duplicate range [9301-9400]
- Line 827: Duplicate range [9401-9500]
- Line 832: Duplicate range [9501-9600]
- Line 843: Duplicate range [9601-9700]
- Line 848: Duplicate range [9701-9800]
- Line 865: Duplicate range [9801-9900]
- Line 870: Duplicate range [9901-10000]

---

### File: dynamic/commentary_BACKUP/02-20-01-01.txt

**Errors:**
- Line 6: Duplicate range [8083-8091]
- Line 23: Duplicate range [8092-8101]
- Line 38: Duplicate range [8102-8109]
- Line 52: Duplicate range [8110-8116]
- Line 66: Duplicate range [8117-8124]
- Line 83: Duplicate range [8125-8132]
- Line 100: Duplicate range [8133-8142]
- Line 115: Duplicate range [8143-8163]
- Line 132: Duplicate range [8164-8173]
- Line 147: Duplicate range [8174-8194]
- Line 160: Duplicate range [8195-8199]
- Line 173: Duplicate range [8200-8207]
- Line 188: Duplicate range [8208-8223]
- Line 202: Duplicate range [8224-8250]
- Line 218: Duplicate range [8251-8266]
- Line 232: Duplicate range [8267-8302]
- Line 249: Duplicate range [8303-8318]
- Line 263: Duplicate range [8319-8342]
- Line 280: Duplicate range [8343-8374]
- Line 306: Duplicate range [8375-8405]
- Line 324: Duplicate range [8406-8437]
- Line 341: Duplicate range [8438-8456]
- Line 359: Duplicate range [8457-8478]
- Line 376: Duplicate range [8479-8490]
- Line 390: Duplicate range [8491-8524]
- Line 406: Duplicate range [8525-8561]
- Line 423: Duplicate range [8562-8585]
- Line 437: Duplicate range [8586-8625]
- Line 454: Duplicate range [8626-8631]
- Line 469: Duplicate range [8632-8658]
- Line 485: Duplicate range [8659-8670]
- Line 501: Duplicate range [8671-8678]
- Line 514: Duplicate range [8679-8695]
- Line 528: Duplicate range [8696-8718]
- Line 542: Duplicate range [8719-8728]
- Line 558: Duplicate range [8729-8752]
- Line 573: Duplicate range [8753-8804]
- Line 589: Duplicate range [8805-8825]
- Line 603: Duplicate range [8826-8830]

---

### File: dynamic/commentary_BACKUP/02-20-03-01.txt

**Errors:**
- Line 6: Duplicate range [8970-8971]
- Line 11: Duplicate range [8970-8971]
- Line 15: Duplicate range [8970-8971]
- Line 19: Duplicate range [8970-8971]
- Line 22: Duplicate range [8970-8971]

---

### File: dynamic/commentary_BACKUP/02-20-04-01.txt

**Errors:**
- Line 3: Duplicate range [8972-9006]
- Line 5: Duplicate range [8972-9006]
- Line 7: Duplicate range [8972-9006]
- Line 9: Duplicate range [8972-9006]
- Line 13: Duplicate range [8984-8999]
- Line 15: Duplicate range [8984-8999]
- Line 19: Duplicate range [9000-9006]
- Line 21: Duplicate range [9000-9006]
- Line 25: Duplicate range [9007-9023]
- Line 27: Duplicate range [9007-9023]
- Line 29: Duplicate range [9007-9023]
- Line 33: Duplicate range [9024-9026]

---

### File: dynamic/commentary_BACKUP/02-20-05-01.txt

**Errors:**
- Line 3: Duplicate range [9027-9042]
- Line 5: Duplicate range [9027-9042]
- Line 7: Duplicate range [9027-9042]
- Line 9: Duplicate range [9027-9042]
- Line 11: Duplicate range [9027-9042]
- Line 15: Duplicate range [9043-9068]
- Line 17: Duplicate range [9043-9068]
- Line 19: Duplicate range [9043-9068]
- Line 21: Duplicate range [9043-9068]
- Line 23: Duplicate range [9043-9068]

---

### File: dynamic/commentary_BACKUP/02-20-06-01.txt

**Errors:**
- Line 6: Duplicate range [9069-9078]
- Line 12: Duplicate range [9069-9078]
- Line 18: Duplicate range [9069-9078]
- Line 21: Duplicate range [9069-9078]
- Line 27: Duplicate range [9069-9078]
- Line 33: Duplicate range [9069-9078]
- Line 40: Duplicate range [9069-9078]

---

### File: dynamic/commentary_BACKUP/02-20-07-01.txt

**Errors:**
- Line 3: Duplicate range [9024-9040]
- Line 5: Duplicate range [9024-9040]
- Line 9: Duplicate range [9041-9050]
- Line 13: Duplicate range [9051-9060]
- Line 17: Duplicate range [9061-9070]
- Line 21: Duplicate range [9071-9080]
- Line 25: Duplicate range [9081-9090]
- Line 29: Duplicate range [9091-9100]
- Line 33: Duplicate range [9101-9110]
- Line 37: Duplicate range [9111-9120]
- Line 41: Duplicate range [9121-9130]
- Line 45: Duplicate range [9131-9140]
- Line 49: Duplicate range [9141-9150]
- Line 53: Duplicate range [9151-9160]
- Line 57: Duplicate range [9161-9170]
- Line 61: Duplicate range [9171-9180]
- Line 65: Duplicate range [9181-9190]

---

### File: dynamic/commentary_BACKUP/02-20-08-01.txt

**Errors:**
- Line 30: Duplicate range [9342-9371]

---

### File: dynamic/commentary_BACKUP/02-20-09-01.txt

**Errors:**
- Line 4: Duplicate range [9404-9412]

---

### File: dynamic/commentary_BACKUP/02-22-02-01.txt

**Errors:**
- Line 3: Duplicate range [10766-10771]
- Line 7: Duplicate range [10772-10776]
- Line 11: Duplicate range [10777-10782]
- Line 15: Duplicate range [10783-10789]
- Line 19: Duplicate range [10790-10809]
- Line 23: Duplicate range [10811-10825]
- Line 25: Duplicate range [10811-10825]

---

### File: dynamic/commentary_BACKUP/02-22-03-02.txt

**Errors:**
- Line 4: Duplicate range [10900-10908]

---

### File: dynamic/commentary_BACKUP/02-22-03-03.txt

**Errors:**
- Line 57: Non-sequential range [11182-11300] - Start (11182) < Previous start (11291)
- Line 3: Duplicate range [11182-11190]
- Line 5: Duplicate range [11182-11190]
- Line 9: Duplicate range [11191-11200]
- Line 13: Duplicate range [11201-11210]
- Line 17: Duplicate range [11211-11220]
- Line 21: Duplicate range [11221-11230]
- Line 25: Duplicate range [11231-11240]
- Line 29: Duplicate range [11241-11250]
- Line 33: Duplicate range [11251-11260]
- Line 37: Duplicate range [11261-11270]
- Line 41: Duplicate range [11271-11280]
- Line 45: Duplicate range [11281-11290]
- Line 49: Duplicate range [11291-11300]
- Line 59: Duplicate range [11182-11300]
- Line 61: Duplicate range [11182-11300]
- Line 63: Duplicate range [11182-11300]
- Line 65: Duplicate range [11182-11300]
- Line 67: Duplicate range [11182-11300]
- Line 69: Duplicate range [11182-11300]

---

### File: dynamic/commentary_BACKUP/02-22-04-01.txt

**Errors:**
- Line 81: Non-sequential range [11551-11600] - Start (11551) < Previous start (11681)

---

### File: dynamic/commentary_BACKUP/02-23-02-01.txt

**Errors:**
- Line 62: Non-sequential range [12245-12255] - Start (12245) < Previous start (12341)
- Line 90: Non-sequential range [12245-12350] - Start (12245) < Previous start (12311)
- Line 62: Duplicate range [12245-12255]
- Line 64: Duplicate range [12245-12255]
- Line 66: Duplicate range [12245-12255]
- Line 68: Duplicate range [12245-12255]
- Line 70: Duplicate range [12245-12255]
- Line 72: Duplicate range [12256-12280]
- Line 74: Duplicate range [12256-12280]
- Line 76: Duplicate range [12256-12280]
- Line 78: Duplicate range [12256-12280]
- Line 82: Duplicate range [12281-12310]
- Line 86: Duplicate range [12311-12350]
- Line 88: Duplicate range [12311-12350]
- Line 92: Duplicate range [12245-12350]
- Line 94: Duplicate range [12245-12350]
- Line 96: Duplicate range [12245-12350]
- Line 98: Duplicate range [12245-12350]
- Line 100: Duplicate range [12245-12350]
- Line 102: Duplicate range [12245-12350]
- Line 104: Duplicate range [12245-12350]
- Line 106: Duplicate range [12245-12350]
- Line 108: Duplicate range [12245-12350]
- Line 110: Duplicate range [12245-12350]
- Line 112: Duplicate range [12245-12350]
- Line 114: Duplicate range [12245-12350]
- Line 116: Duplicate range [12245-12350]
- Line 118: Duplicate range [12245-12350]
- Line 120: Duplicate range [12245-12350]
- Line 122: Duplicate range [12245-12350]
- Line 124: Duplicate range [12245-12350]

---

### File: dynamic/commentary_BACKUP/02-23-03-02.txt

**Errors:**
- Line 236: Non-sequential range [11741-11800] - Start (11741) < Previous start (13861)

---

### File: dynamic/commentary_BACKUP/02-23-04-01.txt

**Errors:**
- Line 145: Non-sequential range [13304-13694] - Start (13304) < Previous start (13690)
- Line 3: Duplicate range [13304-13320]
- Line 5: Duplicate range [13304-13320]
- Line 7: Duplicate range [13304-13320]
- Line 11: Duplicate range [13321-13340]
- Line 13: Duplicate range [13321-13340]
- Line 15: Duplicate range [13321-13340]
- Line 19: Duplicate range [13341-13360]
- Line 21: Duplicate range [13341-13360]
- Line 23: Duplicate range [13341-13360]
- Line 27: Duplicate range [13361-13380]
- Line 29: Duplicate range [13361-13380]
- Line 31: Duplicate range [13361-13380]
- Line 35: Duplicate range [13381-13400]
- Line 37: Duplicate range [13381-13400]
- Line 39: Duplicate range [13381-13400]
- Line 43: Duplicate range [13401-13420]
- Line 45: Duplicate range [13401-13420]
- Line 47: Duplicate range [13401-13420]
- Line 51: Duplicate range [13421-13450]
- Line 53: Duplicate range [13421-13450]
- Line 55: Duplicate range [13421-13450]
- Line 59: Duplicate range [13451-13480]
- Line 61: Duplicate range [13451-13480]
- Line 63: Duplicate range [13451-13480]
- Line 67: Duplicate range [13481-13500]
- Line 69: Duplicate range [13481-13500]
- Line 71: Duplicate range [13481-13500]
- Line 75: Duplicate range [13501-13520]
- Line 77: Duplicate range [13501-13520]
- Line 79: Duplicate range [13501-13520]
- Line 83: Duplicate range [13521-13540]
- Line 85: Duplicate range [13521-13540]
- Line 87: Duplicate range [13521-13540]
- Line 91: Duplicate range [13541-13560]
- Line 93: Duplicate range [13541-13560]
- Line 95: Duplicate range [13541-13560]
- Line 99: Duplicate range [13561-13580]
- Line 101: Duplicate range [13561-13580]
- Line 103: Duplicate range [13561-13580]
- Line 107: Duplicate range [13581-13600]
- Line 109: Duplicate range [13581-13600]
- Line 111: Duplicate range [13581-13600]
- Line 115: Duplicate range [13601-13630]
- Line 117: Duplicate range [13601-13630]
- Line 119: Duplicate range [13601-13630]
- Line 123: Duplicate range [13631-13660]
- Line 125: Duplicate range [13631-13660]
- Line 127: Duplicate range [13631-13660]
- Line 131: Duplicate range [13661-13689]
- Line 133: Duplicate range [13661-13689]
- Line 135: Duplicate range [13661-13689]
- Line 139: Duplicate range [13690-13694]
- Line 141: Duplicate range [13690-13694]
- Line 143: Duplicate range [13690-13694]
- Line 147: Duplicate range [13304-13694]
- Line 149: Duplicate range [13304-13694]
- Line 151: Duplicate range [13304-13694]
- Line 153: Duplicate range [13304-13694]
- Line 155: Duplicate range [13304-13694]
- Line 157: Duplicate range [13304-13694]
- Line 159: Duplicate range [13304-13694]
- Line 161: Duplicate range [13304-13694]
- Line 163: Duplicate range [13304-13694]
- Line 165: Duplicate range [13304-13694]
- Line 167: Duplicate range [13304-13694]
- Line 169: Duplicate range [13304-13694]
- Line 171: Duplicate range [13304-13694]
- Line 173: Duplicate range [13304-13694]
- Line 175: Duplicate range [13304-13694]
- Line 177: Duplicate range [13304-13694]
- Line 179: Duplicate range [13304-13694]
- Line 181: Duplicate range [13304-13694]
- Line 183: Duplicate range [13304-13694]
- Line 185: Duplicate range [13304-13694]
- Line 187: Duplicate range [13304-13694]
- Line 189: Duplicate range [13304-13694]
- Line 191: Duplicate range [13304-13694]
- Line 193: Duplicate range [13304-13694]
- Line 195: Duplicate range [13304-13694]
- Line 197: Duplicate range [13304-13694]
- Line 199: Duplicate range [13304-13694]
- Line 201: Duplicate range [13304-13694]
- Line 203: Duplicate range [13304-13694]
- Line 205: Duplicate range [13304-13694]
- Line 207: Duplicate range [13304-13694]
- Line 209: Duplicate range [13304-13694]
- Line 211: Duplicate range [13304-13694]
- Line 213: Duplicate range [13304-13694]
- Line 215: Duplicate range [13304-13694]
- Line 217: Duplicate range [13304-13694]
- Line 219: Duplicate range [13304-13694]
- Line 221: Duplicate range [13304-13694]
- Line 223: Duplicate range [13304-13694]
- Line 225: Duplicate range [13304-13694]
- Line 227: Duplicate range [13304-13694]
- Line 229: Duplicate range [13304-13694]
- Line 231: Duplicate range [13304-13694]
- Line 233: Duplicate range [13304-13694]
- Line 235: Duplicate range [13304-13694]
- Line 237: Duplicate range [13304-13694]
- Line 239: Duplicate range [13304-13694]
- Line 241: Duplicate range [13304-13694]
- Line 243: Duplicate range [13304-13694]
- Line 245: Duplicate range [13304-13694]
- Line 247: Duplicate range [13304-13694]
- Line 249: Duplicate range [13304-13694]
- Line 251: Duplicate range [13304-13694]
- Line 253: Duplicate range [13304-13694]
- Line 254: Duplicate range [13481-13500]
- Line 256: Duplicate range [13481-13500]
- Line 260: Duplicate range [13501-13550]
- Line 262: Duplicate range [13501-13550]
- Line 264: Duplicate range [13501-13550]
- Line 268: Duplicate range [13551-13600]
- Line 270: Duplicate range [13551-13600]
- Line 272: Duplicate range [13551-13600]
- Line 276: Duplicate range [13601-13650]
- Line 278: Duplicate range [13601-13650]
- Line 282: Duplicate range [13651-13700]
- Line 284: Duplicate range [13651-13700]

---

### File: dynamic/commentary_BACKUP/02-23-05-01.txt

**Errors:**
- Line 6: Duplicate range [13695-13700]

---

### File: dynamic/commentary_BACKUP/02-23-06-01.txt

**Errors:**
- Line 810: Non-sequential range [13701-14200] - Start (13701) < Previous start (14199)
- Line 278: Duplicate range [13911-13940]
- Line 805: Duplicate range [14199-14199]
- Line 812: Duplicate range [13701-14200]
- Line 814: Duplicate range [13701-14200]
- Line 816: Duplicate range [13701-14200]
- Line 818: Duplicate range [13701-14200]
- Line 820: Duplicate range [13701-14200]
- Line 822: Duplicate range [13701-14200]
- Line 824: Duplicate range [13701-14200]
- Line 826: Duplicate range [13701-14200]
- Line 828: Duplicate range [13701-14200]
- Line 830: Duplicate range [13701-14200]
- Line 832: Duplicate range [13701-14200]

---

### File: dynamic/commentary_BACKUP/02-23-07-01.txt

**Errors:**
- Line 196: Non-sequential range [14334-14370] - Start (14334) < Previous start (14366)
- Line 357: Non-sequential range [14404-14459] - Start (14404) < Previous start (14457)
- Line 11: Duplicate range [14278-14280]

---

### File: dynamic/commentary_BACKUP/02-23-08-01.txt

**Errors:**
- Line 6: Duplicate range [14588-14588]
- Line 11: Duplicate range [14588-14588]
- Line 15: Duplicate range [14588-14588]

---

### File: dynamic/commentary_BACKUP/02-23-08-02.txt

**Errors:**
- Line 3: Duplicate range [14589-14589]

---

### File: dynamic/commentary_BACKUP/02-23-08-03.txt

**Errors:**
- Line 46: Non-sequential range [14590-14651] - Start (14590) < Previous start (14638)
- Line 10: Duplicate range [14598-14609]
- Line 49: Duplicate range [14590-14651]
- Line 52: Duplicate range [14590-14651]
- Line 55: Duplicate range [14590-14651]
- Line 58: Duplicate range [14590-14651]

---

### File: dynamic/commentary_BACKUP/02-23-08-04.txt

**Errors:**
- Line 6: Duplicate range [14640-14641]
- Line 11: Duplicate range [14640-14641]
- Line 15: Duplicate range [14640-14641]

---

### File: dynamic/commentary_BACKUP/02-23-08-06.txt

**Errors:**
- Line 6: Duplicate range [14750-14750]
- Line 11: Duplicate range [14750-14750]
- Line 15: Duplicate range [14750-14750]

---

### File: dynamic/commentary_BACKUP/02-23-08-07.txt

**Errors:**
- Line 6: Duplicate range [14751-14751]
- Line 11: Duplicate range [14751-14751]
- Line 14: Duplicate range [14751-14751]

---

### File: dynamic/commentary_BACKUP/02-23-08-08.txt

**Errors:**
- Line 8: Duplicate range [14752-14752]

---

### File: dynamic/commentary_BACKUP/02-23-08-09.txt

**Errors:**
- Line 3: Duplicate range [14761-14770]
- Line 5: Duplicate range [14761-14770]
- Line 9: Duplicate range [14771-14780]
- Line 13: Duplicate range [14781-14790]
- Line 17: Duplicate range [14791-14800]
- Line 21: Duplicate range [14801-14810]
- Line 25: Duplicate range [14811-14820]
- Line 29: Duplicate range [14821-14830]
- Line 33: Duplicate range [14831-14840]
- Line 37: Duplicate range [14841-14850]
- Line 41: Duplicate range [14851-14860]
- Line 45: Duplicate range [14861-14870]

---

### File: dynamic/commentary_BACKUP/02-23-09-01.txt

**Errors:**
- Line 287: Non-sequential range [15079-15087] - Start (15079) < Previous start (15085)

---

### File: dynamic/delusion/01-02-02-02.txt

**Errors:**
- Line 248: Duplicate range [1532-1538]

---

### File: dynamic/delusion/01-04-03-01.txt

**Errors:**
- Line 33: Duplicate range [2833-2833]
- Line 49: Duplicate range [2833-2833]
- Line 65: Duplicate range [2833-2833]
- Line 81: Duplicate range [2833-2833]

---

### File: dynamic/delusion/01-04-08-01.txt

**Errors:**
- Line 58: Duplicate range [3002-3008]

---

### File: dynamic/delusion/01-04-10-01.txt

**Errors:**
- Line 17: Duplicate range [3037-3039]
- Line 33: Duplicate range [3037-3039]

---

### File: dynamic/delusion/01-05-04-04.txt

**Errors:**
- Line 1: Duplicate range [6422-6422]

---

### File: dynamic/delusion/01-06-01-01.txt

**Errors:**
- Line 18: Non-sequential range [6801-6801] - Start (6801) < Previous start (6808)
- Line 35: Non-sequential range [6801-6801] - Start (6801) < Previous start (6815)
- Line 52: Non-sequential range [6801-6801] - Start (6801) < Previous start (6823)
- Line 69: Non-sequential range [6801-6801] - Start (6801) < Previous start (6830)
- Line 120: Non-sequential range [6801-6801] - Start (6801) < Previous start (6838)
- Line 137: Non-sequential range [6801-6801] - Start (6801) < Previous start (6845)
- Line 154: Non-sequential range [6801-6801] - Start (6801) < Previous start (6852)
- Line 171: Non-sequential range [6801-6801] - Start (6801) < Previous start (6859)
- Line 188: Non-sequential range [6801-6801] - Start (6801) < Previous start (6866)
- Line 205: Non-sequential range [6801-6801] - Start (6801) < Previous start (6873)
- Line 256: Non-sequential range [6801-6801] - Start (6801) < Previous start (6880)
- Line 273: Non-sequential range [6801-6801] - Start (6801) < Previous start (6886)
- Line 290: Non-sequential range [6801-6801] - Start (6801) < Previous start (6893)
- Line 307: Non-sequential range [6801-6801] - Start (6801) < Previous start (6899)
- Line 324: Non-sequential range [6801-6801] - Start (6801) < Previous start (6906)
- Line 341: Non-sequential range [6801-6801] - Start (6801) < Previous start (6912)
- Line 392: Non-sequential range [6801-6801] - Start (6801) < Previous start (6919)
- Line 409: Non-sequential range [6801-6801] - Start (6801) < Previous start (6925)
- Line 426: Non-sequential range [6801-6801] - Start (6801) < Previous start (6931)
- Line 443: Non-sequential range [6801-6801] - Start (6801) < Previous start (6938)
- Line 460: Non-sequential range [6801-6801] - Start (6801) < Previous start (6944)
- Line 477: Non-sequential range [6801-6801] - Start (6801) < Previous start (6950)
- Line 528: Non-sequential range [6801-6801] - Start (6801) < Previous start (6957)
- Line 545: Non-sequential range [6801-6801] - Start (6801) < Previous start (6963)
- Line 562: Non-sequential range [6801-6801] - Start (6801) < Previous start (6970)
- Line 579: Non-sequential range [6801-6801] - Start (6801) < Previous start (6976)
- Line 596: Non-sequential range [6801-6801] - Start (6801) < Previous start (6983)
- Line 613: Non-sequential range [6801-6801] - Start (6801) < Previous start (6989)
- Line 664: Non-sequential range [6801-6801] - Start (6801) < Previous start (6996)
- Line 681: Non-sequential range [6801-6801] - Start (6801) < Previous start (7003)
- Line 698: Non-sequential range [6801-6801] - Start (6801) < Previous start (7010)
- Line 715: Non-sequential range [6801-6801] - Start (6801) < Previous start (7017)
- Line 732: Non-sequential range [6801-6801] - Start (6801) < Previous start (7024)
- Line 749: Non-sequential range [6801-6801] - Start (6801) < Previous start (7031)
- Line 800: Non-sequential range [6801-6801] - Start (6801) < Previous start (7038)
- Line 817: Non-sequential range [6801-6801] - Start (6801) < Previous start (7045)
- Line 834: Non-sequential range [6801-6801] - Start (6801) < Previous start (7053)
- Line 851: Non-sequential range [6801-6801] - Start (6801) < Previous start (7061)
- Line 868: Non-sequential range [6801-6801] - Start (6801) < Previous start (7069)
- Line 885: Non-sequential range [6801-6801] - Start (6801) < Previous start (7077)
- Line 936: Non-sequential range [6801-6801] - Start (6801) < Previous start (7085)
- Line 953: Non-sequential range [6801-6801] - Start (6801) < Previous start (7096)
- Line 18: Duplicate range [6801-6801]
- Line 35: Duplicate range [6801-6801]
- Line 52: Duplicate range [6801-6801]
- Line 69: Duplicate range [6801-6801]
- Line 120: Duplicate range [6801-6801]
- Line 137: Duplicate range [6801-6801]
- Line 154: Duplicate range [6801-6801]
- Line 171: Duplicate range [6801-6801]
- Line 188: Duplicate range [6801-6801]
- Line 205: Duplicate range [6801-6801]
- Line 256: Duplicate range [6801-6801]
- Line 273: Duplicate range [6801-6801]
- Line 290: Duplicate range [6801-6801]
- Line 307: Duplicate range [6801-6801]
- Line 324: Duplicate range [6801-6801]
- Line 341: Duplicate range [6801-6801]
- Line 392: Duplicate range [6801-6801]
- Line 409: Duplicate range [6801-6801]
- Line 426: Duplicate range [6801-6801]
- Line 443: Duplicate range [6801-6801]
- Line 460: Duplicate range [6801-6801]
- Line 477: Duplicate range [6801-6801]
- Line 528: Duplicate range [6801-6801]
- Line 545: Duplicate range [6801-6801]
- Line 562: Duplicate range [6801-6801]
- Line 579: Duplicate range [6801-6801]
- Line 596: Duplicate range [6801-6801]
- Line 613: Duplicate range [6801-6801]
- Line 664: Duplicate range [6801-6801]
- Line 681: Duplicate range [6801-6801]
- Line 698: Duplicate range [6801-6801]
- Line 715: Duplicate range [6801-6801]
- Line 732: Duplicate range [6801-6801]
- Line 749: Duplicate range [6801-6801]
- Line 800: Duplicate range [6801-6801]
- Line 817: Duplicate range [6801-6801]
- Line 834: Duplicate range [6801-6801]
- Line 851: Duplicate range [6801-6801]
- Line 868: Duplicate range [6801-6801]
- Line 885: Duplicate range [6801-6801]
- Line 936: Duplicate range [6801-6801]
- Line 953: Duplicate range [6801-6801]

---

### File: dynamic/delusion/01-06-04-01.txt

**Errors:**
- Line 23: Duplicate range [8138-8142]
- Line 67: Duplicate range [8143-8152]
- Line 111: Duplicate range [8153-8171]
- Line 133: Duplicate range [8153-8171]
- Line 155: Duplicate range [8153-8171]
- Line 177: Duplicate range [8153-8171]
- Line 199: Duplicate range [8153-8171]
- Line 243: Duplicate range [8172-8190]
- Line 265: Duplicate range [8172-8190]
- Line 309: Duplicate range [8191-8218]
- Line 375: Duplicate range [8232-8253]
- Line 419: Duplicate range [8254-8273]
- Line 463: Duplicate range [8274-8287]
- Line 485: Duplicate range [8274-8287]
- Line 507: Duplicate range [8274-8287]

---

### File: dynamic/delusion/01-06-13-01.txt

**Errors:**
- Line 232: Non-sequential range [9526-9528] - Start (9526) < Previous start (9575)
- Line 319: Non-sequential range [9537-9542] - Start (9537) < Previous start (9566)
- Line 440: Non-sequential range [9584-9604] - Start (9584) < Previous start (9591)
- Line 457: Non-sequential range [9575-9582] - Start (9575) < Previous start (9584)
- Line 491: Non-sequential range [9584-9604] - Start (9584) < Previous start (9597)
- Line 542: Non-sequential range [9614-9670] - Start (9614) < Previous start (9617)
- Line 457: Duplicate range [9575-9582]
- Line 491: Duplicate range [9584-9604]

---

### File: dynamic/delusion/01-09-01-01.txt

**Errors:**
- Line 1582: Non-sequential range [11682-11686] - Start (11682) < Previous start (12142)
- Line 1602: Non-sequential range [11687-11693] - Start (11687) < Previous start (12148)
- Line 1622: Non-sequential range [11694-11698] - Start (11694) < Previous start (12155)
- Line 1642: Non-sequential range [11699-11710] - Start (11699) < Previous start (12161)
- Line 1662: Non-sequential range [11711-11728] - Start (11711) < Previous start (12168)
- Line 1682: Non-sequential range [11729-11742] - Start (11729) < Previous start (12177)
- Line 1702: Non-sequential range [11743-11758] - Start (11743) < Previous start (12186)
- Line 1722: Non-sequential range [11759-11781] - Start (11759) < Previous start (12195)
- Line 1742: Non-sequential range [11782-11788] - Start (11782) < Previous start (12205)
- Line 1762: Non-sequential range [11789-11802] - Start (11789) < Previous start (12216)
- Line 1782: Non-sequential range [11803-11818] - Start (11803) < Previous start (12228)
- Line 1802: Non-sequential range [11819-11838] - Start (11819) < Previous start (12239)
- Line 1822: Non-sequential range [11854-11873] - Start (11854) < Previous start (12251)
- Line 1842: Non-sequential range [11874-11895] - Start (11874) < Previous start (12259)
- Line 1862: Non-sequential range [11896-11910] - Start (11896) < Previous start (12267)
- Line 1882: Non-sequential range [11911-11932] - Start (11911) < Previous start (12275)
- Line 1902: Non-sequential range [11933-11947] - Start (11933) < Previous start (12284)
- Line 1922: Non-sequential range [11948-11974] - Start (11948) < Previous start (12289)
- Line 1942: Non-sequential range [11975-11994] - Start (11975) < Previous start (12295)
- Line 1962: Non-sequential range [11995-12000] - Start (11995) < Previous start (12301)
- Line 1982: Non-sequential range [12001-12018] - Start (12001) < Previous start (12307)
- Line 2002: Non-sequential range [12019-12040] - Start (12019) < Previous start (12316)
- Line 2022: Non-sequential range [12041-12053] - Start (12041) < Previous start (12326)
- Line 2042: Non-sequential range [12054-12067] - Start (12054) < Previous start (12335)
- Line 2062: Non-sequential range [12068-12086] - Start (12068) < Previous start (12345)
- Line 2082: Non-sequential range [12087-12105] - Start (12087) < Previous start (12356)
- Line 2102: Non-sequential range [12106-12117] - Start (12106) < Previous start (12368)
- Line 2122: Non-sequential range [12118-12137] - Start (12118) < Previous start (12380)
- Line 2142: Non-sequential range [12138-12153] - Start (12138) < Previous start (12392)
- Line 2162: Non-sequential range [12154-12166] - Start (12154) < Previous start (12402)
- Line 2182: Non-sequential range [12167-12191] - Start (12167) < Previous start (12413)
- Line 2202: Non-sequential range [12192-12208] - Start (12192) < Previous start (12424)
- Line 2222: Non-sequential range [12209-12226] - Start (12209) < Previous start (12435)
- Line 2242: Non-sequential range [12227-12244] - Start (12227) < Previous start (12446)
- Line 2262: Non-sequential range [12245-12267] - Start (12245) < Previous start (12458)
- Line 2282: Non-sequential range [12268-12287] - Start (12268) < Previous start (12470)

---

### File: dynamic/delusion/01-10-01-01.txt

**Errors:**
- Line 21: Non-sequential range [12500-12500] - Start (12500) < Previous start (12511)
- Line 41: Non-sequential range [12500-12500] - Start (12500) < Previous start (12526)
- Line 61: Non-sequential range [12500-12500] - Start (12500) < Previous start (12541)
- Line 81: Non-sequential range [12500-12500] - Start (12500) < Previous start (12557)
- Line 101: Non-sequential range [12500-12500] - Start (12500) < Previous start (12573)
- Line 121: Non-sequential range [12500-12500] - Start (12500) < Previous start (12589)
- Line 141: Non-sequential range [12500-12500] - Start (12500) < Previous start (12606)
- Line 161: Non-sequential range [12500-12500] - Start (12500) < Previous start (12616)
- Line 181: Non-sequential range [12500-12500] - Start (12500) < Previous start (12626)
- Line 221: Non-sequential range [12500-12500] - Start (12500) < Previous start (12647)
- Line 241: Non-sequential range [12500-12500] - Start (12500) < Previous start (12658)
- Line 261: Non-sequential range [12500-12500] - Start (12500) < Previous start (12669)
- Line 281: Non-sequential range [12500-12500] - Start (12500) < Previous start (12680)
- Line 301: Non-sequential range [12500-12500] - Start (12500) < Previous start (12691)
- Line 321: Non-sequential range [12500-12500] - Start (12500) < Previous start (12703)
- Line 341: Non-sequential range [12500-12500] - Start (12500) < Previous start (12713)
- Line 361: Non-sequential range [12500-12500] - Start (12500) < Previous start (12723)
- Line 381: Non-sequential range [12500-12500] - Start (12500) < Previous start (12733)
- Line 401: Non-sequential range [12500-12500] - Start (12500) < Previous start (12744)
- Line 421: Non-sequential range [12500-12500] - Start (12500) < Previous start (12752)
- Line 441: Non-sequential range [12500-12500] - Start (12500) < Previous start (12760)
- Line 461: Non-sequential range [12500-12500] - Start (12500) < Previous start (12768)
- Line 481: Non-sequential range [12500-12500] - Start (12500) < Previous start (12777)
- Line 501: Non-sequential range [12500-12500] - Start (12500) < Previous start (12786)
- Line 521: Non-sequential range [12500-12500] - Start (12500) < Previous start (12795)
- Line 541: Non-sequential range [12500-12500] - Start (12500) < Previous start (12804)
- Line 561: Non-sequential range [12500-12500] - Start (12500) < Previous start (12814)
- Line 581: Non-sequential range [12500-12500] - Start (12500) < Previous start (12825)
- Line 601: Non-sequential range [12500-12500] - Start (12500) < Previous start (12837)
- Line 621: Non-sequential range [12500-12500] - Start (12500) < Previous start (12849)
- Line 641: Non-sequential range [12500-12500] - Start (12500) < Previous start (12861)
- Line 661: Non-sequential range [12500-12500] - Start (12500) < Previous start (12870)
- Line 681: Non-sequential range [12500-12500] - Start (12500) < Previous start (12880)
- Line 701: Non-sequential range [12500-12500] - Start (12500) < Previous start (12890)
- Line 721: Non-sequential range [12500-12500] - Start (12500) < Previous start (12900)
- Line 741: Non-sequential range [12500-12500] - Start (12500) < Previous start (12906)
- Line 761: Non-sequential range [12500-12510] - Start (12500) < Previous start (12912)
- Line 781: Non-sequential range [12500-12500] - Start (12500) < Previous start (12918)
- Line 821: Non-sequential range [12500-12500] - Start (12500) < Previous start (12933)
- Line 841: Non-sequential range [12500-12510] - Start (12500) < Previous start (12942)
- Line 861: Non-sequential range [12511-12520] - Start (12511) < Previous start (12951)
- Line 881: Non-sequential range [12500-12500] - Start (12500) < Previous start (12960)
- Line 21: Duplicate range [12500-12500]
- Line 41: Duplicate range [12500-12500]
- Line 61: Duplicate range [12500-12500]
- Line 81: Duplicate range [12500-12500]
- Line 101: Duplicate range [12500-12500]
- Line 121: Duplicate range [12500-12500]
- Line 141: Duplicate range [12500-12500]
- Line 161: Duplicate range [12500-12500]
- Line 181: Duplicate range [12500-12500]
- Line 221: Duplicate range [12500-12500]
- Line 241: Duplicate range [12500-12500]
- Line 261: Duplicate range [12500-12500]
- Line 281: Duplicate range [12500-12500]
- Line 301: Duplicate range [12500-12500]
- Line 321: Duplicate range [12500-12500]
- Line 341: Duplicate range [12500-12500]
- Line 361: Duplicate range [12500-12500]
- Line 381: Duplicate range [12500-12500]
- Line 401: Duplicate range [12500-12500]
- Line 421: Duplicate range [12500-12500]
- Line 441: Duplicate range [12500-12500]
- Line 461: Duplicate range [12500-12500]
- Line 481: Duplicate range [12500-12500]
- Line 501: Duplicate range [12500-12500]
- Line 521: Duplicate range [12500-12500]
- Line 541: Duplicate range [12500-12500]
- Line 561: Duplicate range [12500-12500]
- Line 581: Duplicate range [12500-12500]
- Line 601: Duplicate range [12500-12500]
- Line 621: Duplicate range [12500-12500]
- Line 641: Duplicate range [12500-12500]
- Line 661: Duplicate range [12500-12500]
- Line 681: Duplicate range [12500-12500]
- Line 701: Duplicate range [12500-12500]
- Line 721: Duplicate range [12500-12500]
- Line 741: Duplicate range [12500-12500]
- Line 761: Duplicate range [12500-12510]
- Line 781: Duplicate range [12500-12500]
- Line 821: Duplicate range [12500-12500]
- Line 841: Duplicate range [12500-12510]
- Line 881: Duplicate range [12500-12500]

---

### File: dynamic/delusion/01-13-05-01.txt

**Errors:**
- Line 23: Duplicate range [16866-16930]
- Line 45: Duplicate range [16866-16930]
- Line 67: Duplicate range [16866-16930]
- Line 89: Duplicate range [16866-16930]
- Line 111: Duplicate range [16866-16930]
- Line 133: Duplicate range [16866-16930]
- Line 155: Duplicate range [16866-16930]
- Line 177: Duplicate range [16866-16930]
- Line 199: Duplicate range [16866-16930]

---

### File: dynamic/delusion/01-13-06-01.txt

**Errors:**
- Line 23: Duplicate range [17072-17200]
- Line 45: Duplicate range [17072-17200]
- Line 67: Duplicate range [17072-17200]
- Line 89: Duplicate range [17072-17200]
- Line 111: Duplicate range [17072-17200]
- Line 133: Duplicate range [17072-17200]
- Line 155: Duplicate range [17072-17200]
- Line 177: Duplicate range [17072-17200]
- Line 199: Duplicate range [17072-17200]

---

### File: dynamic/delusion/01-14-01-01.txt

**Errors:**
- Line 23: Duplicate range [17361-17440]
- Line 45: Duplicate range [17361-17440]
- Line 67: Duplicate range [17361-17440]
- Line 89: Duplicate range [17361-17440]
- Line 111: Duplicate range [17361-17440]
- Line 133: Duplicate range [17361-17440]
- Line 155: Duplicate range [17361-17440]
- Line 177: Duplicate range [17361-17440]
- Line 199: Duplicate range [17361-17440]
- Line 221: Duplicate range [17361-17440]
- Line 243: Duplicate range [17361-17440]

---

### File: dynamic/delusion/02-16-03-01.txt

**Errors:**
- Line 248: Non-sequential range [1182-1588] - Start (1182) < Previous start (1588)
- Line 20: Duplicate range [1182-1203]
- Line 267: Duplicate range [1182-1588]
- Line 286: Duplicate range [1182-1588]
- Line 305: Duplicate range [1182-1588]
- Line 324: Duplicate range [1182-1588]
- Line 343: Duplicate range [1182-1588]
- Line 362: Duplicate range [1182-1588]
- Line 381: Duplicate range [1182-1588]
- Line 400: Duplicate range [1182-1588]
- Line 419: Duplicate range [1182-1588]
- Line 438: Duplicate range [1182-1588]

---

### File: dynamic/delusion/02-17-01-01.txt

**Errors:**
- Line 23: Duplicate range [1754-1830]
- Line 45: Duplicate range [1754-1830]
- Line 67: Duplicate range [1754-1830]
- Line 89: Duplicate range [1754-1830]
- Line 111: Duplicate range [1754-1830]

---

### File: dynamic/delusion/02-17-08-01.txt

**Errors:**
- Line 81: Non-sequential range [3057-3070] - Start (3057) < Previous start (3115)

---

### File: dynamic/delusion/02-17-09-01.txt

**Errors:**
- Line 41: Non-sequential range [3148-3159] - Start (3148) < Previous start (3185)
- Line 45: Non-sequential range [3125-3145] - Start (3125) < Previous start (3148)
- Line 65: Non-sequential range [3148-3159] - Start (3148) < Previous start (3185)
- Line 77: Non-sequential range [3148-3149] - Start (3148) < Previous start (3169)
- Line 85: Non-sequential range [3128-3135] - Start (3128) < Previous start (3178)
- Line 109: Non-sequential range [3141-3142] - Start (3141) < Previous start (3144)
- Line 25: Duplicate range [3147-3148]
- Line 53: Duplicate range [3169-3177]
- Line 57: Duplicate range [3178-3184]
- Line 61: Duplicate range [3185-3197]
- Line 65: Duplicate range [3148-3159]
- Line 73: Duplicate range [3169-3177]
- Line 81: Duplicate range [3178-3184]
- Line 85: Duplicate range [3128-3135]
- Line 89: Duplicate range [3136-3145]
- Line 113: Duplicate range [3146-3147]
- Line 117: Duplicate range [3147-3148]
- Line 125: Duplicate range [3169-3177]
- Line 133: Duplicate range [3185-3197]

---

### File: dynamic/delusion/02-17-09-02.txt

**Errors:**
- Line 22: Duplicate range [3198-3202]
- Line 211: Duplicate range [3232-3240]
- Line 505: Duplicate range [3294-3298]
- Line 589: Duplicate range [3304-3306]

---

### File: dynamic/delusion/02-17-10-01.txt

**Errors:**
- Line 22: Duplicate range [3307-3308]
- Line 211: Duplicate range [3316-3317]
- Line 253: Duplicate range [3317-3318]

---

### File: dynamic/delusion/02-17-12-01.txt

**Errors:**
- Line 22: Duplicate range [3600-3607]
- Line 211: Duplicate range [3608-3623]
- Line 253: Duplicate range [3620-3623]

---

### File: dynamic/delusion/02-17-13-01.txt

**Errors:**
- Line 197: Duplicate range [3823-3841]

---

### File: dynamic/delusion/02-18-03-04.txt

**Errors:**
- Line 63: Duplicate range [4467-4467]
- Line 85: Duplicate range [4467-4467]
- Line 107: Duplicate range [4467-4467]
- Line 129: Duplicate range [4467-4467]
- Line 151: Duplicate range [4467-4467]
- Line 173: Duplicate range [4467-4467]
- Line 195: Duplicate range [4467-4467]
- Line 217: Duplicate range [4467-4467]
- Line 239: Duplicate range [4467-4467]
- Line 261: Duplicate range [4467-4467]
- Line 283: Duplicate range [4467-4467]
- Line 305: Duplicate range [4467-4467]
- Line 327: Duplicate range [4467-4467]
- Line 349: Duplicate range [4467-4467]
- Line 371: Duplicate range [4467-4467]
- Line 393: Duplicate range [4467-4467]
- Line 415: Duplicate range [4467-4467]
- Line 437: Duplicate range [4467-4467]
- Line 459: Duplicate range [4467-4467]
- Line 481: Duplicate range [4467-4467]
- Line 503: Duplicate range [4467-4467]
- Line 525: Duplicate range [4467-4467]
- Line 547: Duplicate range [4467-4467]

---

### File: dynamic/delusion/02-18-04-01.txt

**Errors:**
- Line 22: Duplicate range [4468-4492]
- Line 43: Duplicate range [4468-4492]
- Line 85: Duplicate range [4493-4522]
- Line 127: Duplicate range [4523-4546]
- Line 169: Duplicate range [4547-4558]
- Line 253: Duplicate range [4566-4600]

---

### File: dynamic/delusion/02-18-05-01.txt

**Errors:**
- Line 22: Duplicate range [4601-4625]
- Line 43: Duplicate range [4601-4625]
- Line 85: Duplicate range [4626-4638]
- Line 106: Duplicate range [4626-4638]
- Line 127: Duplicate range [4626-4638]
- Line 169: Duplicate range [4639-4695]
- Line 190: Duplicate range [4639-4695]

---

### File: dynamic/delusion/02-18-06-01.txt

**Errors:**
- Line 22: Duplicate range [4696-4704]
- Line 148: Duplicate range [4715-4717]
- Line 379: Duplicate range [4728-4731]
- Line 484: Duplicate range [4735-4736]
- Line 505: Duplicate range [4735-4736]
- Line 736: Duplicate range [4746-4746]
- Line 757: Duplicate range [4746-4746]

---

### File: dynamic/delusion/02-18-07-01.txt

**Errors:**
- Line 22: Duplicate range [4747-4751]
- Line 64: Duplicate range [4752-4767]
- Line 106: Duplicate range [4768-4788]
- Line 148: Duplicate range [4789-4801]
- Line 232: Duplicate range [4831-4844]

---

### File: dynamic/delusion/02-18-09-01.txt

**Errors:**
- Line 22: Duplicate range [5085-5091]
- Line 169: Duplicate range [5090-5091]
- Line 421: Duplicate range [5101-5103]
- Line 715: Duplicate range [5112-5114]
- Line 736: Duplicate range [5112-5114]
- Line 757: Duplicate range [5112-5114]
- Line 778: Duplicate range [5112-5114]
- Line 819: Duplicate range [5113-5114]
- Line 1144: Duplicate range [5121-5124]
- Line 1186: Duplicate range [5123-5124]

---

### File: dynamic/delusion/02-18-10-01.txt

**Errors:**
- Line 63: Duplicate range [5158-5158]
- Line 85: Duplicate range [5158-5158]
- Line 107: Duplicate range [5158-5158]
- Line 129: Duplicate range [5158-5158]
- Line 151: Duplicate range [5158-5158]
- Line 173: Duplicate range [5158-5158]
- Line 195: Duplicate range [5158-5158]
- Line 217: Duplicate range [5158-5158]
- Line 239: Duplicate range [5158-5158]
- Line 261: Duplicate range [5158-5158]
- Line 283: Duplicate range [5158-5158]
- Line 305: Duplicate range [5158-5158]
- Line 327: Duplicate range [5158-5158]
- Line 349: Duplicate range [5158-5158]
- Line 371: Duplicate range [5158-5158]
- Line 393: Duplicate range [5158-5158]
- Line 415: Duplicate range [5158-5158]
- Line 437: Duplicate range [5158-5158]
- Line 459: Duplicate range [5158-5158]
- Line 481: Duplicate range [5158-5158]
- Line 503: Duplicate range [5158-5158]
- Line 525: Duplicate range [5158-5158]
- Line 547: Duplicate range [5158-5158]

---

### File: dynamic/delusion/02-18-12-01.txt

**Errors:**
- Line 23: Duplicate range [5242-5246]
- Line 45: Duplicate range [5242-5246]
- Line 89: Duplicate range [5247-5251]
- Line 111: Duplicate range [5247-5251]
- Line 199: Duplicate range [5254-5260]
- Line 243: Duplicate range [5257-5260]
- Line 287: Duplicate range [5261-5265]
- Line 331: Duplicate range [5266-5268]

---

### File: dynamic/delusion/02-18-13-01.txt

**Errors:**
- Line 838: Duplicate range [5639-5639]
- Line 860: Duplicate range [5639-5639]
- Line 882: Duplicate range [5639-5639]
- Line 904: Duplicate range [5639-5639]
- Line 926: Duplicate range [5639-5639]
- Line 948: Duplicate range [5639-5639]
- Line 970: Duplicate range [5639-5639]
- Line 992: Duplicate range [5639-5639]
- Line 1014: Duplicate range [5639-5639]
- Line 1036: Duplicate range [5639-5639]
- Line 1058: Duplicate range [5639-5639]
- Line 1080: Duplicate range [5639-5639]
- Line 1102: Duplicate range [5639-5639]
- Line 1124: Duplicate range [5639-5639]
- Line 1146: Duplicate range [5639-5639]
- Line 1168: Duplicate range [5639-5639]

---

### File: dynamic/delusion/02-18-15-01.txt

**Errors:**
- Line 778: Duplicate range [5731-5732]
- Line 904: Duplicate range [5736-5737]

---

### File: dynamic/delusion/02-18-16-04.txt

**Errors:**
- Line 361: Non-sequential range [5941-5942] - Start (5941) < Previous start (5961)
- Line 341: Duplicate range [5961-5962]
- Line 361: Duplicate range [5941-5942]

---

### File: dynamic/delusion/02-19-00-01.txt

**Errors:**
- Line 511: Duplicate range [6413-6413]
- Line 533: Duplicate range [6413-6413]
- Line 555: Duplicate range [6413-6413]
- Line 577: Duplicate range [6413-6413]
- Line 599: Duplicate range [6413-6413]
- Line 621: Duplicate range [6413-6413]
- Line 643: Duplicate range [6413-6413]
- Line 665: Duplicate range [6413-6413]

---

### File: dynamic/delusion/02-20-02-01.txt

**Errors:**
- Line 185: Non-sequential range [8906-8910] - Start (8906) < Previous start (8933)
- Line 229: Non-sequential range [8920-8925] - Start (8920) < Previous start (8939)
- Line 273: Non-sequential range [8834-8848] - Start (8834) < Previous start (8926)
- Line 361: Non-sequential range [8831-8838] - Start (8831) < Previous start (8926)
- Line 405: Non-sequential range [8834-8848] - Start (8834) < Previous start (8844)
- Line 294: Duplicate range [8911-8938]
- Line 317: Duplicate range [8920-8925]
- Line 405: Duplicate range [8834-8848]

---

### File: dynamic/delusion/02-20-04-01.txt

**Errors:**
- Line 22: Duplicate range [8972-8979]

---

### File: dynamic/delusion/02-20-05-01.txt

**Errors:**
- Line 85: Duplicate range [9068-9068]
- Line 107: Duplicate range [9068-9068]
- Line 129: Duplicate range [9068-9068]
- Line 151: Duplicate range [9068-9068]
- Line 173: Duplicate range [9068-9068]
- Line 195: Duplicate range [9068-9068]
- Line 217: Duplicate range [9068-9068]
- Line 239: Duplicate range [9068-9068]
- Line 261: Duplicate range [9068-9068]
- Line 283: Duplicate range [9068-9068]
- Line 305: Duplicate range [9068-9068]
- Line 327: Duplicate range [9068-9068]
- Line 349: Duplicate range [9068-9068]
- Line 371: Duplicate range [9068-9068]
- Line 393: Duplicate range [9068-9068]
- Line 415: Duplicate range [9068-9068]
- Line 437: Duplicate range [9068-9068]
- Line 459: Duplicate range [9068-9068]
- Line 481: Duplicate range [9068-9068]
- Line 503: Duplicate range [9068-9068]
- Line 525: Duplicate range [9068-9068]
- Line 547: Duplicate range [9068-9068]
- Line 569: Duplicate range [9068-9068]

---

### File: dynamic/delusion/02-20-07-01.txt

**Errors:**
- Line 661: Duplicate range [9140-9142]

---

### File: dynamic/delusion/02-20-08-01.txt

**Errors:**
- Line 402: Non-sequential range [9235-9248] - Start (9235) < Previous start (9385)
- Line 442: Non-sequential range [9294-9303] - Start (9294) < Previous start (9327)
- Line 462: Non-sequential range [9278-9314] - Start (9278) < Previous start (9294)
- Line 262: Duplicate range [9315-9341]
- Line 302: Duplicate range [9342-9371]
- Line 362: Duplicate range [9385-9403]
- Line 382: Duplicate range [9385-9403]
- Line 442: Duplicate range [9294-9303]

---

### File: dynamic/delusion/02-21-00-01.txt

**Errors:**
- Line 683: Duplicate range [9712-9712]
- Line 705: Duplicate range [9712-9712]
- Line 727: Duplicate range [9712-9712]
- Line 749: Duplicate range [9712-9712]
- Line 771: Duplicate range [9712-9712]
- Line 793: Duplicate range [9712-9712]
- Line 815: Duplicate range [9712-9712]
- Line 837: Duplicate range [9712-9712]
- Line 859: Duplicate range [9712-9712]
- Line 881: Duplicate range [9712-9712]
- Line 903: Duplicate range [9712-9712]
- Line 925: Duplicate range [9712-9712]
- Line 947: Duplicate range [9712-9712]
- Line 969: Duplicate range [9712-9712]
- Line 991: Duplicate range [9712-9712]
- Line 1013: Duplicate range [9712-9712]
- Line 1035: Duplicate range [9712-9712]
- Line 1057: Duplicate range [9712-9712]
- Line 1079: Duplicate range [9712-9712]
- Line 1101: Duplicate range [9712-9712]
- Line 1123: Duplicate range [9712-9712]
- Line 1145: Duplicate range [9712-9712]
- Line 1167: Duplicate range [9712-9712]
- Line 1189: Duplicate range [9712-9712]
- Line 1211: Duplicate range [9712-9712]
- Line 1233: Duplicate range [9712-9712]
- Line 1255: Duplicate range [9712-9712]
- Line 1277: Duplicate range [9712-9712]
- Line 1299: Duplicate range [9712-9712]
- Line 1321: Duplicate range [9712-9712]
- Line 1343: Duplicate range [9712-9712]
- Line 1365: Duplicate range [9712-9712]
- Line 1387: Duplicate range [9712-9712]
- Line 1409: Duplicate range [9712-9712]
- Line 1431: Duplicate range [9712-9712]
- Line 1453: Duplicate range [9712-9712]
- Line 1475: Duplicate range [9712-9712]
- Line 1497: Duplicate range [9712-9712]
- Line 1519: Duplicate range [9712-9712]
- Line 1541: Duplicate range [9712-9712]
- Line 1563: Duplicate range [9712-9712]
- Line 1585: Duplicate range [9712-9712]
- Line 1607: Duplicate range [9712-9712]
- Line 1629: Duplicate range [9712-9712]
- Line 1651: Duplicate range [9712-9712]
- Line 1673: Duplicate range [9712-9712]
- Line 1695: Duplicate range [9712-9712]
- Line 1717: Duplicate range [9712-9712]
- Line 1739: Duplicate range [9712-9712]
- Line 1761: Duplicate range [9712-9712]

---

### File: dynamic/delusion/02-21-01-01.txt

**Errors:**
- Line 400: Non-sequential range [9713-10200] - Start (9713) < Previous start (10113)
- Line 20: Duplicate range [9713-9716]
- Line 229: Duplicate range [9781-9796]
- Line 362: Duplicate range [10016-10112]
- Line 419: Duplicate range [9713-10200]
- Line 438: Duplicate range [9713-10200]
- Line 457: Duplicate range [9713-10200]
- Line 476: Duplicate range [9713-10200]
- Line 495: Duplicate range [9713-10200]
- Line 514: Duplicate range [9713-10200]
- Line 533: Duplicate range [9713-10200]
- Line 552: Duplicate range [9713-10200]
- Line 571: Duplicate range [9713-10200]
- Line 590: Duplicate range [9713-10200]
- Line 609: Duplicate range [9713-10200]
- Line 628: Duplicate range [9713-10200]
- Line 647: Duplicate range [9713-10200]
- Line 666: Duplicate range [9713-10200]
- Line 685: Duplicate range [9713-10200]
- Line 704: Duplicate range [9713-10200]
- Line 723: Duplicate range [9713-10200]
- Line 742: Duplicate range [9713-10200]
- Line 761: Duplicate range [9713-10200]
- Line 780: Duplicate range [9713-10200]
- Line 799: Duplicate range [9713-10200]

---

### File: dynamic/delusion/02-22-01-01.txt

**Errors:**
- Line 96: Non-sequential range [10238-10254] - Start (10238) < Previous start (10250)
- Line 248: Duplicate range [10284-10304]
- Line 267: Duplicate range [10284-10304]
- Line 404: Duplicate range [10765-10765]
- Line 427: Duplicate range [10765-10765]
- Line 450: Duplicate range [10765-10765]
- Line 473: Duplicate range [10765-10765]
- Line 496: Duplicate range [10765-10765]
- Line 519: Duplicate range [10765-10765]
- Line 542: Duplicate range [10765-10765]
- Line 565: Duplicate range [10765-10765]
- Line 588: Duplicate range [10765-10765]
- Line 611: Duplicate range [10765-10765]
- Line 634: Duplicate range [10765-10765]

---

### File: dynamic/delusion/02-22-03-02.txt

**Errors:**
- Line 286: Non-sequential range [10900-11181] - Start (10900) < Previous start (11163)
- Line 134: Duplicate range [10936-10962]
- Line 305: Duplicate range [10900-11181]
- Line 324: Duplicate range [10900-11181]
- Line 343: Duplicate range [10900-11181]
- Line 362: Duplicate range [10900-11181]
- Line 381: Duplicate range [10900-11181]
- Line 400: Duplicate range [10900-11181]
- Line 419: Duplicate range [10900-11181]

---

### File: dynamic/delusion/02-22-03-03.txt

**Errors:**
- Line 85: Invalid range [11341-11321] - End < Start

---

### File: dynamic/delusion/02-22-04-01.txt

**Errors:**
- Line 766: Non-sequential range [11322-11479] - Start (11322) < Previous start (11476)
- Line 18: Duplicate range [11322-11327]
- Line 52: Duplicate range [11328-11334]
- Line 86: Duplicate range [11335-11341]
- Line 137: Duplicate range [11344-11358]
- Line 171: Duplicate range [11359-11363]
- Line 222: Duplicate range [11371-11378]
- Line 256: Duplicate range [11379-11383]
- Line 290: Duplicate range [11384-11386]
- Line 324: Duplicate range [11387-11389]
- Line 341: Duplicate range [11387-11389]
- Line 375: Duplicate range [11390-11399]
- Line 409: Duplicate range [11400-11405]
- Line 443: Duplicate range [11406-11410]
- Line 477: Duplicate range [11411-11417]
- Line 528: Duplicate range [11422-11431]
- Line 579: Duplicate range [11437-11445]
- Line 613: Duplicate range [11446-11455]
- Line 664: Duplicate range [11468-11475]
- Line 681: Duplicate range [11468-11475]
- Line 698: Duplicate range [11468-11475]
- Line 715: Duplicate range [11468-11475]
- Line 749: Duplicate range [11476-11479]

---

### File: dynamic/delusion/02-22-05-01.txt

**Errors:**
- Line 231: Non-sequential range [11480-11480] - Start (11480) < Previous start (11721)
- Line 254: Duplicate range [11480-11480]
- Line 277: Duplicate range [11480-11480]

---

### File: dynamic/delusion/02-22-05-02.txt

**Errors:**
- Line 1141: Non-sequential range [11742-11779] - Start (11742) < Previous start (11818)
- Line 1217: Non-sequential range [11736-11823] - Start (11736) < Previous start (11785)

---

### File: dynamic/delusion/02-22-06-01.txt

**Errors:**
- Line 440: Invalid range [12003-12002] - End < Start
- Line 22: Duplicate range [11825-11838]
- Line 64: Duplicate range [11838-11847]
- Line 127: Duplicate range [11859-11871]
- Line 232: Duplicate range [11898-11905]
- Line 274: Duplicate range [11906-11922]
- Line 336: Duplicate range [11923-11975]
- Line 377: Duplicate range [11985-11990]
- Line 419: Duplicate range [11991-12002]

---

### File: dynamic/delusion/02-23-01-01.txt

**Errors:**
- Line 22: Duplicate range [12011-12022]
- Line 64: Duplicate range [12022-12043]
- Line 295: Duplicate range [12135-12145]
- Line 316: Duplicate range [12135-12145]
- Line 337: Duplicate range [12135-12145]
- Line 358: Duplicate range [12135-12145]
- Line 421: Duplicate range [12148-12154]
- Line 463: Duplicate range [12155-12167]
- Line 589: Duplicate range [12205-12235]
- Line 610: Duplicate range [12205-12235]
- Line 652: Duplicate range [12236-12244]
- Line 673: Duplicate range [12236-12244]
- Line 694: Duplicate range [12236-12244]
- Line 715: Duplicate range [12236-12244]

---

### File: dynamic/delusion/02-23-02-01.txt

**Errors:**
- Line 904: Non-sequential range [12278-12320] - Start (12278) < Previous start (12345)
- Line 925: Non-sequential range [12245-12350] - Start (12245) < Previous start (12278)
- Line 1009: Non-sequential range [12245-12258] - Start (12245) < Previous start (12286)
- Line 1114: Non-sequential range [12245-12350] - Start (12245) < Previous start (12315)
- Line 1156: Non-sequential range [12260-12263] - Start (12260) < Previous start (12278)
- Line 1324: Non-sequential range [12245-12350] - Start (12245) < Previous start (12300)
- Line 1513: Non-sequential range [12245-12350] - Start (12245) < Previous start (12344)
- Line 1051: Duplicate range [12306-12307]
- Line 1072: Duplicate range [12308-12314]
- Line 1093: Duplicate range [12315-12320]
- Line 1114: Duplicate range [12245-12350]
- Line 1156: Duplicate range [12260-12263]
- Line 1177: Duplicate range [12271-12276]
- Line 1198: Duplicate range [12283-12284]
- Line 1219: Duplicate range [12290-12292]
- Line 1240: Duplicate range [12293-12296]
- Line 1282: Duplicate range [12297-12299]
- Line 1324: Duplicate range [12245-12350]
- Line 1345: Duplicate range [12245-12258]
- Line 1387: Duplicate range [12278-12279]
- Line 1408: Duplicate range [12280-12299]
- Line 1450: Duplicate range [12338-12340]
- Line 1492: Duplicate range [12344-12350]
- Line 1513: Duplicate range [12245-12350]
- Line 1534: Duplicate range [12245-12350]
- Line 1555: Duplicate range [12245-12350]

---

### File: dynamic/delusion/02-23-02-02.txt

**Errors:**
- Line 22: Duplicate range [12351-12362]
- Line 64: Duplicate range [12363-12411]
- Line 232: Duplicate range [12461-12494]
- Line 274: Duplicate range [12495-12504]

---

### File: dynamic/delusion/02-23-03-01.txt

**Errors:**
- Line 22: Duplicate range [12522-12540]
- Line 43: Duplicate range [12522-12540]
- Line 85: Duplicate range [12541-12605]
- Line 106: Duplicate range [12541-12605]
- Line 127: Duplicate range [12541-12605]
- Line 169: Duplicate range [12606-12663]
- Line 211: Duplicate range [12664-12688]
- Line 232: Duplicate range [12664-12688]
- Line 274: Duplicate range [12689-12709]
- Line 295: Duplicate range [12689-12709]
- Line 358: Duplicate range [12718-12736]
- Line 400: Duplicate range [12737-12754]

---

### File: dynamic/delusion/02-23-03-02.txt

**Errors:**
- Line 20: Duplicate range [12779-12780]
- Line 362: Duplicate range [12876-12878]

---

### File: dynamic/delusion/02-23-04-01.txt

**Errors:**
- Line 22: Duplicate range [13304-13308]
- Line 43: Duplicate range [13304-13308]
- Line 127: Duplicate range [13307-13308]
- Line 190: Duplicate range [13309-13317]
- Line 232: Duplicate range [13318-13336]
- Line 337: Duplicate range [13437-13493]
- Line 442: Duplicate range [13614-13693]

---

### File: dynamic/delusion/02-23-06-01.txt

**Errors:**
- Line 22: Duplicate range [13701-13705]

---

### File: dynamic/delusion/02-23-06-02.txt

**Errors:**
- Line 358: Non-sequential range [14200-14206] - Start (14200) < Previous start (14277)
- Line 392: Duplicate range [14207-14214]
- Line 460: Duplicate range [14222-14224]
- Line 579: Duplicate range [14239-14242]
- Line 613: Duplicate range [14242-14243]
- Line 715: Duplicate range [14248-14251]
- Line 732: Duplicate range [14249-14252]
- Line 766: Duplicate range [14252-14255]
- Line 800: Duplicate range [14255-14256]
- Line 817: Duplicate range [14256-14258]
- Line 851: Duplicate range [14258-14259]
- Line 868: Duplicate range [14267-14269]
- Line 953: Duplicate range [14276-14277]
- Line 970: Duplicate range [14277-14277]

---

### File: dynamic/delusion/02-23-08-03.txt

**Errors:**
- Line 241: Duplicate range [14639-14639]
- Line 261: Duplicate range [14639-14639]
- Line 281: Duplicate range [14639-14639]

---

### File: dynamic/delusion/02-23-08-05.txt

**Errors:**
- Line 101: Non-sequential range [14642-14650] - Start (14642) < Previous start (14738)
- Line 181: Duplicate range [14720-14737]

---

### File: dynamic/delusion/02-23-08-09.txt

**Errors:**
- Line 101: Non-sequential range [14753-14765] - Start (14753) < Previous start (14810)

---

### File: dynamic/delusion/02-24-01-01.txt

**Errors:**
- Line 20: Duplicate range [15275-15277]

---

### File: dynamic/delusion/02-25-02-01.txt

**Errors:**
- Line 23: Duplicate range [16329-16344]
- Line 45: Duplicate range [16329-16344]
- Line 67: Duplicate range [16329-16344]
- Line 89: Duplicate range [16329-16344]
- Line 133: Duplicate range [16343-16344]
- Line 177: Duplicate range [16344-16351]
- Line 199: Duplicate range [16344-16351]
- Line 221: Duplicate range [16344-16351]
- Line 287: Duplicate range [16352-16358]
- Line 309: Duplicate range [16352-16358]
- Line 331: Duplicate range [16352-16358]
- Line 353: Duplicate range [16352-16358]

---

### File: dynamic/delusion/02-25-03-01.txt

**Errors:**
- Line 61: Non-sequential range [16360-16370] - Start (16360) < Previous start (16395)

---

### File: dynamic/delusion/02-25-04-01.txt

**Errors:**
- Line 63: Duplicate range [16435-16435]
- Line 85: Duplicate range [16435-16435]
- Line 107: Duplicate range [16435-16435]
- Line 129: Duplicate range [16435-16435]
- Line 151: Duplicate range [16435-16435]
- Line 173: Duplicate range [16435-16435]
- Line 195: Duplicate range [16435-16435]
- Line 217: Duplicate range [16435-16435]
- Line 239: Duplicate range [16435-16435]
- Line 261: Duplicate range [16435-16435]
- Line 283: Duplicate range [16435-16435]
- Line 305: Duplicate range [16435-16435]
- Line 327: Duplicate range [16435-16435]
- Line 349: Duplicate range [16435-16435]
- Line 371: Duplicate range [16435-16435]
- Line 393: Duplicate range [16435-16435]
- Line 415: Duplicate range [16435-16435]
- Line 437: Duplicate range [16435-16435]
- Line 459: Duplicate range [16435-16435]
- Line 481: Duplicate range [16435-16435]
- Line 503: Duplicate range [16435-16435]
- Line 525: Duplicate range [16435-16435]
- Line 547: Duplicate range [16435-16435]

---

### File: dynamic/delusion/02-25-06-01.txt

**Errors:**
- Line 61: Non-sequential range [16719-16728] - Start (16719) < Previous start (16750)
- Line 101: Duplicate range [16750-16769]

---

### File: dynamic/delusion/02-25-06-02.txt

**Errors:**
- Line 161: Non-sequential range [16840-16855] - Start (16840) < Previous start (16864)

---

### File: dynamic/delusion/02-25-07-01.txt

**Errors:**
- Line 381: Non-sequential range [17240-17318] - Start (17240) < Previous start (17319)
- Line 438: Invalid range [17333-17330] - End < Start
- Line 457: Non-sequential range [17258-17330] - Start (17258) < Previous start (17333)
- Line 476: Non-sequential range [17242-17330] - Start (17242) < Previous start (17258)
- Line 514: Non-sequential range [17111-17330] - Start (17111) < Previous start (17328)
- Line 571: Non-sequential range [17142-17330] - Start (17142) < Previous start (17320)
- Line 609: Invalid range [17343-17330] - End < Start
- Line 628: Non-sequential range [16972-17330] - Start (16972) < Previous start (17343)
- Line 780: Non-sequential range [17285-17330] - Start (17285) < Previous start (17305)
- Line 799: Non-sequential range [16972-17330] - Start (16972) < Previous start (17285)
- Line 856: Non-sequential range [17230-17330] - Start (17230) < Previous start (17306)
- Line 970: Non-sequential range [16972-17330] - Start (16972) < Previous start (17328)
- Line 495: Duplicate range [17328-17330]
- Line 533: Duplicate range [17319-17330]
- Line 647: Duplicate range [16972-17330]
- Line 666: Duplicate range [17034-17046]
- Line 799: Duplicate range [16972-17330]
- Line 913: Duplicate range [17285-17330]
- Line 932: Duplicate range [17328-17330]
- Line 951: Duplicate range [17328-17330]
- Line 970: Duplicate range [16972-17330]
- Line 989: Duplicate range [16972-17330]
- Line 1008: Duplicate range [16972-17330]
- Line 1027: Duplicate range [16972-17330]
- Line 1046: Duplicate range [16972-17330]
- Line 1065: Duplicate range [16972-17330]
- Line 1084: Duplicate range [16972-17330]
- Line 1103: Duplicate range [16972-17330]
- Line 1122: Duplicate range [16972-17330]

---

### File: dynamic/delusion_backup/01-03-01-01.txt

**Errors:**
- Line 81: Non-sequential range [1582-1582] - Start (1582) < Previous start (1666)
- Line 97: Duplicate range [1582-1582]
- Line 113: Duplicate range [1582-1582]
- Line 129: Duplicate range [1582-1582]
- Line 145: Duplicate range [1582-1582]
- Line 161: Duplicate range [1582-1582]
- Line 177: Duplicate range [1582-1582]
- Line 193: Duplicate range [1582-1582]

---

### File: dynamic/delusion_backup/01-03-02-01.txt

**Errors:**
- Line 49: Non-sequential range [1671-1671] - Start (1671) < Previous start (1711)
- Line 65: Duplicate range [1671-1671]
- Line 81: Duplicate range [1671-1671]
- Line 97: Duplicate range [1671-1671]
- Line 113: Duplicate range [1671-1671]
- Line 129: Duplicate range [1671-1671]

---

### File: dynamic/delusion_backup/01-03-03-01.txt

**Errors:**
- Line 97: Non-sequential range [1732-1732] - Start (1732) < Previous start (1901)
- Line 113: Duplicate range [1732-1732]
- Line 129: Duplicate range [1732-1732]
- Line 145: Duplicate range [1732-1732]
- Line 161: Duplicate range [1732-1732]
- Line 177: Duplicate range [1732-1732]
- Line 193: Duplicate range [1732-1732]
- Line 209: Duplicate range [1732-1732]

---

### File: dynamic/delusion_backup/01-04-01-01.txt

**Errors:**
- Line 237: Non-sequential range [1902-2214] - Start (1902) < Previous start (1993)
- Line 327: Non-sequential range [1943-2043] - Start (1943) < Previous start (1951)
- Line 385: Non-sequential range [2272-2277] - Start (2272) < Previous start (2276)
- Line 405: Non-sequential range [2076-2196] - Start (2076) < Previous start (2272)
- Line 459: Non-sequential range [1902-2208] - Start (1902) < Previous start (2208)
- Line 495: Non-sequential range [2074-2096] - Start (2074) < Previous start (2210)
- Line 549: Non-sequential range [1943-1958] - Start (1943) < Previous start (2212)
- Line 585: Non-sequential range [2208-2214] - Start (2208) < Previous start (2303)
- Line 603: Non-sequential range [2033-2052] - Start (2033) < Previous start (2208)
- Line 695: Non-sequential range [2102-2106] - Start (2102) < Previous start (2341)
- Line 749: Non-sequential range [2108-2228] - Start (2108) < Previous start (2188)
- Line 585: Duplicate range [2208-2214]

---

### File: dynamic/delusion_backup/01-04-06-01.txt

**Errors:**
- Line 253: Non-sequential range [2873-2873] - Start (2873) < Previous start (2971)
- Line 274: Duplicate range [2873-2873]

---

### File: dynamic/delusion_backup/01-05-04-01.txt

**Errors:**
- Line 449: Non-sequential range [6200-6419] - Start (6200) < Previous start (6301)
- Line 478: Non-sequential range [4848-4857] - Start (4848) < Previous start (6200)
- Line 826: Non-sequential range [4848-4950] - Start (4848) < Previous start (4895)
- Line 1116: Non-sequential range [4885-4948] - Start (4885) < Previous start (4946)
- Line 478: Duplicate range [4848-4857]

---

### File: dynamic/delusion_backup/01-05-04-06.txt

**Errors:**
- Line 1: Invalid range [150-1] - End < Start
- Line 18: Invalid range [150-2] - End < Start
- Line 35: Invalid range [150-3] - End < Start
- Line 52: Invalid range [150-4] - End < Start
- Line 69: Invalid range [150-5] - End < Start
- Line 119: Invalid range [151-1] - End < Start
- Line 136: Invalid range [151-2] - End < Start
- Line 153: Invalid range [151-3] - End < Start
- Line 170: Invalid range [151-4] - End < Start
- Line 187: Invalid range [151-5] - End < Start
- Line 204: Invalid range [151-6] - End < Start
- Line 254: Invalid range [152-1] - End < Start
- Line 271: Invalid range [152-2] - End < Start
- Line 288: Invalid range [152-3] - End < Start
- Line 305: Invalid range [152-4] - End < Start
- Line 322: Invalid range [152-5] - End < Start
- Line 339: Invalid range [152-6] - End < Start
- Line 389: Invalid range [153-1] - End < Start
- Line 406: Invalid range [153-2] - End < Start
- Line 423: Invalid range [153-3] - End < Start
- Line 440: Invalid range [153-4] - End < Start
- Line 457: Invalid range [153-5] - End < Start
- Line 474: Invalid range [153-6] - End < Start
- Line 524: Invalid range [154-1] - End < Start
- Line 541: Invalid range [154-2] - End < Start
- Line 558: Invalid range [154-3] - End < Start
- Line 575: Invalid range [154-4] - End < Start
- Line 592: Invalid range [154-5] - End < Start
- Line 609: Invalid range [154-6] - End < Start
- Line 659: Invalid range [155-1] - End < Start
- Line 676: Invalid range [155-2] - End < Start
- Line 693: Invalid range [155-3] - End < Start
- Line 710: Invalid range [155-4] - End < Start
- Line 727: Invalid range [155-5] - End < Start
- Line 744: Invalid range [155-6] - End < Start
- Line 794: Invalid range [156-1] - End < Start
- Line 811: Invalid range [156-2] - End < Start
- Line 828: Invalid range [156-3] - End < Start
- Line 845: Invalid range [156-4] - End < Start
- Line 862: Invalid range [156-5] - End < Start
- Line 879: Invalid range [156-6] - End < Start
- Line 929: Invalid range [157-1] - End < Start
- Line 946: Invalid range [157-2] - End < Start
- Line 963: Invalid range [157-3] - End < Start
- Line 980: Invalid range [157-4] - End < Start
- Line 997: Invalid range [157-5] - End < Start
- Line 1014: Invalid range [157-6] - End < Start
- Line 1064: Invalid range [158-1] - End < Start
- Line 1081: Invalid range [158-2] - End < Start
- Line 1098: Invalid range [158-3] - End < Start
- Line 1115: Invalid range [158-4] - End < Start
- Line 1132: Invalid range [158-5] - End < Start
- Line 1149: Invalid range [158-6] - End < Start

---

### File: dynamic/delusion_backup/01-08-02-01.txt

**Errors:**
- Line 191: Non-sequential range [10548-10673] - Start (10548) < Previous start (10645)
- Line 20: Duplicate range [10548-10559]
- Line 96: Duplicate range [10585-10619]
- Line 134: Duplicate range [10620-10633]
- Line 210: Duplicate range [10548-10673]
- Line 229: Duplicate range [10548-10673]
- Line 248: Duplicate range [10548-10673]
- Line 267: Duplicate range [10548-10673]
- Line 286: Duplicate range [10548-10673]
- Line 305: Duplicate range [10548-10673]

---

### File: dynamic/delusion_backup/01-13-01-01.txt

**Errors:**
- Line 552: Non-sequential range [16025-16273] - Start (16025) < Previous start (16255)
- Line 609: Non-sequential range [16025-16273] - Start (16025) < Previous start (16078)
- Line 647: Non-sequential range [16043-16273] - Start (16043) < Previous start (16105)
- Line 666: Non-sequential range [16025-16273] - Start (16025) < Previous start (16043)
- Line 704: Non-sequential range [16025-16273] - Start (16025) < Previous start (16038)
- Line 818: Non-sequential range [16025-16273] - Start (16025) < Previous start (16243)
- Line 894: Non-sequential range [16025-16273] - Start (16025) < Previous start (16255)
- Line 115: Duplicate range [16045-16049]
- Line 609: Duplicate range [16025-16273]
- Line 647: Duplicate range [16043-16273]
- Line 666: Duplicate range [16025-16273]
- Line 704: Duplicate range [16025-16273]
- Line 723: Duplicate range [16078-16273]
- Line 742: Duplicate range [16105-16273]
- Line 818: Duplicate range [16025-16273]
- Line 837: Duplicate range [16043-16273]
- Line 875: Duplicate range [16255-16268]
- Line 894: Duplicate range [16025-16273]
- Line 913: Duplicate range [16038-16273]
- Line 932: Duplicate range [16105-16273]
- Line 951: Duplicate range [16129-16273]

---

### File: dynamic/delusion_backup/01-13-02-01.txt

**Errors:**
- Line 153: Non-sequential range [16274-16450] - Start (16274) < Previous start (16424)
- Line 39: Duplicate range [16283-16302]
- Line 172: Duplicate range [16274-16450]
- Line 191: Duplicate range [16274-16450]
- Line 210: Duplicate range [16274-16450]
- Line 229: Duplicate range [16274-16450]
- Line 248: Duplicate range [16274-16450]
- Line 267: Duplicate range [16274-16450]
- Line 286: Duplicate range [16274-16450]
- Line 305: Duplicate range [16274-16450]
- Line 324: Duplicate range [16274-16450]
- Line 343: Duplicate range [16274-16450]
- Line 362: Duplicate range [16274-16450]
- Line 381: Duplicate range [16274-16450]
- Line 400: Duplicate range [16274-16450]
- Line 419: Duplicate range [16274-16450]

---

### File: dynamic/delusion_backup/01-13-03-01.txt

**Errors:**
- Line 172: Non-sequential range [16483-16637] - Start (16483) < Previous start (16619)
- Line 58: Duplicate range [16528-16541]
- Line 191: Duplicate range [16483-16637]
- Line 210: Duplicate range [16483-16637]
- Line 229: Duplicate range [16483-16637]
- Line 248: Duplicate range [16483-16637]
- Line 267: Duplicate range [16483-16637]
- Line 286: Duplicate range [16483-16637]
- Line 305: Duplicate range [16483-16637]
- Line 324: Duplicate range [16483-16637]
- Line 343: Duplicate range [16483-16637]
- Line 362: Duplicate range [16483-16637]
- Line 381: Duplicate range [16483-16637]
- Line 400: Duplicate range [16483-16637]
- Line 419: Duplicate range [16483-16637]
- Line 438: Duplicate range [16483-16637]

---

### File: dynamic/delusion_backup/01-13-04-01.txt

**Errors:**
- Line 169: Non-sequential range [16769-16769] - Start (16769) < Previous start (16863)

---

### File: dynamic/delusion_backup/02-15-01-01.txt

**Errors:**
- Line 324: Non-sequential range [1-250] - Start (1) < Previous start (241)
- Line 343: Duplicate range [1-250]
- Line 362: Duplicate range [1-250]
- Line 381: Duplicate range [1-250]
- Line 400: Duplicate range [1-250]
- Line 419: Duplicate range [1-250]
- Line 438: Duplicate range [1-250]

---

### File: dynamic/delusion_backup/02-15-02-01.txt

**Errors:**
- Line 67: Non-sequential range [474-474] - Start (474) < Previous start (601)
- Line 89: Duplicate range [474-474]
- Line 111: Duplicate range [474-474]
- Line 133: Duplicate range [474-474]

---

### File: dynamic/delusion_backup/02-16-02-01.txt

**Errors:**
- Line 89: Non-sequential range [1021-1021] - Start (1021) < Previous start (1181)
- Line 111: Duplicate range [1021-1021]
- Line 133: Duplicate range [1021-1021]

---

### File: dynamic/delusion_backup/02-16-05-01.txt

**Errors:**
- Line 45: Non-sequential range [1638-1753] - Start (1638) < Previous start (1711)
- Line 67: Duplicate range [1638-1753]

---

### File: dynamic/delusion_backup/02-17-05-01.txt

**Errors:**
- Line 64: Duplicate range [2714-2716]
- Line 190: Duplicate range [2750-2753]
- Line 253: Duplicate range [2758-2759]

---

### File: dynamic/delusion_backup/02-17-07-01.txt

**Errors:**
- Line 81: Non-sequential range [3005-3015] - Start (3005) < Previous start (3047)
- Line 141: Duplicate range [3047-3056]

---

### File: dynamic/delusion_final_backup/01-02-02-02.txt

**Errors:**
- Line 248: Duplicate range [1532-1538]

---

### File: dynamic/delusion_final_backup/01-04-03-01.txt

**Errors:**
- Line 33: Duplicate range [2833-2833]
- Line 49: Duplicate range [2833-2833]
- Line 65: Duplicate range [2833-2833]
- Line 81: Duplicate range [2833-2833]

---

### File: dynamic/delusion_final_backup/01-04-08-01.txt

**Errors:**
- Line 58: Duplicate range [3002-3008]

---

### File: dynamic/delusion_final_backup/01-04-10-01.txt

**Errors:**
- Line 17: Duplicate range [3037-3039]
- Line 33: Duplicate range [3037-3039]

---

### File: dynamic/delusion_final_backup/01-05-04-04.txt

**Errors:**
- Line 1: Duplicate range [6422-6422]

---

### File: dynamic/delusion_final_backup/01-06-01-01.txt

**Errors:**
- Line 18: Non-sequential range [6801-6801] - Start (6801) < Previous start (6808)
- Line 35: Non-sequential range [6801-6801] - Start (6801) < Previous start (6815)
- Line 52: Non-sequential range [6801-6801] - Start (6801) < Previous start (6823)
- Line 69: Non-sequential range [6801-6801] - Start (6801) < Previous start (6830)
- Line 120: Non-sequential range [6801-6801] - Start (6801) < Previous start (6838)
- Line 137: Non-sequential range [6801-6801] - Start (6801) < Previous start (6845)
- Line 154: Non-sequential range [6801-6801] - Start (6801) < Previous start (6852)
- Line 171: Non-sequential range [6801-6801] - Start (6801) < Previous start (6859)
- Line 188: Non-sequential range [6801-6801] - Start (6801) < Previous start (6866)
- Line 205: Non-sequential range [6801-6801] - Start (6801) < Previous start (6873)
- Line 256: Non-sequential range [6801-6801] - Start (6801) < Previous start (6880)
- Line 273: Non-sequential range [6801-6801] - Start (6801) < Previous start (6886)
- Line 290: Non-sequential range [6801-6801] - Start (6801) < Previous start (6893)
- Line 307: Non-sequential range [6801-6801] - Start (6801) < Previous start (6899)
- Line 324: Non-sequential range [6801-6801] - Start (6801) < Previous start (6906)
- Line 341: Non-sequential range [6801-6801] - Start (6801) < Previous start (6912)
- Line 392: Non-sequential range [6801-6801] - Start (6801) < Previous start (6919)
- Line 409: Non-sequential range [6801-6801] - Start (6801) < Previous start (6925)
- Line 426: Non-sequential range [6801-6801] - Start (6801) < Previous start (6931)
- Line 443: Non-sequential range [6801-6801] - Start (6801) < Previous start (6938)
- Line 460: Non-sequential range [6801-6801] - Start (6801) < Previous start (6944)
- Line 477: Non-sequential range [6801-6801] - Start (6801) < Previous start (6950)
- Line 528: Non-sequential range [6801-6801] - Start (6801) < Previous start (6957)
- Line 545: Non-sequential range [6801-6801] - Start (6801) < Previous start (6963)
- Line 562: Non-sequential range [6801-6801] - Start (6801) < Previous start (6970)
- Line 579: Non-sequential range [6801-6801] - Start (6801) < Previous start (6976)
- Line 596: Non-sequential range [6801-6801] - Start (6801) < Previous start (6983)
- Line 613: Non-sequential range [6801-6801] - Start (6801) < Previous start (6989)
- Line 664: Non-sequential range [6801-6801] - Start (6801) < Previous start (6996)
- Line 681: Non-sequential range [6801-6801] - Start (6801) < Previous start (7003)
- Line 698: Non-sequential range [6801-6801] - Start (6801) < Previous start (7010)
- Line 715: Non-sequential range [6801-6801] - Start (6801) < Previous start (7017)
- Line 732: Non-sequential range [6801-6801] - Start (6801) < Previous start (7024)
- Line 749: Non-sequential range [6801-6801] - Start (6801) < Previous start (7031)
- Line 800: Non-sequential range [6801-6801] - Start (6801) < Previous start (7038)
- Line 817: Non-sequential range [6801-6801] - Start (6801) < Previous start (7045)
- Line 834: Non-sequential range [6801-6801] - Start (6801) < Previous start (7053)
- Line 851: Non-sequential range [6801-6801] - Start (6801) < Previous start (7061)
- Line 868: Non-sequential range [6801-6801] - Start (6801) < Previous start (7069)
- Line 885: Non-sequential range [6801-6801] - Start (6801) < Previous start (7077)
- Line 936: Non-sequential range [6801-6801] - Start (6801) < Previous start (7085)
- Line 953: Non-sequential range [6801-6801] - Start (6801) < Previous start (7096)
- Line 18: Duplicate range [6801-6801]
- Line 35: Duplicate range [6801-6801]
- Line 52: Duplicate range [6801-6801]
- Line 69: Duplicate range [6801-6801]
- Line 120: Duplicate range [6801-6801]
- Line 137: Duplicate range [6801-6801]
- Line 154: Duplicate range [6801-6801]
- Line 171: Duplicate range [6801-6801]
- Line 188: Duplicate range [6801-6801]
- Line 205: Duplicate range [6801-6801]
- Line 256: Duplicate range [6801-6801]
- Line 273: Duplicate range [6801-6801]
- Line 290: Duplicate range [6801-6801]
- Line 307: Duplicate range [6801-6801]
- Line 324: Duplicate range [6801-6801]
- Line 341: Duplicate range [6801-6801]
- Line 392: Duplicate range [6801-6801]
- Line 409: Duplicate range [6801-6801]
- Line 426: Duplicate range [6801-6801]
- Line 443: Duplicate range [6801-6801]
- Line 460: Duplicate range [6801-6801]
- Line 477: Duplicate range [6801-6801]
- Line 528: Duplicate range [6801-6801]
- Line 545: Duplicate range [6801-6801]
- Line 562: Duplicate range [6801-6801]
- Line 579: Duplicate range [6801-6801]
- Line 596: Duplicate range [6801-6801]
- Line 613: Duplicate range [6801-6801]
- Line 664: Duplicate range [6801-6801]
- Line 681: Duplicate range [6801-6801]
- Line 698: Duplicate range [6801-6801]
- Line 715: Duplicate range [6801-6801]
- Line 732: Duplicate range [6801-6801]
- Line 749: Duplicate range [6801-6801]
- Line 800: Duplicate range [6801-6801]
- Line 817: Duplicate range [6801-6801]
- Line 834: Duplicate range [6801-6801]
- Line 851: Duplicate range [6801-6801]
- Line 868: Duplicate range [6801-6801]
- Line 885: Duplicate range [6801-6801]
- Line 936: Duplicate range [6801-6801]
- Line 953: Duplicate range [6801-6801]

---

### File: dynamic/delusion_final_backup/01-06-04-01.txt

**Errors:**
- Line 23: Duplicate range [8138-8142]
- Line 67: Duplicate range [8143-8152]
- Line 111: Duplicate range [8153-8171]
- Line 133: Duplicate range [8153-8171]
- Line 155: Duplicate range [8153-8171]
- Line 177: Duplicate range [8153-8171]
- Line 199: Duplicate range [8153-8171]
- Line 243: Duplicate range [8172-8190]
- Line 265: Duplicate range [8172-8190]
- Line 309: Duplicate range [8191-8218]
- Line 375: Duplicate range [8232-8253]
- Line 419: Duplicate range [8254-8273]
- Line 463: Duplicate range [8274-8287]
- Line 485: Duplicate range [8274-8287]
- Line 507: Duplicate range [8274-8287]

---

### File: dynamic/delusion_final_backup/01-06-13-01.txt

**Errors:**
- Line 248: Non-sequential range [9526-9528] - Start (9526) < Previous start (9575)
- Line 343: Non-sequential range [9537-9542] - Start (9537) < Previous start (9566)
- Line 476: Non-sequential range [9584-9604] - Start (9584) < Previous start (9591)
- Line 495: Non-sequential range [9575-9582] - Start (9575) < Previous start (9584)
- Line 533: Non-sequential range [9584-9604] - Start (9584) < Previous start (9597)
- Line 590: Non-sequential range [9614-9670] - Start (9614) < Previous start (9617)
- Line 495: Duplicate range [9575-9582]
- Line 533: Duplicate range [9584-9604]

---

### File: dynamic/delusion_final_backup/01-09-01-01.txt

**Errors:**
- Line 1582: Non-sequential range [11682-11686] - Start (11682) < Previous start (12142)
- Line 1602: Non-sequential range [11687-11693] - Start (11687) < Previous start (12148)
- Line 1622: Non-sequential range [11694-11698] - Start (11694) < Previous start (12155)
- Line 1642: Non-sequential range [11699-11710] - Start (11699) < Previous start (12161)
- Line 1662: Non-sequential range [11711-11728] - Start (11711) < Previous start (12168)
- Line 1682: Non-sequential range [11729-11742] - Start (11729) < Previous start (12177)
- Line 1702: Non-sequential range [11743-11758] - Start (11743) < Previous start (12186)
- Line 1722: Non-sequential range [11759-11781] - Start (11759) < Previous start (12195)
- Line 1742: Non-sequential range [11782-11788] - Start (11782) < Previous start (12205)
- Line 1762: Non-sequential range [11789-11802] - Start (11789) < Previous start (12216)
- Line 1782: Non-sequential range [11803-11818] - Start (11803) < Previous start (12228)
- Line 1802: Non-sequential range [11819-11838] - Start (11819) < Previous start (12239)
- Line 1822: Non-sequential range [11854-11873] - Start (11854) < Previous start (12251)
- Line 1842: Non-sequential range [11874-11895] - Start (11874) < Previous start (12259)
- Line 1862: Non-sequential range [11896-11910] - Start (11896) < Previous start (12267)
- Line 1882: Non-sequential range [11911-11932] - Start (11911) < Previous start (12275)
- Line 1902: Non-sequential range [11933-11947] - Start (11933) < Previous start (12284)
- Line 1922: Non-sequential range [11948-11974] - Start (11948) < Previous start (12289)
- Line 1942: Non-sequential range [11975-11994] - Start (11975) < Previous start (12295)
- Line 1962: Non-sequential range [11995-12000] - Start (11995) < Previous start (12301)
- Line 1982: Non-sequential range [12001-12018] - Start (12001) < Previous start (12307)
- Line 2002: Non-sequential range [12019-12040] - Start (12019) < Previous start (12316)
- Line 2022: Non-sequential range [12041-12053] - Start (12041) < Previous start (12326)
- Line 2042: Non-sequential range [12054-12067] - Start (12054) < Previous start (12335)
- Line 2062: Non-sequential range [12068-12086] - Start (12068) < Previous start (12345)
- Line 2082: Non-sequential range [12087-12105] - Start (12087) < Previous start (12356)
- Line 2102: Non-sequential range [12106-12117] - Start (12106) < Previous start (12368)
- Line 2122: Non-sequential range [12118-12137] - Start (12118) < Previous start (12380)
- Line 2142: Non-sequential range [12138-12153] - Start (12138) < Previous start (12392)
- Line 2162: Non-sequential range [12154-12166] - Start (12154) < Previous start (12402)
- Line 2182: Non-sequential range [12167-12191] - Start (12167) < Previous start (12413)
- Line 2202: Non-sequential range [12192-12208] - Start (12192) < Previous start (12424)
- Line 2222: Non-sequential range [12209-12226] - Start (12209) < Previous start (12435)
- Line 2242: Non-sequential range [12227-12244] - Start (12227) < Previous start (12446)
- Line 2262: Non-sequential range [12245-12267] - Start (12245) < Previous start (12458)
- Line 2282: Non-sequential range [12268-12287] - Start (12268) < Previous start (12470)

---

### File: dynamic/delusion_final_backup/01-10-01-01.txt

**Errors:**
- Line 21: Non-sequential range [12500-12500] - Start (12500) < Previous start (12511)
- Line 41: Non-sequential range [12500-12500] - Start (12500) < Previous start (12526)
- Line 61: Non-sequential range [12500-12500] - Start (12500) < Previous start (12541)
- Line 81: Non-sequential range [12500-12500] - Start (12500) < Previous start (12557)
- Line 101: Non-sequential range [12500-12500] - Start (12500) < Previous start (12573)
- Line 121: Non-sequential range [12500-12500] - Start (12500) < Previous start (12589)
- Line 141: Non-sequential range [12500-12500] - Start (12500) < Previous start (12606)
- Line 161: Non-sequential range [12500-12500] - Start (12500) < Previous start (12616)
- Line 181: Non-sequential range [12500-12500] - Start (12500) < Previous start (12626)
- Line 221: Non-sequential range [12500-12500] - Start (12500) < Previous start (12647)
- Line 241: Non-sequential range [12500-12500] - Start (12500) < Previous start (12658)
- Line 261: Non-sequential range [12500-12500] - Start (12500) < Previous start (12669)
- Line 281: Non-sequential range [12500-12500] - Start (12500) < Previous start (12680)
- Line 301: Non-sequential range [12500-12500] - Start (12500) < Previous start (12691)
- Line 321: Non-sequential range [12500-12500] - Start (12500) < Previous start (12703)
- Line 341: Non-sequential range [12500-12500] - Start (12500) < Previous start (12713)
- Line 361: Non-sequential range [12500-12500] - Start (12500) < Previous start (12723)
- Line 381: Non-sequential range [12500-12500] - Start (12500) < Previous start (12733)
- Line 401: Non-sequential range [12500-12500] - Start (12500) < Previous start (12744)
- Line 421: Non-sequential range [12500-12500] - Start (12500) < Previous start (12752)
- Line 441: Non-sequential range [12500-12500] - Start (12500) < Previous start (12760)
- Line 461: Non-sequential range [12500-12500] - Start (12500) < Previous start (12768)
- Line 481: Non-sequential range [12500-12500] - Start (12500) < Previous start (12777)
- Line 501: Non-sequential range [12500-12500] - Start (12500) < Previous start (12786)
- Line 521: Non-sequential range [12500-12500] - Start (12500) < Previous start (12795)
- Line 541: Non-sequential range [12500-12500] - Start (12500) < Previous start (12804)
- Line 561: Non-sequential range [12500-12500] - Start (12500) < Previous start (12814)
- Line 581: Non-sequential range [12500-12500] - Start (12500) < Previous start (12825)
- Line 601: Non-sequential range [12500-12500] - Start (12500) < Previous start (12837)
- Line 621: Non-sequential range [12500-12500] - Start (12500) < Previous start (12849)
- Line 641: Non-sequential range [12500-12500] - Start (12500) < Previous start (12861)
- Line 661: Non-sequential range [12500-12500] - Start (12500) < Previous start (12870)
- Line 681: Non-sequential range [12500-12500] - Start (12500) < Previous start (12880)
- Line 701: Non-sequential range [12500-12500] - Start (12500) < Previous start (12890)
- Line 721: Non-sequential range [12500-12500] - Start (12500) < Previous start (12900)
- Line 741: Non-sequential range [12500-12500] - Start (12500) < Previous start (12906)
- Line 761: Non-sequential range [12500-12510] - Start (12500) < Previous start (12912)
- Line 781: Non-sequential range [12500-12500] - Start (12500) < Previous start (12918)
- Line 821: Non-sequential range [12500-12500] - Start (12500) < Previous start (12933)
- Line 841: Non-sequential range [12500-12510] - Start (12500) < Previous start (12942)
- Line 861: Non-sequential range [12511-12520] - Start (12511) < Previous start (12951)
- Line 881: Non-sequential range [12500-12500] - Start (12500) < Previous start (12960)
- Line 21: Duplicate range [12500-12500]
- Line 41: Duplicate range [12500-12500]
- Line 61: Duplicate range [12500-12500]
- Line 81: Duplicate range [12500-12500]
- Line 101: Duplicate range [12500-12500]
- Line 121: Duplicate range [12500-12500]
- Line 141: Duplicate range [12500-12500]
- Line 161: Duplicate range [12500-12500]
- Line 181: Duplicate range [12500-12500]
- Line 221: Duplicate range [12500-12500]
- Line 241: Duplicate range [12500-12500]
- Line 261: Duplicate range [12500-12500]
- Line 281: Duplicate range [12500-12500]
- Line 301: Duplicate range [12500-12500]
- Line 321: Duplicate range [12500-12500]
- Line 341: Duplicate range [12500-12500]
- Line 361: Duplicate range [12500-12500]
- Line 381: Duplicate range [12500-12500]
- Line 401: Duplicate range [12500-12500]
- Line 421: Duplicate range [12500-12500]
- Line 441: Duplicate range [12500-12500]
- Line 461: Duplicate range [12500-12500]
- Line 481: Duplicate range [12500-12500]
- Line 501: Duplicate range [12500-12500]
- Line 521: Duplicate range [12500-12500]
- Line 541: Duplicate range [12500-12500]
- Line 561: Duplicate range [12500-12500]
- Line 581: Duplicate range [12500-12500]
- Line 601: Duplicate range [12500-12500]
- Line 621: Duplicate range [12500-12500]
- Line 641: Duplicate range [12500-12500]
- Line 661: Duplicate range [12500-12500]
- Line 681: Duplicate range [12500-12500]
- Line 701: Duplicate range [12500-12500]
- Line 721: Duplicate range [12500-12500]
- Line 741: Duplicate range [12500-12500]
- Line 761: Duplicate range [12500-12510]
- Line 781: Duplicate range [12500-12500]
- Line 821: Duplicate range [12500-12500]
- Line 841: Duplicate range [12500-12510]
- Line 881: Duplicate range [12500-12500]

---

### File: dynamic/delusion_final_backup/01-13-05-01.txt

**Errors:**
- Line 23: Duplicate range [16866-16930]
- Line 45: Duplicate range [16866-16930]
- Line 67: Duplicate range [16866-16930]
- Line 89: Duplicate range [16866-16930]
- Line 111: Duplicate range [16866-16930]
- Line 133: Duplicate range [16866-16930]
- Line 155: Duplicate range [16866-16930]
- Line 177: Duplicate range [16866-16930]
- Line 199: Duplicate range [16866-16930]

---

### File: dynamic/delusion_final_backup/01-13-06-01.txt

**Errors:**
- Line 23: Duplicate range [17072-17200]
- Line 45: Duplicate range [17072-17200]
- Line 67: Duplicate range [17072-17200]
- Line 89: Duplicate range [17072-17200]
- Line 111: Duplicate range [17072-17200]
- Line 133: Duplicate range [17072-17200]
- Line 155: Duplicate range [17072-17200]
- Line 177: Duplicate range [17072-17200]
- Line 199: Duplicate range [17072-17200]

---

### File: dynamic/delusion_final_backup/01-14-01-01.txt

**Errors:**
- Line 23: Duplicate range [17361-17440]
- Line 45: Duplicate range [17361-17440]
- Line 67: Duplicate range [17361-17440]
- Line 89: Duplicate range [17361-17440]
- Line 111: Duplicate range [17361-17440]
- Line 133: Duplicate range [17361-17440]
- Line 155: Duplicate range [17361-17440]
- Line 177: Duplicate range [17361-17440]
- Line 199: Duplicate range [17361-17440]
- Line 221: Duplicate range [17361-17440]
- Line 243: Duplicate range [17361-17440]

---

### File: dynamic/delusion_final_backup/02-16-03-01.txt

**Errors:**
- Line 248: Non-sequential range [1182-1588] - Start (1182) < Previous start (1588)
- Line 20: Duplicate range [1182-1203]
- Line 267: Duplicate range [1182-1588]
- Line 286: Duplicate range [1182-1588]
- Line 305: Duplicate range [1182-1588]
- Line 324: Duplicate range [1182-1588]
- Line 343: Duplicate range [1182-1588]
- Line 362: Duplicate range [1182-1588]
- Line 381: Duplicate range [1182-1588]
- Line 400: Duplicate range [1182-1588]
- Line 419: Duplicate range [1182-1588]
- Line 438: Duplicate range [1182-1588]

---

### File: dynamic/delusion_final_backup/02-17-01-01.txt

**Errors:**
- Line 23: Duplicate range [1754-1830]
- Line 45: Duplicate range [1754-1830]
- Line 67: Duplicate range [1754-1830]
- Line 89: Duplicate range [1754-1830]
- Line 111: Duplicate range [1754-1830]

---

### File: dynamic/delusion_final_backup/02-17-08-01.txt

**Errors:**
- Line 81: Non-sequential range [3057-3070] - Start (3057) < Previous start (3115)

---

### File: dynamic/delusion_final_backup/02-17-09-01.txt

**Errors:**
- Line 51: Non-sequential range [3148-3159] - Start (3148) < Previous start (3185)
- Line 56: Non-sequential range [3125-3145] - Start (3125) < Previous start (3148)
- Line 81: Non-sequential range [3148-3159] - Start (3148) < Previous start (3185)
- Line 96: Non-sequential range [3148-3149] - Start (3148) < Previous start (3169)
- Line 106: Non-sequential range [3128-3135] - Start (3128) < Previous start (3178)
- Line 136: Non-sequential range [3141-3142] - Start (3141) < Previous start (3144)
- Line 31: Duplicate range [3147-3148]
- Line 66: Duplicate range [3169-3177]
- Line 71: Duplicate range [3178-3184]
- Line 76: Duplicate range [3185-3197]
- Line 81: Duplicate range [3148-3159]
- Line 91: Duplicate range [3169-3177]
- Line 101: Duplicate range [3178-3184]
- Line 106: Duplicate range [3128-3135]
- Line 111: Duplicate range [3136-3145]
- Line 141: Duplicate range [3146-3147]
- Line 146: Duplicate range [3147-3148]
- Line 156: Duplicate range [3169-3177]
- Line 166: Duplicate range [3185-3197]

---

### File: dynamic/delusion_final_backup/02-17-09-02.txt

**Errors:**
- Line 22: Duplicate range [3198-3202]
- Line 211: Duplicate range [3232-3240]
- Line 505: Duplicate range [3294-3298]
- Line 589: Duplicate range [3304-3306]

---

### File: dynamic/delusion_final_backup/02-17-10-01.txt

**Errors:**
- Line 22: Duplicate range [3307-3308]
- Line 211: Duplicate range [3316-3317]
- Line 253: Duplicate range [3317-3318]

---

### File: dynamic/delusion_final_backup/02-17-12-01.txt

**Errors:**
- Line 22: Duplicate range [3600-3607]
- Line 211: Duplicate range [3608-3623]
- Line 253: Duplicate range [3620-3623]

---

### File: dynamic/delusion_final_backup/02-17-13-01.txt

**Errors:**
- Line 197: Duplicate range [3823-3841]

---

### File: dynamic/delusion_final_backup/02-18-03-04.txt

**Errors:**
- Line 63: Duplicate range [4467-4467]
- Line 85: Duplicate range [4467-4467]
- Line 107: Duplicate range [4467-4467]
- Line 129: Duplicate range [4467-4467]
- Line 151: Duplicate range [4467-4467]
- Line 173: Duplicate range [4467-4467]
- Line 195: Duplicate range [4467-4467]
- Line 217: Duplicate range [4467-4467]
- Line 239: Duplicate range [4467-4467]
- Line 261: Duplicate range [4467-4467]
- Line 283: Duplicate range [4467-4467]
- Line 305: Duplicate range [4467-4467]
- Line 327: Duplicate range [4467-4467]
- Line 349: Duplicate range [4467-4467]
- Line 371: Duplicate range [4467-4467]
- Line 393: Duplicate range [4467-4467]
- Line 415: Duplicate range [4467-4467]
- Line 437: Duplicate range [4467-4467]
- Line 459: Duplicate range [4467-4467]
- Line 481: Duplicate range [4467-4467]
- Line 503: Duplicate range [4467-4467]
- Line 525: Duplicate range [4467-4467]
- Line 547: Duplicate range [4467-4467]

---

### File: dynamic/delusion_final_backup/02-18-04-01.txt

**Errors:**
- Line 22: Duplicate range [4468-4492]
- Line 43: Duplicate range [4468-4492]
- Line 85: Duplicate range [4493-4522]
- Line 127: Duplicate range [4523-4546]
- Line 169: Duplicate range [4547-4558]
- Line 253: Duplicate range [4566-4600]

---

### File: dynamic/delusion_final_backup/02-18-05-01.txt

**Errors:**
- Line 22: Duplicate range [4601-4625]
- Line 43: Duplicate range [4601-4625]
- Line 85: Duplicate range [4626-4638]
- Line 106: Duplicate range [4626-4638]
- Line 127: Duplicate range [4626-4638]
- Line 169: Duplicate range [4639-4695]
- Line 190: Duplicate range [4639-4695]

---

### File: dynamic/delusion_final_backup/02-18-06-01.txt

**Errors:**
- Line 22: Duplicate range [4696-4704]
- Line 148: Duplicate range [4715-4717]
- Line 379: Duplicate range [4728-4731]
- Line 484: Duplicate range [4735-4736]
- Line 505: Duplicate range [4735-4736]
- Line 736: Duplicate range [4746-4746]
- Line 757: Duplicate range [4746-4746]

---

### File: dynamic/delusion_final_backup/02-18-07-01.txt

**Errors:**
- Line 22: Duplicate range [4747-4751]
- Line 64: Duplicate range [4752-4767]
- Line 106: Duplicate range [4768-4788]
- Line 148: Duplicate range [4789-4801]
- Line 232: Duplicate range [4831-4844]

---

### File: dynamic/delusion_final_backup/02-18-09-01.txt

**Errors:**
- Line 22: Duplicate range [5085-5091]
- Line 169: Duplicate range [5090-5091]
- Line 421: Duplicate range [5101-5103]
- Line 715: Duplicate range [5112-5114]
- Line 736: Duplicate range [5112-5114]
- Line 757: Duplicate range [5112-5114]
- Line 778: Duplicate range [5112-5114]
- Line 820: Duplicate range [5113-5114]
- Line 1156: Duplicate range [5121-5124]
- Line 1198: Duplicate range [5123-5124]

---

### File: dynamic/delusion_final_backup/02-18-10-01.txt

**Errors:**
- Line 63: Duplicate range [5158-5158]
- Line 85: Duplicate range [5158-5158]
- Line 107: Duplicate range [5158-5158]
- Line 129: Duplicate range [5158-5158]
- Line 151: Duplicate range [5158-5158]
- Line 173: Duplicate range [5158-5158]
- Line 195: Duplicate range [5158-5158]
- Line 217: Duplicate range [5158-5158]
- Line 239: Duplicate range [5158-5158]
- Line 261: Duplicate range [5158-5158]
- Line 283: Duplicate range [5158-5158]
- Line 305: Duplicate range [5158-5158]
- Line 327: Duplicate range [5158-5158]
- Line 349: Duplicate range [5158-5158]
- Line 371: Duplicate range [5158-5158]
- Line 393: Duplicate range [5158-5158]
- Line 415: Duplicate range [5158-5158]
- Line 437: Duplicate range [5158-5158]
- Line 459: Duplicate range [5158-5158]
- Line 481: Duplicate range [5158-5158]
- Line 503: Duplicate range [5158-5158]
- Line 525: Duplicate range [5158-5158]
- Line 547: Duplicate range [5158-5158]

---

### File: dynamic/delusion_final_backup/02-18-12-01.txt

**Errors:**
- Line 23: Duplicate range [5242-5246]
- Line 45: Duplicate range [5242-5246]
- Line 89: Duplicate range [5247-5251]
- Line 111: Duplicate range [5247-5251]
- Line 199: Duplicate range [5254-5260]
- Line 243: Duplicate range [5257-5260]
- Line 287: Duplicate range [5261-5265]
- Line 331: Duplicate range [5266-5268]

---

### File: dynamic/delusion_final_backup/02-18-13-01.txt

**Errors:**
- Line 838: Duplicate range [5639-5639]
- Line 860: Duplicate range [5639-5639]
- Line 882: Duplicate range [5639-5639]
- Line 904: Duplicate range [5639-5639]
- Line 926: Duplicate range [5639-5639]
- Line 948: Duplicate range [5639-5639]
- Line 970: Duplicate range [5639-5639]
- Line 992: Duplicate range [5639-5639]
- Line 1014: Duplicate range [5639-5639]
- Line 1036: Duplicate range [5639-5639]
- Line 1058: Duplicate range [5639-5639]
- Line 1080: Duplicate range [5639-5639]
- Line 1102: Duplicate range [5639-5639]
- Line 1124: Duplicate range [5639-5639]
- Line 1146: Duplicate range [5639-5639]
- Line 1168: Duplicate range [5639-5639]

---

### File: dynamic/delusion_final_backup/02-18-15-01.txt

**Errors:**
- Line 778: Duplicate range [5731-5732]
- Line 904: Duplicate range [5736-5737]

---

### File: dynamic/delusion_final_backup/02-18-16-04.txt

**Errors:**
- Line 361: Non-sequential range [5941-5942] - Start (5941) < Previous start (5961)
- Line 341: Duplicate range [5961-5962]
- Line 361: Duplicate range [5941-5942]

---

### File: dynamic/delusion_final_backup/02-19-00-01.txt

**Errors:**
- Line 511: Duplicate range [6413-6413]
- Line 533: Duplicate range [6413-6413]
- Line 555: Duplicate range [6413-6413]
- Line 577: Duplicate range [6413-6413]
- Line 599: Duplicate range [6413-6413]
- Line 621: Duplicate range [6413-6413]
- Line 643: Duplicate range [6413-6413]
- Line 665: Duplicate range [6413-6413]

---

### File: dynamic/delusion_final_backup/02-20-02-01.txt

**Errors:**
- Line 202: Non-sequential range [8906-8910] - Start (8906) < Previous start (8933)
- Line 250: Non-sequential range [8920-8925] - Start (8920) < Previous start (8939)
- Line 298: Non-sequential range [8834-8848] - Start (8834) < Previous start (8926)
- Line 394: Non-sequential range [8831-8838] - Start (8831) < Previous start (8926)
- Line 442: Non-sequential range [8834-8848] - Start (8834) < Previous start (8844)
- Line 321: Duplicate range [8911-8938]
- Line 346: Duplicate range [8920-8925]
- Line 442: Duplicate range [8834-8848]

---

### File: dynamic/delusion_final_backup/02-20-04-01.txt

**Errors:**
- Line 22: Duplicate range [8972-8979]

---

### File: dynamic/delusion_final_backup/02-20-05-01.txt

**Errors:**
- Line 85: Duplicate range [9068-9068]
- Line 107: Duplicate range [9068-9068]
- Line 129: Duplicate range [9068-9068]
- Line 151: Duplicate range [9068-9068]
- Line 173: Duplicate range [9068-9068]
- Line 195: Duplicate range [9068-9068]
- Line 217: Duplicate range [9068-9068]
- Line 239: Duplicate range [9068-9068]
- Line 261: Duplicate range [9068-9068]
- Line 283: Duplicate range [9068-9068]
- Line 305: Duplicate range [9068-9068]
- Line 327: Duplicate range [9068-9068]
- Line 349: Duplicate range [9068-9068]
- Line 371: Duplicate range [9068-9068]
- Line 393: Duplicate range [9068-9068]
- Line 415: Duplicate range [9068-9068]
- Line 437: Duplicate range [9068-9068]
- Line 459: Duplicate range [9068-9068]
- Line 481: Duplicate range [9068-9068]
- Line 503: Duplicate range [9068-9068]
- Line 525: Duplicate range [9068-9068]
- Line 547: Duplicate range [9068-9068]
- Line 569: Duplicate range [9068-9068]

---

### File: dynamic/delusion_final_backup/02-20-07-01.txt

**Errors:**
- Line 661: Duplicate range [9140-9142]

---

### File: dynamic/delusion_final_backup/02-20-08-01.txt

**Errors:**
- Line 402: Non-sequential range [9235-9248] - Start (9235) < Previous start (9385)
- Line 442: Non-sequential range [9294-9303] - Start (9294) < Previous start (9327)
- Line 462: Non-sequential range [9278-9314] - Start (9278) < Previous start (9294)
- Line 262: Duplicate range [9315-9341]
- Line 302: Duplicate range [9342-9371]
- Line 362: Duplicate range [9385-9403]
- Line 382: Duplicate range [9385-9403]
- Line 442: Duplicate range [9294-9303]

---

### File: dynamic/delusion_final_backup/02-21-00-01.txt

**Errors:**
- Line 683: Duplicate range [9712-9712]
- Line 705: Duplicate range [9712-9712]
- Line 727: Duplicate range [9712-9712]
- Line 749: Duplicate range [9712-9712]
- Line 771: Duplicate range [9712-9712]
- Line 793: Duplicate range [9712-9712]
- Line 815: Duplicate range [9712-9712]
- Line 837: Duplicate range [9712-9712]
- Line 859: Duplicate range [9712-9712]
- Line 881: Duplicate range [9712-9712]
- Line 903: Duplicate range [9712-9712]
- Line 925: Duplicate range [9712-9712]
- Line 947: Duplicate range [9712-9712]
- Line 969: Duplicate range [9712-9712]
- Line 991: Duplicate range [9712-9712]
- Line 1013: Duplicate range [9712-9712]
- Line 1035: Duplicate range [9712-9712]
- Line 1057: Duplicate range [9712-9712]
- Line 1079: Duplicate range [9712-9712]
- Line 1101: Duplicate range [9712-9712]
- Line 1123: Duplicate range [9712-9712]
- Line 1145: Duplicate range [9712-9712]
- Line 1167: Duplicate range [9712-9712]
- Line 1189: Duplicate range [9712-9712]
- Line 1211: Duplicate range [9712-9712]
- Line 1233: Duplicate range [9712-9712]
- Line 1255: Duplicate range [9712-9712]
- Line 1277: Duplicate range [9712-9712]
- Line 1299: Duplicate range [9712-9712]
- Line 1321: Duplicate range [9712-9712]
- Line 1343: Duplicate range [9712-9712]
- Line 1365: Duplicate range [9712-9712]
- Line 1387: Duplicate range [9712-9712]
- Line 1409: Duplicate range [9712-9712]
- Line 1431: Duplicate range [9712-9712]
- Line 1453: Duplicate range [9712-9712]
- Line 1475: Duplicate range [9712-9712]
- Line 1497: Duplicate range [9712-9712]
- Line 1519: Duplicate range [9712-9712]
- Line 1541: Duplicate range [9712-9712]
- Line 1563: Duplicate range [9712-9712]
- Line 1585: Duplicate range [9712-9712]
- Line 1607: Duplicate range [9712-9712]
- Line 1629: Duplicate range [9712-9712]
- Line 1651: Duplicate range [9712-9712]
- Line 1673: Duplicate range [9712-9712]
- Line 1695: Duplicate range [9712-9712]
- Line 1717: Duplicate range [9712-9712]
- Line 1739: Duplicate range [9712-9712]
- Line 1761: Duplicate range [9712-9712]

---

### File: dynamic/delusion_final_backup/02-21-01-01.txt

**Errors:**
- Line 400: Non-sequential range [9713-10200] - Start (9713) < Previous start (10113)
- Line 20: Duplicate range [9713-9716]
- Line 229: Duplicate range [9781-9796]
- Line 362: Duplicate range [10016-10112]
- Line 419: Duplicate range [9713-10200]
- Line 438: Duplicate range [9713-10200]
- Line 457: Duplicate range [9713-10200]
- Line 476: Duplicate range [9713-10200]
- Line 495: Duplicate range [9713-10200]
- Line 514: Duplicate range [9713-10200]
- Line 533: Duplicate range [9713-10200]
- Line 552: Duplicate range [9713-10200]
- Line 571: Duplicate range [9713-10200]
- Line 590: Duplicate range [9713-10200]
- Line 609: Duplicate range [9713-10200]
- Line 628: Duplicate range [9713-10200]
- Line 647: Duplicate range [9713-10200]
- Line 666: Duplicate range [9713-10200]
- Line 685: Duplicate range [9713-10200]
- Line 704: Duplicate range [9713-10200]
- Line 723: Duplicate range [9713-10200]
- Line 742: Duplicate range [9713-10200]
- Line 761: Duplicate range [9713-10200]
- Line 780: Duplicate range [9713-10200]
- Line 799: Duplicate range [9713-10200]

---

### File: dynamic/delusion_final_backup/02-22-01-01.txt

**Errors:**
- Line 96: Non-sequential range [10238-10254] - Start (10238) < Previous start (10250)
- Line 248: Duplicate range [10284-10304]
- Line 267: Duplicate range [10284-10304]
- Line 404: Duplicate range [10765-10765]
- Line 427: Duplicate range [10765-10765]
- Line 450: Duplicate range [10765-10765]
- Line 473: Duplicate range [10765-10765]
- Line 496: Duplicate range [10765-10765]
- Line 519: Duplicate range [10765-10765]
- Line 542: Duplicate range [10765-10765]
- Line 565: Duplicate range [10765-10765]
- Line 588: Duplicate range [10765-10765]
- Line 611: Duplicate range [10765-10765]
- Line 634: Duplicate range [10765-10765]

---

### File: dynamic/delusion_final_backup/02-22-03-02.txt

**Errors:**
- Line 286: Non-sequential range [10900-11181] - Start (10900) < Previous start (11163)
- Line 134: Duplicate range [10936-10962]
- Line 305: Duplicate range [10900-11181]
- Line 324: Duplicate range [10900-11181]
- Line 343: Duplicate range [10900-11181]
- Line 362: Duplicate range [10900-11181]
- Line 381: Duplicate range [10900-11181]
- Line 400: Duplicate range [10900-11181]
- Line 419: Duplicate range [10900-11181]

---

### File: dynamic/delusion_final_backup/02-22-03-03.txt

**Errors:**
- Line 85: Invalid range [11341-11321] - End < Start

---

### File: dynamic/delusion_final_backup/02-22-04-01.txt

**Errors:**
- Line 766: Non-sequential range [11322-11479] - Start (11322) < Previous start (11476)
- Line 18: Duplicate range [11322-11327]
- Line 52: Duplicate range [11328-11334]
- Line 86: Duplicate range [11335-11341]
- Line 137: Duplicate range [11344-11358]
- Line 171: Duplicate range [11359-11363]
- Line 222: Duplicate range [11371-11378]
- Line 256: Duplicate range [11379-11383]
- Line 290: Duplicate range [11384-11386]
- Line 324: Duplicate range [11387-11389]
- Line 341: Duplicate range [11387-11389]
- Line 375: Duplicate range [11390-11399]
- Line 409: Duplicate range [11400-11405]
- Line 443: Duplicate range [11406-11410]
- Line 477: Duplicate range [11411-11417]
- Line 528: Duplicate range [11422-11431]
- Line 579: Duplicate range [11437-11445]
- Line 613: Duplicate range [11446-11455]
- Line 664: Duplicate range [11468-11475]
- Line 681: Duplicate range [11468-11475]
- Line 698: Duplicate range [11468-11475]
- Line 715: Duplicate range [11468-11475]
- Line 749: Duplicate range [11476-11479]

---

### File: dynamic/delusion_final_backup/02-22-05-01.txt

**Errors:**
- Line 231: Non-sequential range [11480-11480] - Start (11480) < Previous start (11721)
- Line 254: Duplicate range [11480-11480]
- Line 277: Duplicate range [11480-11480]

---

### File: dynamic/delusion_final_backup/02-22-05-02.txt

**Errors:**
- Line 1141: Non-sequential range [11742-11779] - Start (11742) < Previous start (11818)
- Line 1217: Non-sequential range [11736-11823] - Start (11736) < Previous start (11785)

---

### File: dynamic/delusion_final_backup/02-22-06-01.txt

**Errors:**
- Line 442: Invalid range [12003-12002] - End < Start
- Line 22: Duplicate range [11825-11838]
- Line 64: Duplicate range [11838-11847]
- Line 127: Duplicate range [11859-11871]
- Line 232: Duplicate range [11898-11905]
- Line 274: Duplicate range [11906-11922]
- Line 337: Duplicate range [11923-11975]
- Line 379: Duplicate range [11985-11990]
- Line 421: Duplicate range [11991-12002]

---

### File: dynamic/delusion_final_backup/02-23-01-01.txt

**Errors:**
- Line 22: Duplicate range [12011-12022]
- Line 64: Duplicate range [12022-12043]
- Line 295: Duplicate range [12135-12145]
- Line 316: Duplicate range [12135-12145]
- Line 337: Duplicate range [12135-12145]
- Line 358: Duplicate range [12135-12145]
- Line 421: Duplicate range [12148-12154]
- Line 463: Duplicate range [12155-12167]
- Line 589: Duplicate range [12205-12235]
- Line 610: Duplicate range [12205-12235]
- Line 652: Duplicate range [12236-12244]
- Line 673: Duplicate range [12236-12244]
- Line 694: Duplicate range [12236-12244]
- Line 715: Duplicate range [12236-12244]

---

### File: dynamic/delusion_final_backup/02-23-02-01.txt

**Errors:**
- Line 904: Non-sequential range [12278-12320] - Start (12278) < Previous start (12345)
- Line 925: Non-sequential range [12245-12350] - Start (12245) < Previous start (12278)
- Line 1009: Non-sequential range [12245-12258] - Start (12245) < Previous start (12286)
- Line 1114: Non-sequential range [12245-12350] - Start (12245) < Previous start (12315)
- Line 1156: Non-sequential range [12260-12263] - Start (12260) < Previous start (12278)
- Line 1324: Non-sequential range [12245-12350] - Start (12245) < Previous start (12300)
- Line 1513: Non-sequential range [12245-12350] - Start (12245) < Previous start (12344)
- Line 1051: Duplicate range [12306-12307]
- Line 1072: Duplicate range [12308-12314]
- Line 1093: Duplicate range [12315-12320]
- Line 1114: Duplicate range [12245-12350]
- Line 1156: Duplicate range [12260-12263]
- Line 1177: Duplicate range [12271-12276]
- Line 1198: Duplicate range [12283-12284]
- Line 1219: Duplicate range [12290-12292]
- Line 1240: Duplicate range [12293-12296]
- Line 1282: Duplicate range [12297-12299]
- Line 1324: Duplicate range [12245-12350]
- Line 1345: Duplicate range [12245-12258]
- Line 1387: Duplicate range [12278-12279]
- Line 1408: Duplicate range [12280-12299]
- Line 1450: Duplicate range [12338-12340]
- Line 1492: Duplicate range [12344-12350]
- Line 1513: Duplicate range [12245-12350]
- Line 1534: Duplicate range [12245-12350]
- Line 1555: Duplicate range [12245-12350]

---

### File: dynamic/delusion_final_backup/02-23-02-02.txt

**Errors:**
- Line 22: Duplicate range [12351-12362]
- Line 64: Duplicate range [12363-12411]
- Line 232: Duplicate range [12461-12494]
- Line 274: Duplicate range [12495-12504]

---

### File: dynamic/delusion_final_backup/02-23-03-01.txt

**Errors:**
- Line 22: Duplicate range [12522-12540]
- Line 43: Duplicate range [12522-12540]
- Line 85: Duplicate range [12541-12605]
- Line 106: Duplicate range [12541-12605]
- Line 127: Duplicate range [12541-12605]
- Line 169: Duplicate range [12606-12663]
- Line 211: Duplicate range [12664-12688]
- Line 232: Duplicate range [12664-12688]
- Line 274: Duplicate range [12689-12709]
- Line 295: Duplicate range [12689-12709]
- Line 358: Duplicate range [12718-12736]
- Line 400: Duplicate range [12737-12754]

---

### File: dynamic/delusion_final_backup/02-23-03-02.txt

**Errors:**
- Line 20: Duplicate range [12779-12780]
- Line 362: Duplicate range [12876-12878]

---

### File: dynamic/delusion_final_backup/02-23-04-01.txt

**Errors:**
- Line 22: Duplicate range [13304-13308]
- Line 43: Duplicate range [13304-13308]
- Line 127: Duplicate range [13307-13308]
- Line 190: Duplicate range [13309-13317]
- Line 232: Duplicate range [13318-13336]
- Line 337: Duplicate range [13437-13493]
- Line 442: Duplicate range [13614-13693]

---

### File: dynamic/delusion_final_backup/02-23-06-01.txt

**Errors:**
- Line 22: Duplicate range [13701-13705]

---

### File: dynamic/delusion_final_backup/02-23-06-02.txt

**Errors:**
- Line 358: Non-sequential range [14200-14206] - Start (14200) < Previous start (14277)
- Line 392: Duplicate range [14207-14214]
- Line 460: Duplicate range [14222-14224]
- Line 579: Duplicate range [14239-14242]
- Line 613: Duplicate range [14242-14243]
- Line 715: Duplicate range [14248-14251]
- Line 732: Duplicate range [14249-14252]
- Line 766: Duplicate range [14252-14255]
- Line 800: Duplicate range [14255-14256]
- Line 817: Duplicate range [14256-14258]
- Line 851: Duplicate range [14258-14259]
- Line 868: Duplicate range [14267-14269]
- Line 953: Duplicate range [14276-14277]
- Line 970: Duplicate range [14277-14277]

---

### File: dynamic/delusion_final_backup/02-23-08-03.txt

**Errors:**
- Line 241: Duplicate range [14639-14639]
- Line 261: Duplicate range [14639-14639]
- Line 281: Duplicate range [14639-14639]

---

### File: dynamic/delusion_final_backup/02-23-08-05.txt

**Errors:**
- Line 101: Non-sequential range [14642-14650] - Start (14642) < Previous start (14738)
- Line 181: Duplicate range [14720-14737]

---

### File: dynamic/delusion_final_backup/02-23-08-09.txt

**Errors:**
- Line 101: Non-sequential range [14753-14765] - Start (14753) < Previous start (14810)

---

### File: dynamic/delusion_final_backup/02-24-01-01.txt

**Errors:**
- Line 20: Duplicate range [15275-15277]

---

### File: dynamic/delusion_final_backup/02-25-02-01.txt

**Errors:**
- Line 23: Duplicate range [16329-16344]
- Line 45: Duplicate range [16329-16344]
- Line 67: Duplicate range [16329-16344]
- Line 89: Duplicate range [16329-16344]
- Line 133: Duplicate range [16343-16344]
- Line 177: Duplicate range [16344-16351]
- Line 199: Duplicate range [16344-16351]
- Line 221: Duplicate range [16344-16351]
- Line 287: Duplicate range [16352-16358]
- Line 309: Duplicate range [16352-16358]
- Line 331: Duplicate range [16352-16358]
- Line 353: Duplicate range [16352-16358]

---

### File: dynamic/delusion_final_backup/02-25-03-01.txt

**Errors:**
- Line 61: Non-sequential range [16360-16370] - Start (16360) < Previous start (16395)

---

### File: dynamic/delusion_final_backup/02-25-04-01.txt

**Errors:**
- Line 63: Duplicate range [16435-16435]
- Line 85: Duplicate range [16435-16435]
- Line 107: Duplicate range [16435-16435]
- Line 129: Duplicate range [16435-16435]
- Line 151: Duplicate range [16435-16435]
- Line 173: Duplicate range [16435-16435]
- Line 195: Duplicate range [16435-16435]
- Line 217: Duplicate range [16435-16435]
- Line 239: Duplicate range [16435-16435]
- Line 261: Duplicate range [16435-16435]
- Line 283: Duplicate range [16435-16435]
- Line 305: Duplicate range [16435-16435]
- Line 327: Duplicate range [16435-16435]
- Line 349: Duplicate range [16435-16435]
- Line 371: Duplicate range [16435-16435]
- Line 393: Duplicate range [16435-16435]
- Line 415: Duplicate range [16435-16435]
- Line 437: Duplicate range [16435-16435]
- Line 459: Duplicate range [16435-16435]
- Line 481: Duplicate range [16435-16435]
- Line 503: Duplicate range [16435-16435]
- Line 525: Duplicate range [16435-16435]
- Line 547: Duplicate range [16435-16435]

---

### File: dynamic/delusion_final_backup/02-25-06-01.txt

**Errors:**
- Line 61: Non-sequential range [16719-16728] - Start (16719) < Previous start (16750)
- Line 101: Duplicate range [16750-16769]

---

### File: dynamic/delusion_final_backup/02-25-06-02.txt

**Errors:**
- Line 161: Non-sequential range [16840-16855] - Start (16840) < Previous start (16864)

---

### File: dynamic/delusion_final_backup/02-25-07-01.txt

**Errors:**
- Line 381: Non-sequential range [17240-17318] - Start (17240) < Previous start (17319)
- Line 438: Invalid range [17333-17330] - End < Start
- Line 457: Non-sequential range [17258-17330] - Start (17258) < Previous start (17333)
- Line 476: Non-sequential range [17242-17330] - Start (17242) < Previous start (17258)
- Line 514: Non-sequential range [17111-17330] - Start (17111) < Previous start (17328)
- Line 571: Non-sequential range [17142-17330] - Start (17142) < Previous start (17320)
- Line 609: Invalid range [17343-17330] - End < Start
- Line 628: Non-sequential range [16972-17330] - Start (16972) < Previous start (17343)
- Line 780: Non-sequential range [17285-17330] - Start (17285) < Previous start (17305)
- Line 799: Non-sequential range [16972-17330] - Start (16972) < Previous start (17285)
- Line 856: Non-sequential range [17230-17330] - Start (17230) < Previous start (17306)
- Line 970: Non-sequential range [16972-17330] - Start (16972) < Previous start (17328)
- Line 495: Duplicate range [17328-17330]
- Line 533: Duplicate range [17319-17330]
- Line 647: Duplicate range [16972-17330]
- Line 666: Duplicate range [17034-17046]
- Line 799: Duplicate range [16972-17330]
- Line 913: Duplicate range [17285-17330]
- Line 932: Duplicate range [17328-17330]
- Line 951: Duplicate range [17328-17330]
- Line 970: Duplicate range [16972-17330]
- Line 989: Duplicate range [16972-17330]
- Line 1008: Duplicate range [16972-17330]
- Line 1027: Duplicate range [16972-17330]
- Line 1046: Duplicate range [16972-17330]
- Line 1065: Duplicate range [16972-17330]
- Line 1084: Duplicate range [16972-17330]
- Line 1103: Duplicate range [16972-17330]
- Line 1122: Duplicate range [16972-17330]

---

### File: dynamic/delusion_oob_backup/02-16-03-01.txt

**Errors:**
- Line 248: Non-sequential range [1182-1700] - Start (1182) < Previous start (1601)
- Line 20: Duplicate range [1182-1203]
- Line 267: Duplicate range [1182-1700]
- Line 286: Duplicate range [1182-1700]
- Line 305: Duplicate range [1182-1700]
- Line 324: Duplicate range [1182-1700]
- Line 343: Duplicate range [1182-1700]
- Line 362: Duplicate range [1182-1700]
- Line 381: Duplicate range [1182-1700]
- Line 400: Duplicate range [1182-1700]
- Line 419: Duplicate range [1182-1700]
- Line 438: Duplicate range [1182-1700]

---

### File: dynamic/delusion_oob_backup/02-18-06-01.txt

**Errors:**
- Line 22: Duplicate range [4696-4704]
- Line 148: Duplicate range [4715-4717]
- Line 379: Duplicate range [4728-4731]
- Line 484: Duplicate range [4735-4736]
- Line 505: Duplicate range [4735-4736]
- Line 736: Duplicate range [4746-4747]

---

### File: dynamic/delusion_oob_backup/02-18-16-04.txt

**Errors:**
- Line 361: Non-sequential range [5941-5942] - Start (5941) < Previous start (5961)
- Line 341: Duplicate range [5961-5964]
- Line 361: Duplicate range [5941-5942]

---

### File: dynamic/delusion_oob_backup/02-22-01-01.txt

**Errors:**
- Line 96: Non-sequential range [10238-10254] - Start (10238) < Previous start (10250)
- Line 248: Duplicate range [10284-10304]
- Line 267: Duplicate range [10284-10304]

---

### File: dynamic/delusion_oob_backup/02-22-03-02.txt

**Errors:**
- Line 286: Non-sequential range [10900-11181] - Start (10900) < Previous start (11163)
- Line 134: Duplicate range [10936-10962]
- Line 305: Duplicate range [10900-11181]
- Line 324: Duplicate range [10900-11181]
- Line 343: Duplicate range [10900-11181]
- Line 362: Duplicate range [10900-11181]
- Line 381: Duplicate range [10900-11181]
- Line 400: Duplicate range [10900-11181]
- Line 419: Duplicate range [10900-11181]

---

### File: dynamic/delusion_oob_backup/02-22-06-01.txt

**Errors:**
- Line 22: Duplicate range [11825-11838]
- Line 64: Duplicate range [11838-11847]
- Line 127: Duplicate range [11859-11871]
- Line 232: Duplicate range [11898-11905]
- Line 274: Duplicate range [11906-11922]
- Line 337: Duplicate range [11923-11975]
- Line 379: Duplicate range [11985-11990]
- Line 421: Duplicate range [11991-12002]

---

### File: dynamic/delusion_oob_backup/02-23-06-01.txt

**Errors:**
- Line 22: Duplicate range [13701-13705]

---

### File: dynamic/delusion_oob_backup/02-23-06-02.txt

**Errors:**
- Line 358: Non-sequential range [14200-14206] - Start (14200) < Previous start (14277)
- Line 392: Duplicate range [14207-14214]
- Line 460: Duplicate range [14222-14224]
- Line 579: Duplicate range [14239-14242]
- Line 613: Duplicate range [14242-14243]
- Line 715: Duplicate range [14248-14251]
- Line 732: Duplicate range [14249-14252]
- Line 766: Duplicate range [14252-14255]
- Line 800: Duplicate range [14255-14256]
- Line 817: Duplicate range [14256-14258]
- Line 851: Duplicate range [14258-14259]
- Line 868: Duplicate range [14267-14269]
- Line 953: Duplicate range [14276-14277]
- Line 970: Duplicate range [14277-14279]

---

### File: dynamic/delusion_oob_backup/02-23-08-03.txt

**Errors:**
- Line 261: Non-sequential range [14639-14642] - Start (14639) < Previous start (14649)

---

### File: dynamic/delusion_oob_backup/02-25-07-01.txt

**Errors:**
- Line 381: Non-sequential range [17240-17318] - Start (17240) < Previous start (17319)
- Line 457: Non-sequential range [17258-17342] - Start (17258) < Previous start (17333)
- Line 476: Non-sequential range [17242-17342] - Start (17242) < Previous start (17258)
- Line 514: Non-sequential range [17111-17342] - Start (17111) < Previous start (17328)
- Line 571: Non-sequential range [17142-17342] - Start (17142) < Previous start (17320)
- Line 628: Non-sequential range [16972-17358] - Start (16972) < Previous start (17343)
- Line 780: Non-sequential range [17285-17342] - Start (17285) < Previous start (17305)
- Line 799: Non-sequential range [16972-17358] - Start (16972) < Previous start (17285)
- Line 856: Non-sequential range [17230-17342] - Start (17230) < Previous start (17306)
- Line 970: Non-sequential range [16972-17358] - Start (16972) < Previous start (17328)
- Line 647: Duplicate range [16972-17358]
- Line 666: Duplicate range [17034-17046]
- Line 799: Duplicate range [16972-17358]
- Line 913: Duplicate range [17285-17342]
- Line 932: Duplicate range [17328-17342]
- Line 970: Duplicate range [16972-17358]
- Line 989: Duplicate range [16972-17358]
- Line 1008: Duplicate range [16972-17358]
- Line 1027: Duplicate range [16972-17358]
- Line 1046: Duplicate range [16972-17358]
- Line 1065: Duplicate range [16972-17358]
- Line 1084: Duplicate range [16972-17358]
- Line 1103: Duplicate range [16972-17358]
- Line 1122: Duplicate range [16972-17358]

---

### File: dynamic/scholar/01-01-01-01.txt

**Errors:**
- Line 9: Duplicate range [1-4]
- Line 34: Duplicate range [5-11]
- Line 71: Duplicate range [16-19]
- Line 87: Duplicate range [16-19]
- Line 114: Duplicate range [20-27]
- Line 135: Duplicate range [20-27]
- Line 156: Duplicate range [28-40]
- Line 173: Duplicate range [28-40]
- Line 200: Duplicate range [41-45]
- Line 214: Duplicate range [41-45]
- Line 245: Duplicate range [46-58]
- Line 261: Duplicate range [46-58]
- Line 287: Duplicate range [59-64]
- Line 302: Duplicate range [59-64]
- Line 311: Duplicate range [59-64]
- Line 331: Duplicate range [65-71]
- Line 345: Duplicate range [65-71]
- Line 369: Duplicate range [72-75]
- Line 383: Duplicate range [72-75]
- Line 405: Duplicate range [76-87]
- Line 423: Duplicate range [76-87]
- Line 443: Duplicate range [88-98]
- Line 460: Duplicate range [88-98]
- Line 482: Duplicate range [99-109]
- Line 492: Duplicate range [99-109]
- Line 512: Duplicate range [110-114]
- Line 525: Duplicate range [110-114]
- Line 542: Duplicate range [115-125]
- Line 558: Duplicate range [115-125]
- Line 574: Duplicate range [126-138]
- Line 588: Duplicate range [126-138]
- Line 609: Duplicate range [139-161]
- Line 625: Duplicate range [139-161]
- Line 650: Duplicate range [162-174]
- Line 671: Duplicate range [162-174]
- Line 691: Duplicate range [162-174]

---

### File: dynamic/scholar/01-01-02-01.txt

**Errors:**
- Line 37: Duplicate range [175-191]
- Line 64: Duplicate range [175-191]
- Line 119: Duplicate range [192-229]
- Line 148: Duplicate range [192-229]
- Line 165: Duplicate range [192-229]
- Line 208: Duplicate range [230-257]
- Line 235: Duplicate range [230-257]
- Line 262: Duplicate range [230-257]
- Line 313: Duplicate range [258-365]
- Line 343: Duplicate range [258-365]
- Line 361: Duplicate range [258-365]
- Line 435: Duplicate range [366-403]
- Line 472: Duplicate range [366-403]
- Line 506: Duplicate range [366-403]
- Line 552: Duplicate range [366-403]
- Line 579: Duplicate range [366-403]
- Line 614: Duplicate range [366-403]
- Line 643: Duplicate range [366-403]

---

### File: dynamic/scholar/01-02-01-03.txt

**Errors:**
- Line 4: Duplicate range [997-997]
- Line 10: Duplicate range [997-997]
- Line 13: Duplicate range [997-997]

---

### File: dynamic/scholar/01-02-01-04.txt

**Errors:**
- Line 4: Duplicate range [998-998]
- Line 10: Duplicate range [998-998]
- Line 13: Duplicate range [998-998]

---

### File: dynamic/scholar/01-02-01-05.txt

**Errors:**
- Line 47: Duplicate range [999-1041]
- Line 114: Duplicate range [999-1041]
- Line 190: Duplicate range [999-1041]
- Line 386: Duplicate range [1042-1098]
- Line 421: Duplicate range [1042-1098]
- Line 467: Duplicate range [1042-1098]
- Line 585: Duplicate range [1295-1370]
- Line 695: Duplicate range [1295-1423]

---

### File: dynamic/scholar/01-02-02-01.txt

**Errors:**
- Line 74: Duplicate range [1447-1455]
- Line 78: Duplicate range [1447-1455]
- Line 96: Duplicate range [1451-1453]
- Line 141: Duplicate range [1455-1459]
- Line 156: Duplicate range [1456-1462]

---

### File: dynamic/scholar/01-02-02-02.txt

**Errors:**
- Line 5: Duplicate range [1463-1478]
- Line 28: Duplicate range [1479-1495]
- Line 42: Duplicate range [1496-1512]
- Line 50: Duplicate range [1496-1512]
- Line 72: Duplicate range [1513-1528]
- Line 82: Duplicate range [1513-1528]
- Line 101: Duplicate range [1529-1538]
- Line 111: Duplicate range [1529-1538]
- Line 120: Duplicate range [1529-1538]
- Line 148: Duplicate range [1532-1541]
- Line 152: Duplicate range [1532-1541]
- Line 172: Duplicate range [1539-1541]
- Line 176: Duplicate range [1539-1541]
- Line 186: Duplicate range [1539-1541]
- Line 190: Duplicate range [1539-1541]
- Line 200: Duplicate range [1539-1541]
- Line 204: Duplicate range [1539-1541]
- Line 214: Duplicate range [1539-1541]

---

### File: dynamic/scholar/01-04-01-01.txt

**Errors:**
- Line 891: Non-sequential range [2052-2101] - Start (2052) < Previous start (2099)
- Line 24: Duplicate range [1902-1909]
- Line 57: Duplicate range [1902-1909]
- Line 88: Duplicate range [1902-1909]
- Line 149: Duplicate range [1910-1942]
- Line 200: Duplicate range [1910-1942]
- Line 247: Duplicate range [1910-1942]
- Line 335: Duplicate range [1943-2032]
- Line 384: Duplicate range [1943-2032]
- Line 443: Duplicate range [1943-2032]
- Line 568: Duplicate range [2033-2098]
- Line 620: Duplicate range [2033-2098]
- Line 665: Duplicate range [2033-2098]
- Line 749: Duplicate range [2099-2200]
- Line 772: Duplicate range [2099-2200]
- Line 801: Duplicate range [2099-2200]
- Line 934: Duplicate range [2052-2101]
- Line 982: Duplicate range [2052-2101]
- Line 1033: Duplicate range [2052-2101]
- Line 1118: Duplicate range [2102-2200]
- Line 1161: Duplicate range [2102-2200]
- Line 1206: Duplicate range [2102-2200]
- Line 1388: Duplicate range [2201-2400]
- Line 1430: Duplicate range [2201-2400]
- Line 1483: Duplicate range [2201-2400]

---

### File: dynamic/scholar/01-04-02-01.txt

**Errors:**
- Line 448: Duplicate range [2831-2832]

---

### File: dynamic/scholar/01-04-03-01.txt

**Errors:**
- Line 25: Duplicate range [2833-2833]
- Line 38: Duplicate range [2833-2833]
- Line 54: Duplicate range [2833-2833]
- Line 58: Duplicate range [2833-2833]
- Line 67: Duplicate range [2833-2833]
- Line 81: Duplicate range [2833-2833]
- Line 93: Duplicate range [2833-2833]

---

### File: dynamic/scholar/01-04-04-01.txt

**Errors:**
- Line 29: Duplicate range [2836-2848]
- Line 86: Duplicate range [2836-2848]
- Line 134: Duplicate range [2836-2848]

---

### File: dynamic/scholar/01-04-05-01.txt

**Errors:**
- Line 36: Duplicate range [2849-2872]
- Line 141: Duplicate range [2849-2849]

---

### File: dynamic/scholar/01-04-06-01.txt

**Errors:**
- Line 65: Duplicate range [2873-2902]

---

### File: dynamic/scholar/01-04-07-01.txt

**Errors:**
- Line 5: Duplicate range [2983-2984]

---

### File: dynamic/scholar/01-04-08-01.txt

**Errors:**
- Line 191: Non-sequential range [2989-2989] - Start (2989) < Previous start (3016)
- Line 100: Duplicate range [3000-3016]
- Line 128: Duplicate range [3000-3016]

---

### File: dynamic/scholar/01-04-09-01.txt

**Errors:**
- Line 24: Non-sequential range [3017-3035] - Start (3017) < Previous start (3035)
- Line 24: Duplicate range [3017-3035]
- Line 39: Duplicate range [3017-3035]
- Line 46: Duplicate range [3017-3035]

---

### File: dynamic/scholar/01-04-10-01.txt

**Errors:**
- Line 12: Duplicate range [3037-3039]
- Line 37: Duplicate range [3037-3039]
- Line 49: Duplicate range [3037-3039]

---

### File: dynamic/scholar/01-04-11-01.txt

**Errors:**
- Line 28: Non-sequential range [3040-3061] - Start (3040) < Previous start (3057)
- Line 12: Duplicate range [3040-3053]
- Line 42: Duplicate range [3040-3061]
- Line 52: Duplicate range [3040-3061]

---

### File: dynamic/scholar/01-04-12-01.txt

**Errors:**
- Line 38: Duplicate range [3062-3086]
- Line 70: Duplicate range [3062-3062]
- Line 86: Duplicate range [3062-3062]
- Line 89: Duplicate range [3062-3062]
- Line 99: Duplicate range [3062-3062]
- Line 116: Duplicate range [3064-3067]
- Line 119: Duplicate range [3064-3067]
- Line 140: Duplicate range [3068-3076]
- Line 153: Duplicate range [3068-3076]
- Line 175: Duplicate range [3077-3086]
- Line 178: Duplicate range [3077-3086]
- Line 233: Duplicate range [3081-3086]
- Line 272: Duplicate range [3087-3092]
- Line 277: Duplicate range [3087-3092]
- Line 298: Duplicate range [3093-3102]
- Line 311: Duplicate range [3093-3102]
- Line 334: Duplicate range [3103-3113]
- Line 337: Duplicate range [3103-3113]
- Line 356: Duplicate range [3114-3117]
- Line 361: Duplicate range [3114-3117]
- Line 422: Duplicate range [3126-3130]
- Line 490: Duplicate range [3132-3134]
- Line 547: Duplicate range [3137-3140]
- Line 580: Duplicate range [3141-3142]
- Line 602: Duplicate range [3143-3146]
- Line 625: Duplicate range [3148-3158]
- Line 632: Duplicate range [3148-3158]
- Line 665: Duplicate range [3159-3165]
- Line 702: Duplicate range [3159-3165]
- Line 1071: Duplicate range [3285-3286]
- Line 1093: Duplicate range [3287-3310]
- Line 1114: Duplicate range [3294-3299]
- Line 1131: Duplicate range [3301-3304]
- Line 1149: Duplicate range [3311-3312]

---

### File: dynamic/scholar/01-04-13-01.txt

**Errors:**
- Line 26: Duplicate range [3313-3316]
- Line 69: Duplicate range [3318-3319]
- Line 85: Duplicate range [3322-3327]
- Line 106: Duplicate range [3323-3324]
- Line 131: Duplicate range [3328-3334]
- Line 147: Duplicate range [3331-3334]
- Line 165: Duplicate range [3335-3340]
- Line 169: Duplicate range [3335-3336]
- Line 186: Duplicate range [3338-3340]

---

### File: dynamic/scholar/01-04-14-01.txt

**Errors:**
- Line 14: Duplicate range [3341-3343]
- Line 18: Duplicate range [3341-3342]
- Line 43: Duplicate range [3344-3351]
- Line 470: Duplicate range [3493-3517]
- Line 476: Duplicate range [3493-3495]
- Line 495: Duplicate range [3496-3501]
- Line 516: Duplicate range [3502-3507]
- Line 538: Duplicate range [3508-3512]
- Line 567: Duplicate range [3513-3517]
- Line 574: Duplicate range [3513-3517]
- Line 620: Duplicate range [3519-3520]
- Line 641: Duplicate range [3521-3522]
- Line 666: Duplicate range [3524-3525]
- Line 700: Duplicate range [3529-3533]
- Line 706: Duplicate range [3529-3530]
- Line 724: Duplicate range [3531-3532]
- Line 748: Duplicate range [3534-3538]
- Line 766: Duplicate range [3537-3538]

---

### File: dynamic/scholar/01-04-15-01.txt

**Errors:**
- Line 5: Duplicate range [3721-3730]
- Line 22: Duplicate range [3721-3730]
- Line 172: Duplicate range [3761-3765]

---

### File: dynamic/scholar/01-04-17-01.txt

**Errors:**
- Line 5: Duplicate range [3870-3882]
- Line 22: Duplicate range [3870-3882]
- Line 28: Duplicate range [3870-3882]
- Line 46: Duplicate range [3870-3882]
- Line 98: Duplicate range [3877-3882]

---

### File: dynamic/scholar/01-04-18-01.txt

**Errors:**
- Line 15: Duplicate range [3888-3889]
- Line 57: Duplicate range [3888-3892]
- Line 67: Duplicate range [3888-3892]
- Line 76: Duplicate range [3888-3892]

---

### File: dynamic/scholar/01-04-18-02.txt

**Errors:**
- Line 293: Non-sequential range [3893-3893] - Start (3893) < Previous start (3990)
- Line 261: Duplicate range [3984-3993]

---

### File: dynamic/scholar/01-04-19-01.txt

**Errors:**
- Line 307: Non-sequential range [4101-4118] - Start (4101) < Previous start (4118)
- Line 29: Duplicate range [4005-4028]

---

### File: dynamic/scholar/01-05-01-01.txt

**Errors:**
- Line 219: Duplicate range [4172-4210]

---

### File: dynamic/scholar/01-05-02-01.txt

**Errors:**
- Line 71: Duplicate range [4319-4327]
- Line 221: Duplicate range [4367-4370]
- Line 240: Duplicate range [4371-4376]
- Line 384: Duplicate range [4407-4416]
- Line 391: Duplicate range [4407-4409]
- Line 410: Duplicate range [4410-4412]
- Line 434: Duplicate range [4413-4416]
- Line 605: Duplicate range [4491-4501]
- Line 648: Duplicate range [4502-4518]
- Line 709: Duplicate range [4519-4541]
- Line 716: Duplicate range [4519-4525]
- Line 764: Duplicate range [4528-4541]
- Line 771: Duplicate range [4528-4541]

---

### File: dynamic/scholar/01-05-03-01.txt

**Errors:**
- Line 364: Duplicate range [4728-4758]
- Line 385: Duplicate range [4729-4730]
- Line 430: Duplicate range [4733-4734]
- Line 446: Duplicate range [4735-4738]
- Line 675: Duplicate range [4847-4847]

---

### File: dynamic/scholar/01-05-04-01.txt

**Errors:**
- Line 45: Duplicate range [4856-4873]
- Line 79: Duplicate range [4874-4878]
- Line 100: Duplicate range [4879-4884]
- Line 177: Duplicate range [4885-4952]
- Line 358: Duplicate range [4992-4994]
- Line 596: Duplicate range [5166-5176]
- Line 610: Duplicate range [5172-5176]
- Line 690: Duplicate range [5207-5227]
- Line 698: Duplicate range [5207-5227]
- Line 795: Duplicate range [5298-5306]
- Line 1017: Duplicate range [5388-5395]
- Line 1041: Duplicate range [5396-5405]
- Line 1266: Duplicate range [5491-5493]
- Line 1285: Duplicate range [5505-5506]
- Line 1303: Duplicate range [5508-5512]
- Line 1320: Duplicate range [5508-5512]
- Line 1365: Duplicate range [5513-5520]
- Line 1400: Duplicate range [5521-5538]
- Line 1419: Duplicate range [5525-5528]
- Line 1443: Duplicate range [5529-5532]
- Line 1460: Duplicate range [5533-5584]
- Line 1475: Duplicate range [5535-5538]
- Line 1522: Duplicate range [5551-5584]
- Line 1528: Duplicate range [5551-5584]
- Line 1545: Duplicate range [5556-5563]
- Line 1555: Duplicate range [5556-5563]
- Line 1585: Duplicate range [5570-5573]
- Line 1623: Duplicate range [5585-5625]
- Line 1632: Duplicate range [5585-5593]
- Line 1643: Duplicate range [5585-5593]
- Line 1649: Duplicate range [5585-5593]
- Line 1661: Duplicate range [5585-5625]
- Line 1682: Duplicate range [5596-5607]
- Line 1692: Duplicate range [5596-5607]
- Line 1741: Duplicate range [5609-5618]
- Line 1752: Duplicate range [5609-5618]
- Line 1782: Duplicate range [5619-5622]
- Line 1807: Duplicate range [5622-5625]
- Line 2124: Duplicate range [5808-5851]
- Line 2204: Duplicate range [5824-5831]
- Line 2626: Duplicate range [6181-6196]
- Line 2644: Duplicate range [6197-6281]
- Line 2656: Duplicate range [6198-6201]
- Line 2670: Duplicate range [6202-6216]
- Line 2698: Duplicate range [6221-6235]
- Line 2717: Duplicate range [6236-6254]
- Line 2736: Duplicate range [6243-6254]
- Line 2750: Duplicate range [6255-6267]
- Line 2766: Duplicate range [6259-6267]
- Line 2780: Duplicate range [6268-6281]
- Line 2799: Duplicate range [6282-6295]
- Line 2814: Duplicate range [6282-6284]
- Line 2826: Duplicate range [6282-6284]
- Line 2832: Duplicate range [6282-6284]
- Line 2862: Duplicate range [6286-6291]
- Line 2868: Duplicate range [6286-6291]
- Line 2880: Duplicate range [6290-6291]
- Line 2886: Duplicate range [6290-6291]
- Line 2896: Duplicate range [6292-6295]
- Line 2900: Duplicate range [6292-6295]
- Line 2918: Duplicate range [6296-6341]
- Line 2924: Duplicate range [6296-6304]
- Line 2930: Duplicate range [6296-6304]
- Line 2952: Duplicate range [6299-6341]
- Line 2968: Duplicate range [6299-6341]

---

### File: dynamic/scholar/01-05-04-06.txt

**Errors:**
- Line 127: Non-sequential range [6424-6511] - Start (6424) < Previous start (6758)
- Line 123: Duplicate range [6758-6758]
- Line 166: Duplicate range [6424-6511]
- Line 185: Duplicate range [6424-6511]
- Line 205: Duplicate range [6424-6511]
- Line 351: Duplicate range [6512-6628]
- Line 368: Duplicate range [6512-6628]
- Line 400: Duplicate range [6512-6628]

---

### File: dynamic/scholar/01-05-05-01.txt

**Errors:**
- Line 84: Duplicate range [6769-6800]

---

### File: dynamic/scholar/01-06-01-01.txt

**Errors:**
- Line 26: Duplicate range [6801-6830]
- Line 110: Duplicate range [6846-6898]
- Line 210: Duplicate range [6900-6911]
- Line 524: Duplicate range [7040-7057]

---

### File: dynamic/scholar/01-06-02-01.txt

**Errors:**
- Line 405: Duplicate range [7314-7363]
- Line 810: Duplicate range [7564-7614]
- Line 1517: Duplicate range [8065-8111]

---

### File: dynamic/scholar/01-06-04-01.txt

**Errors:**
- Line 443: Non-sequential range [8362-8397] - Start (8362) < Previous start (8368)
- Line 935: Non-sequential range [8553-8572] - Start (8553) < Previous start (8625)
- Line 1018: Non-sequential range [8573-8592] - Start (8573) < Previous start (8625)
- Line 1110: Non-sequential range [8603-8628] - Start (8603) < Previous start (8625)
- Line 1300: Non-sequential range [8615-8638] - Start (8615) < Previous start (8629)
- Line 4: Duplicate range [8138-8169]
- Line 15: Duplicate range [8138-8169]
- Line 65: Duplicate range [8170-8217]
- Line 125: Duplicate range [8218-8279]
- Line 209: Duplicate range [8280-8322]
- Line 675: Duplicate range [8493-8518]
- Line 774: Duplicate range [8499-8518]
- Line 807: Duplicate range [8519-8546]
- Line 818: Duplicate range [8519-8546]
- Line 907: Duplicate range [8625-8650]
- Line 917: Duplicate range [8625-8650]
- Line 979: Duplicate range [8625-8650]
- Line 990: Duplicate range [8625-8650]
- Line 1005: Duplicate range [8625-8650]
- Line 1062: Duplicate range [8593-8616]
- Line 1073: Duplicate range [8625-8650]
- Line 1084: Duplicate range [8625-8650]
- Line 1097: Duplicate range [8625-8650]
- Line 1231: Duplicate range [8625-8650]
- Line 1246: Duplicate range [8625-8650]
- Line 1257: Duplicate range [8625-8650]
- Line 1272: Duplicate range [8625-8650]
- Line 1314: Duplicate range [8615-8638]
- Line 1338: Duplicate range [8617-8642]
- Line 1359: Duplicate range [8625-8650]
- Line 1369: Duplicate range [8625-8650]
- Line 1383: Duplicate range [8625-8650]
- Line 1393: Duplicate range [8625-8650]
- Line 1477: Duplicate range [8639-8668]
- Line 1533: Duplicate range [8651-8671]
- Line 1543: Duplicate range [8651-8671]
- Line 1553: Duplicate range [8651-8671]
- Line 1564: Duplicate range [8651-8671]
- Line 1609: Duplicate range [8669-8671]
- Line 1619: Duplicate range [8669-8671]
- Line 1632: Duplicate range [8669-8671]
- Line 1651: Duplicate range [8669-8671]
- Line 1656: Duplicate range [8669-8671]

---

### File: dynamic/scholar/01-06-05-01.txt

**Errors:**
- Line 7: Duplicate range [8672-8673]
- Line 25: Duplicate range [8672-8673]
- Line 41: Duplicate range [8672-8673]

---

### File: dynamic/scholar/01-06-05-05.txt

**Errors:**
- Line 20: Duplicate range [8677-8679]
- Line 33: Duplicate range [8677-8679]
- Line 56: Duplicate range [8677-8679]
- Line 85: Duplicate range [8677-8679]

---

### File: dynamic/scholar/01-06-06-01.txt

**Errors:**
- Line 14: Duplicate range [8680-8686]
- Line 36: Duplicate range [8680-8686]
- Line 47: Duplicate range [8680-8686]

---

### File: dynamic/scholar/01-06-07-01.txt

**Errors:**
- Line 165: Non-sequential range [8695-8702] - Start (8695) < Previous start (8700)
- Line 72: Duplicate range [8687-8696]
- Line 82: Duplicate range [8687-8696]
- Line 95: Duplicate range [8687-8696]
- Line 114: Duplicate range [8687-8696]
- Line 125: Duplicate range [8687-8696]
- Line 178: Duplicate range [8695-8702]
- Line 188: Duplicate range [8695-8702]
- Line 208: Duplicate range [8695-8702]
- Line 276: Duplicate range [8712-8723]
- Line 281: Duplicate range [8712-8723]
- Line 315: Duplicate range [8712-8722]
- Line 329: Duplicate range [8712-8723]
- Line 368: Duplicate range [8718-8723]
- Line 387: Duplicate range [8718-8723]
- Line 398: Duplicate range [8718-8723]
- Line 460: Duplicate range [8723-8723]
- Line 475: Duplicate range [8723-8723]
- Line 487: Duplicate range [8723-8723]

---

### File: dynamic/scholar/01-06-07-03.txt

**Errors:**
- Line 25: Duplicate range [8725-8755]
- Line 77: Duplicate range [8725-8728]
- Line 96: Duplicate range [8725-8728]
- Line 107: Duplicate range [8725-8728]
- Line 141: Duplicate range [8725-8728]
- Line 161: Duplicate range [8725-8748]
- Line 205: Duplicate range [8725-8726]
- Line 225: Duplicate range [8725-8755]
- Line 291: Duplicate range [8729-8754]
- Line 302: Duplicate range [8729-8754]
- Line 312: Duplicate range [8729-8754]
- Line 389: Duplicate range [8749-8769]
- Line 441: Duplicate range [8755-8769]
- Line 453: Duplicate range [8755-8769]
- Line 474: Duplicate range [8755-8769]
- Line 511: Duplicate range [8756-8769]

---

### File: dynamic/scholar/01-06-08-01.txt

**Errors:**
- Line 15: Duplicate range [8770-8809]

---

### File: dynamic/scholar/01-06-09-01.txt

**Errors:**
- Line 26: Duplicate range [8810-8840]
- Line 59: Duplicate range [8810-8810]
- Line 70: Duplicate range [8810-8810]
- Line 85: Duplicate range [8810-8810]
- Line 100: Duplicate range [8810-8810]
- Line 123: Duplicate range [8810-8810]
- Line 137: Duplicate range [8810-8810]
- Line 149: Duplicate range [8810-8810]
- Line 171: Duplicate range [8810-8810]
- Line 176: Duplicate range [8810-8810]
- Line 188: Duplicate range [8810-8810]
- Line 193: Duplicate range [8810-8810]
- Line 205: Duplicate range [8810-8810]
- Line 228: Duplicate range [8810-8810]
- Line 240: Duplicate range [8810-8810]
- Line 259: Duplicate range [8810-8810]
- Line 273: Duplicate range [8810-8810]
- Line 284: Duplicate range [8810-8810]
- Line 296: Duplicate range [8810-8810]
- Line 319: Duplicate range [8810-8810]
- Line 339: Duplicate range [8810-8810]
- Line 348: Duplicate range [8810-8810]
- Line 376: Duplicate range [8810-8810]

---

### File: dynamic/scholar/01-06-10-01.txt

**Errors:**
- Line 63: Duplicate range [8841-8856]
- Line 144: Duplicate range [8841-8858]
- Line 172: Duplicate range [8841-8858]
- Line 293: Duplicate range [8854-8872]
- Line 298: Duplicate range [8854-8872]
- Line 356: Duplicate range [8859-8872]
- Line 368: Duplicate range [8859-8872]

---

### File: dynamic/scholar/01-06-11-01.txt

**Errors:**
- Line 167: Duplicate range [8873-8884]
- Line 179: Duplicate range [8873-8884]
- Line 212: Duplicate range [8873-8898]
- Line 236: Duplicate range [8873-8896]
- Line 348: Duplicate range [8885-8910]
- Line 415: Duplicate range [8899-8924]
- Line 511: Duplicate range [8911-8936]
- Line 666: Duplicate range [8925-8950]
- Line 762: Duplicate range [8937-8962]
- Line 797: Duplicate range [8939-8964]
- Line 811: Duplicate range [8939-8964]
- Line 882: Duplicate range [8951-8976]
- Line 918: Duplicate range [8957-8982]
- Line 963: Duplicate range [8959-8984]
- Line 1011: Duplicate range [8963-8988]
- Line 1041: Duplicate range [8965-8990]
- Line 1069: Duplicate range [8965-8990]
- Line 1159: Duplicate range [8983-9008]
- Line 1224: Duplicate range [8989-9014]
- Line 1261: Duplicate range [8991-9014]
- Line 1273: Duplicate range [8991-9014]
- Line 1321: Duplicate range [9009-9014]
- Line 1380: Duplicate range [9012-9014]
- Line 1385: Duplicate range [9012-9014]

---

### File: dynamic/scholar/01-06-12-01.txt

**Errors:**
- Line 125: Duplicate range [9015-9016]
- Line 154: Duplicate range [9015-9034]
- Line 166: Duplicate range [9015-9016]
- Line 202: Duplicate range [9017-9042]
- Line 217: Duplicate range [9017-9042]
- Line 291: Duplicate range [9035-9060]
- Line 353: Duplicate range [9043-9068]
- Line 381: Duplicate range [9043-9068]
- Line 459: Duplicate range [9061-9086]
- Line 524: Duplicate range [9069-9094]
- Line 536: Duplicate range [9069-9094]
- Line 624: Duplicate range [9087-9112]
- Line 667: Duplicate range [9095-9120]
- Line 724: Duplicate range [9113-9138]
- Line 794: Duplicate range [9121-9146]
- Line 1268: Duplicate range [9273-9294]
- Line 1337: Duplicate range [9295-9310]
- Line 1880: Duplicate range [9511-9517]

---

### File: dynamic/scholar/01-06-13-01.txt

**Errors:**
- Line 62: Duplicate range [9518-9530]
- Line 130: Duplicate range [9531-9584]

---

### File: dynamic/scholar/01-07-03-01.txt

**Errors:**
- Line 102: Duplicate range [10043-10051]
- Line 106: Duplicate range [10043-10051]

---

### File: dynamic/scholar/01-07-04-01.txt

**Errors:**
- Line 41: Duplicate range [10086-10098]
- Line 88: Duplicate range [10099-10114]
- Line 92: Duplicate range [10099-10114]
- Line 104: Duplicate range [10115-10133]
- Line 112: Duplicate range [10134-10154]
- Line 116: Duplicate range [10134-10154]
- Line 120: Duplicate range [10134-10154]
- Line 166: Duplicate range [10155-10178]
- Line 170: Duplicate range [10155-10178]
- Line 174: Duplicate range [10155-10178]
- Line 182: Duplicate range [10179-10206]
- Line 186: Duplicate range [10179-10206]
- Line 190: Duplicate range [10179-10206]
- Line 254: Duplicate range [10225-10279]
- Line 258: Duplicate range [10225-10279]
- Line 313: Duplicate range [10280-10333]
- Line 321: Duplicate range [10281-10334]
- Line 325: Duplicate range [10281-10334]
- Line 329: Duplicate range [10281-10334]
- Line 333: Duplicate range [10281-10334]
- Line 337: Duplicate range [10281-10334]
- Line 345: Duplicate range [10290-10333]
- Line 397: Duplicate range [10339-10405]
- Line 459: Duplicate range [10406-10426]
- Line 463: Duplicate range [10406-10426]
- Line 467: Duplicate range [10406-10426]
- Line 471: Duplicate range [10406-10426]
- Line 475: Duplicate range [10406-10426]
- Line 479: Duplicate range [10406-10426]
- Line 547: Duplicate range [10470-10470]
- Line 551: Duplicate range [10470-10470]
- Line 555: Duplicate range [10470-10470]

---

### File: dynamic/scholar/01-08-01-01.txt

**Errors:**
- Line 49: Duplicate range [10472-10473]
- Line 53: Duplicate range [10472-10473]
- Line 57: Duplicate range [10472-10473]
- Line 142: Duplicate range [10536-10547]
- Line 146: Duplicate range [10536-10547]
- Line 150: Duplicate range [10536-10547]

---

### File: dynamic/scholar/01-08-02-01.txt

**Errors:**
- Line 66: Duplicate range [10548-10551]
- Line 70: Duplicate range [10548-10551]
- Line 74: Duplicate range [10548-10551]
- Line 91: Duplicate range [10552-10558]
- Line 96: Duplicate range [10552-10558]
- Line 101: Duplicate range [10552-10558]
- Line 129: Duplicate range [10585-10593]
- Line 134: Duplicate range [10585-10593]
- Line 139: Duplicate range [10585-10593]
- Line 149: Duplicate range [10594-10598]
- Line 154: Duplicate range [10594-10598]
- Line 159: Duplicate range [10594-10598]
- Line 169: Duplicate range [10599-10606]
- Line 174: Duplicate range [10599-10606]
- Line 179: Duplicate range [10599-10606]
- Line 189: Duplicate range [10607-10619]
- Line 194: Duplicate range [10607-10619]
- Line 199: Duplicate range [10607-10619]
- Line 213: Duplicate range [10620-10622]
- Line 218: Duplicate range [10620-10622]
- Line 223: Duplicate range [10620-10622]
- Line 233: Duplicate range [10623-10637]
- Line 238: Duplicate range [10623-10637]
- Line 243: Duplicate range [10623-10637]
- Line 291: Duplicate range [10638-10657]
- Line 300: Duplicate range [10638-10644]
- Line 305: Duplicate range [10638-10644]
- Line 310: Duplicate range [10638-10644]
- Line 320: Duplicate range [10645-10657]
- Line 325: Duplicate range [10645-10657]
- Line 330: Duplicate range [10645-10657]
- Line 339: Duplicate range [10658-10692]
- Line 348: Duplicate range [10658-10660]
- Line 353: Duplicate range [10658-10660]
- Line 358: Duplicate range [10658-10660]
- Line 368: Duplicate range [10661-10679]
- Line 373: Duplicate range [10661-10679]
- Line 378: Duplicate range [10661-10679]
- Line 388: Duplicate range [10680-10692]
- Line 393: Duplicate range [10680-10692]
- Line 398: Duplicate range [10680-10692]
- Line 444: Duplicate range [10693-10698]
- Line 449: Duplicate range [10693-10698]
- Line 454: Duplicate range [10693-10698]
- Line 459: Duplicate range [10693-10698]

---

### File: dynamic/scholar/01-08-03-01.txt

**Errors:**
- Line 24: Non-sequential range [10699-10721] - Start (10699) < Previous start (10716)
- Line 24: Duplicate range [10699-10721]
- Line 39: Duplicate range [10699-10721]

---

### File: dynamic/scholar/01-08-04-01.txt

**Errors:**
- Line 12: Duplicate range [10722-10723]
- Line 31: Duplicate range [10722-10723]
- Line 43: Duplicate range [10722-10723]

---

### File: dynamic/scholar/01-08-05-01.txt

**Errors:**
- Line 18: Duplicate range [10757-10773]
- Line 25: Duplicate range [10757-10773]

---

### File: dynamic/scholar/01-08-06-01.txt

**Errors:**
- Line 12: Duplicate range [10775-10781]
- Line 21: Duplicate range [10775-10781]

---

### File: dynamic/scholar/01-08-07-01.txt

**Errors:**
- Line 109: Non-sequential range [10791-10799] - Start (10791) < Previous start (10799)
- Line 172: Non-sequential range [10828-10845] - Start (10828) < Previous start (10836)
- Line 329: Non-sequential range [10882-10896] - Start (10882) < Previous start (10896)
- Line 333: Non-sequential range [10871-10882] - Start (10871) < Previous start (10882)
- Line 454: Non-sequential range [10944-10965] - Start (10944) < Previous start (10956)
- Line 65: Duplicate range [10790-10807]
- Line 69: Duplicate range [10790-10807]
- Line 73: Duplicate range [10790-10807]
- Line 81: Duplicate range [10790-10811]
- Line 85: Duplicate range [10790-10811]
- Line 89: Duplicate range [10790-10811]
- Line 97: Duplicate range [10799-10816]
- Line 101: Duplicate range [10799-10816]
- Line 105: Duplicate range [10799-10816]
- Line 117: Duplicate range [10825-10829]
- Line 121: Duplicate range [10825-10829]
- Line 125: Duplicate range [10825-10829]
- Line 176: Duplicate range [10828-10845]
- Line 180: Duplicate range [10828-10845]
- Line 188: Duplicate range [10831-10855]
- Line 192: Duplicate range [10831-10855]
- Line 196: Duplicate range [10831-10855]
- Line 204: Duplicate range [10833-10857]
- Line 212: Duplicate range [10846-10859]
- Line 216: Duplicate range [10846-10859]
- Line 220: Duplicate range [10846-10859]
- Line 228: Duplicate range [10849-10872]
- Line 232: Duplicate range [10849-10872]
- Line 236: Duplicate range [10849-10872]
- Line 244: Duplicate range [10864-10875]
- Line 248: Duplicate range [10864-10875]
- Line 252: Duplicate range [10864-10875]
- Line 260: Duplicate range [10864-10884]
- Line 264: Duplicate range [10864-10884]
- Line 272: Duplicate range [10870-10890]
- Line 276: Duplicate range [10870-10890]
- Line 280: Duplicate range [10870-10890]
- Line 337: Duplicate range [10871-10882]
- Line 341: Duplicate range [10871-10882]
- Line 349: Duplicate range [10896-10908]
- Line 353: Duplicate range [10896-10908]
- Line 357: Duplicate range [10896-10908]
- Line 365: Duplicate range [10906-10922]
- Line 369: Duplicate range [10906-10922]
- Line 373: Duplicate range [10906-10922]
- Line 381: Duplicate range [10924-10932]
- Line 385: Duplicate range [10924-10932]
- Line 389: Duplicate range [10924-10932]
- Line 397: Duplicate range [10944-10950]
- Line 401: Duplicate range [10944-10950]
- Line 405: Duplicate range [10944-10950]
- Line 458: Duplicate range [10944-10965]
- Line 462: Duplicate range [10944-10965]
- Line 473: Duplicate range [10946-10970]
- Line 481: Duplicate range [10947-10974]
- Line 485: Duplicate range [10947-10974]
- Line 489: Duplicate range [10947-10974]
- Line 497: Duplicate range [10975-11004]
- Line 501: Duplicate range [10975-11004]
- Line 505: Duplicate range [10975-11004]
- Line 556: Duplicate range [11005-11020]
- Line 560: Duplicate range [11005-11020]
- Line 564: Duplicate range [11005-11020]
- Line 572: Duplicate range [11021-11042]
- Line 576: Duplicate range [11021-11042]
- Line 580: Duplicate range [11021-11042]
- Line 588: Duplicate range [11043-11054]
- Line 592: Duplicate range [11043-11054]
- Line 596: Duplicate range [11043-11054]
- Line 634: Duplicate range [11055-11076]
- Line 638: Duplicate range [11055-11076]
- Line 642: Duplicate range [11055-11076]
- Line 650: Duplicate range [11077-11099]
- Line 654: Duplicate range [11077-11099]
- Line 658: Duplicate range [11077-11099]
- Line 666: Duplicate range [11100-11101]
- Line 674: Duplicate range [11102-11127]
- Line 678: Duplicate range [11102-11127]
- Line 682: Duplicate range [11102-11127]
- Line 728: Duplicate range [11128-11137]
- Line 732: Duplicate range [11128-11137]
- Line 740: Duplicate range [11138-11201]
- Line 744: Duplicate range [11138-11201]
- Line 748: Duplicate range [11138-11201]
- Line 783: Duplicate range [11181-11189]
- Line 787: Duplicate range [11181-11189]
- Line 791: Duplicate range [11181-11189]
- Line 799: Duplicate range [11190-11198]
- Line 803: Duplicate range [11190-11198]
- Line 811: Duplicate range [11199-11207]
- Line 815: Duplicate range [11199-11207]
- Line 819: Duplicate range [11199-11207]
- Line 827: Duplicate range [11208-11245]
- Line 831: Duplicate range [11208-11245]
- Line 835: Duplicate range [11208-11245]
- Line 882: Duplicate range [11231-11234]
- Line 886: Duplicate range [11231-11234]
- Line 894: Duplicate range [11240-11266]
- Line 898: Duplicate range [11240-11266]
- Line 902: Duplicate range [11240-11266]
- Line 910: Duplicate range [11266-11316]
- Line 914: Duplicate range [11266-11316]
- Line 918: Duplicate range [11266-11316]
- Line 926: Duplicate range [11290-11316]
- Line 930: Duplicate range [11290-11316]
- Line 934: Duplicate range [11290-11316]
- Line 978: Duplicate range [11297-11316]
- Line 986: Duplicate range [11317-11333]
- Line 990: Duplicate range [11317-11333]
- Line 994: Duplicate range [11317-11333]
- Line 998: Duplicate range [11317-11333]
- Line 1002: Duplicate range [11317-11333]
- Line 1006: Duplicate range [11317-11333]
- Line 1010: Duplicate range [11317-11333]
- Line 1018: Duplicate range [11325-11333]
- Line 1022: Duplicate range [11325-11333]
- Line 1026: Duplicate range [11325-11333]

---

### File: dynamic/scholar/01-09-01-01.txt

**Errors:**
- Line 41: Duplicate range [11335-11335]
- Line 45: Duplicate range [11335-11335]
- Line 49: Duplicate range [11335-11335]
- Line 53: Duplicate range [11335-11335]
- Line 57: Duplicate range [11335-11335]
- Line 61: Duplicate range [11335-11335]
- Line 65: Duplicate range [11335-11335]
- Line 73: Duplicate range [11335-11344]
- Line 77: Duplicate range [11335-11344]
- Line 81: Duplicate range [11335-11344]
- Line 89: Duplicate range [11335-11346]
- Line 93: Duplicate range [11335-11346]
- Line 97: Duplicate range [11335-11346]
- Line 105: Duplicate range [11347-11364]
- Line 109: Duplicate range [11347-11364]
- Line 113: Duplicate range [11347-11364]
- Line 165: Duplicate range [11357-11364]
- Line 169: Duplicate range [11357-11364]
- Line 177: Duplicate range [11365-11391]
- Line 181: Duplicate range [11365-11391]
- Line 185: Duplicate range [11365-11391]
- Line 193: Duplicate range [11373-11391]
- Line 197: Duplicate range [11373-11391]
- Line 201: Duplicate range [11373-11391]
- Line 209: Duplicate range [11384-11391]
- Line 213: Duplicate range [11384-11391]
- Line 217: Duplicate range [11384-11391]
- Line 225: Duplicate range [11392-11396]
- Line 229: Duplicate range [11392-11396]
- Line 233: Duplicate range [11392-11396]
- Line 241: Duplicate range [11397-11433]
- Line 245: Duplicate range [11397-11433]
- Line 249: Duplicate range [11397-11433]
- Line 300: Duplicate range [11424-11450]
- Line 304: Duplicate range [11424-11450]
- Line 308: Duplicate range [11424-11450]
- Line 320: Duplicate range [11453-11504]
- Line 324: Duplicate range [11453-11504]
- Line 328: Duplicate range [11453-11504]
- Line 383: Duplicate range [11505-11546]
- Line 387: Duplicate range [11505-11546]
- Line 391: Duplicate range [11505-11546]
- Line 435: Duplicate range [11547-11606]
- Line 439: Duplicate range [11547-11606]
- Line 443: Duplicate range [11547-11606]
- Line 447: Duplicate range [11547-11606]
- Line 497: Duplicate range [11607-11646]
- Line 501: Duplicate range [11607-11646]
- Line 505: Duplicate range [11607-11646]
- Line 509: Duplicate range [11607-11646]
- Line 513: Duplicate range [11607-11646]
- Line 517: Duplicate range [11607-11646]
- Line 521: Duplicate range [11607-11646]
- Line 529: Duplicate range [11647-11663]
- Line 533: Duplicate range [11647-11663]
- Line 537: Duplicate range [11647-11663]
- Line 541: Duplicate range [11647-11663]
- Line 545: Duplicate range [11647-11663]
- Line 549: Duplicate range [11647-11663]
- Line 553: Duplicate range [11647-11663]
- Line 604: Duplicate range [11664-11681]
- Line 608: Duplicate range [11664-11681]
- Line 616: Duplicate range [11669-11681]
- Line 620: Duplicate range [11669-11681]
- Line 624: Duplicate range [11669-11681]
- Line 636: Duplicate range [11682-11710]
- Line 640: Duplicate range [11682-11710]
- Line 696: Duplicate range [11711-11781]
- Line 700: Duplicate range [11711-11781]
- Line 704: Duplicate range [11711-11781]
- Line 748: Duplicate range [11782-11818]
- Line 752: Duplicate range [11782-11818]
- Line 756: Duplicate range [11782-11818]
- Line 760: Duplicate range [11782-11818]
- Line 768: Duplicate range [11819-11853]
- Line 772: Duplicate range [11819-11853]
- Line 776: Duplicate range [11819-11853]
- Line 780: Duplicate range [11819-11853]
- Line 830: Duplicate range [11854-11901]
- Line 834: Duplicate range [11854-11901]
- Line 838: Duplicate range [11854-11901]
- Line 889: Duplicate range [11896-11957]
- Line 893: Duplicate range [11896-11957]
- Line 897: Duplicate range [11896-11957]
- Line 941: Duplicate range [11952-12000]
- Line 945: Duplicate range [11952-12000]
- Line 949: Duplicate range [11952-12000]
- Line 957: Duplicate range [12001-12047]
- Line 961: Duplicate range [12001-12047]
- Line 965: Duplicate range [12001-12047]
- Line 1016: Duplicate range [12047-12086]
- Line 1020: Duplicate range [12047-12086]
- Line 1024: Duplicate range [12047-12086]
- Line 1074: Duplicate range [12087-12117]
- Line 1078: Duplicate range [12087-12117]
- Line 1082: Duplicate range [12087-12117]
- Line 1090: Duplicate range [12118-12153]
- Line 1094: Duplicate range [12118-12153]
- Line 1098: Duplicate range [12118-12153]
- Line 1152: Duplicate range [12154-12192]
- Line 1156: Duplicate range [12154-12192]
- Line 1160: Duplicate range [12154-12192]
- Line 1216: Duplicate range [12193-12226]
- Line 1220: Duplicate range [12193-12226]
- Line 1224: Duplicate range [12193-12226]
- Line 1232: Duplicate range [12227-12256]
- Line 1236: Duplicate range [12227-12256]
- Line 1240: Duplicate range [12227-12256]
- Line 1281: Duplicate range [12257-12287]
- Line 1285: Duplicate range [12257-12287]
- Line 1289: Duplicate range [12257-12287]
- Line 1297: Duplicate range [12288-12330]
- Line 1301: Duplicate range [12288-12330]
- Line 1305: Duplicate range [12288-12330]
- Line 1356: Duplicate range [12331-12371]
- Line 1360: Duplicate range [12331-12371]
- Line 1364: Duplicate range [12331-12371]
- Line 1415: Duplicate range [12372-12417]
- Line 1419: Duplicate range [12372-12417]
- Line 1423: Duplicate range [12372-12417]
- Line 1431: Duplicate range [12418-12469]
- Line 1435: Duplicate range [12418-12469]
- Line 1439: Duplicate range [12418-12469]

---

### File: dynamic/scholar/01-10-01-01.txt

**Errors:**
- Line 48: Duplicate range [12500-12533]
- Line 53: Duplicate range [12500-12533]
- Line 58: Duplicate range [12500-12533]
- Line 68: Duplicate range [12534-12546]
- Line 73: Duplicate range [12534-12546]
- Line 78: Duplicate range [12534-12546]
- Line 88: Duplicate range [12546-12560]
- Line 93: Duplicate range [12546-12560]
- Line 98: Duplicate range [12546-12560]
- Line 152: Duplicate range [12561-12582]
- Line 157: Duplicate range [12561-12582]
- Line 162: Duplicate range [12561-12582]
- Line 172: Duplicate range [12583-12592]
- Line 177: Duplicate range [12583-12592]
- Line 182: Duplicate range [12583-12592]
- Line 192: Duplicate range [12593-12614]
- Line 197: Duplicate range [12593-12614]
- Line 202: Duplicate range [12593-12614]
- Line 255: Duplicate range [12615-12640]
- Line 260: Duplicate range [12615-12640]
- Line 265: Duplicate range [12615-12640]
- Line 275: Duplicate range [12641-12655]
- Line 280: Duplicate range [12641-12655]
- Line 285: Duplicate range [12641-12655]
- Line 295: Duplicate range [12656-12670]
- Line 300: Duplicate range [12656-12670]
- Line 305: Duplicate range [12656-12670]
- Line 359: Duplicate range [12671-12689]
- Line 364: Duplicate range [12671-12689]
- Line 369: Duplicate range [12671-12689]
- Line 379: Duplicate range [12690-12705]
- Line 384: Duplicate range [12690-12705]
- Line 389: Duplicate range [12690-12705]
- Line 399: Duplicate range [12706-12742]
- Line 404: Duplicate range [12706-12742]
- Line 409: Duplicate range [12706-12742]
- Line 419: Duplicate range [12725-12742]
- Line 424: Duplicate range [12725-12742]
- Line 429: Duplicate range [12725-12742]
- Line 482: Duplicate range [12732-12746]
- Line 487: Duplicate range [12732-12746]
- Line 492: Duplicate range [12732-12746]
- Line 502: Duplicate range [12747-12764]
- Line 507: Duplicate range [12747-12764]
- Line 512: Duplicate range [12747-12764]
- Line 522: Duplicate range [12765-12786]
- Line 527: Duplicate range [12765-12786]
- Line 532: Duplicate range [12765-12786]
- Line 542: Duplicate range [12787-12798]
- Line 547: Duplicate range [12787-12798]
- Line 552: Duplicate range [12787-12798]
- Line 604: Duplicate range [12799-12817]
- Line 609: Duplicate range [12799-12817]
- Line 614: Duplicate range [12799-12817]
- Line 624: Duplicate range [12818-12842]
- Line 629: Duplicate range [12818-12842]
- Line 634: Duplicate range [12818-12842]
- Line 643: Duplicate range [12841-12876]
- Line 647: Duplicate range [12841-12876]
- Line 651: Duplicate range [12841-12876]
- Line 703: Duplicate range [12877-12966]
- Line 707: Duplicate range [12877-12966]
- Line 711: Duplicate range [12877-12966]
- Line 761: Duplicate range [12967-12993]
- Line 765: Duplicate range [12967-12993]
- Line 769: Duplicate range [12967-12993]
- Line 822: Duplicate range [12994-13021]
- Line 826: Duplicate range [12994-13021]
- Line 830: Duplicate range [12994-13021]
- Line 838: Duplicate range [13022-13065]
- Line 842: Duplicate range [13022-13065]
- Line 846: Duplicate range [13022-13065]

---

### File: dynamic/scholar/01-11-01-01.txt

**Errors:**
- Line 269: Duplicate range [13279-13307]

---

### File: dynamic/scholar/01-12-04-01.txt

**Errors:**
- Line 294: Duplicate range [15405-15412]
- Line 303: Duplicate range [15405-15412]
- Line 321: Duplicate range [15413-15414]

---

### File: dynamic/scholar/01-12-05-01.txt

**Errors:**
- Line 17: Duplicate range [15415-15417]
- Line 57: Duplicate range [15422-15427]

---

### File: dynamic/scholar/01-12-05-02.txt

**Errors:**
- Line 16: Duplicate range [15629-15708]
- Line 57: Duplicate range [15629-15708]
- Line 90: Duplicate range [15629-15708]

---

### File: dynamic/scholar/01-12-06-01.txt

**Errors:**
- Line 5: Duplicate range [15769-15777]
- Line 8: Duplicate range [15769-15777]
- Line 11: Duplicate range [15769-15777]

---

### File: dynamic/scholar/01-12-07-01.txt

**Errors:**
- Line 26: Duplicate range [15778-15784]
- Line 52: Duplicate range [15778-15784]
- Line 80: Duplicate range [15778-15784]
- Line 128: Duplicate range [15785-15819]
- Line 163: Duplicate range [15785-15819]
- Line 199: Duplicate range [15785-15819]
- Line 276: Duplicate range [15820-15842]
- Line 311: Duplicate range [15820-15842]
- Line 349: Duplicate range [15820-15842]
- Line 414: Duplicate range [15843-15921]
- Line 454: Duplicate range [15843-15921]
- Line 494: Duplicate range [15843-15921]

---

### File: dynamic/scholar/01-13-01-01.txt

**Errors:**
- Line 367: Non-sequential range [16034-16104] - Start (16034) < Previous start (16042)
- Line 12: Duplicate range [16025-16033]
- Line 41: Duplicate range [16025-16033]
- Line 69: Duplicate range [16025-16033]
- Line 118: Duplicate range [16034-16041]
- Line 149: Duplicate range [16034-16041]
- Line 177: Duplicate range [16034-16041]
- Line 237: Duplicate range [16042-16059]
- Line 273: Duplicate range [16042-16059]
- Line 302: Duplicate range [16042-16059]
- Line 390: Duplicate range [16034-16104]
- Line 432: Duplicate range [16034-16104]
- Line 472: Duplicate range [16034-16104]

---

### File: dynamic/scholar/01-13-02-01.txt

**Errors:**
- Line 30: Duplicate range [16293-16295]
- Line 103: Duplicate range [16344-16350]
- Line 168: Duplicate range [16381-16392]
- Line 271: Duplicate range [16434-16445]
- Line 295: Duplicate range [16453-16460]

---

### File: dynamic/scholar/01-13-03-01.txt

**Errors:**
- Line 13: Duplicate range [16486-16502]
- Line 132: Duplicate range [16542-16560]
- Line 199: Duplicate range [16601-16609]
- Line 232: Duplicate range [16625-16638]
- Line 266: Duplicate range [16647-16655]
- Line 324: Duplicate range [16684-16692]
- Line 359: Duplicate range [16717-16741]
- Line 369: Duplicate range [16717-16741]

---

### File: dynamic/scholar/01-14-02-01.txt

**Errors:**
- Line 19: Duplicate range [17524-17547]
- Line 406: Duplicate range [17867-17869]
- Line 421: Duplicate range [17870-17879]
- Line 450: Duplicate range [17880-17883]

---

### File: dynamic/scholar/01-14-03-01.txt

**Errors:**
- Line 20: Duplicate range [17884-17889]
- Line 40: Duplicate range [17890-17901]
- Line 84: Duplicate range [17912-17918]
- Line 95: Duplicate range [17919-17928]
- Line 136: Duplicate range [17929-17944]
- Line 155: Duplicate range [17945-17948]
- Line 173: Duplicate range [17949-17957]
- Line 190: Duplicate range [17958-17965]
- Line 226: Duplicate range [17966-17980]
- Line 273: Duplicate range [18007-18016]
- Line 290: Duplicate range [18017-18024]
- Line 304: Duplicate range [18025-18032]
- Line 328: Duplicate range [18033-18048]
- Line 349: Duplicate range [18049-18065]
- Line 412: Duplicate range [18101-18112]
- Line 431: Duplicate range [18113-18127]
- Line 454: Duplicate range [18128-18133]
- Line 462: Duplicate range [18134-18144]
- Line 513: Duplicate range [18164-18171]
- Line 529: Duplicate range [18172-18176]
- Line 541: Duplicate range [18177-18185]
- Line 556: Duplicate range [18186-18192]
- Line 578: Duplicate range [18196-18203]
- Line 606: Duplicate range [18204-18234]
- Line 622: Duplicate range [18235-18241]
- Line 649: Duplicate range [18242-18260]

---

### File: dynamic/scholar/01-14-03-02.txt

**Errors:**
- Line 55: Non-sequential range [18262-18273] - Start (18262) < Previous start (18270)
- Line 11: Duplicate range [18262-18273]
- Line 55: Duplicate range [18262-18273]

---

### File: dynamic/scholar/01-14-04-01.txt

**Errors:**
- Line 18: Duplicate range [18274-18285]
- Line 50: Duplicate range [18286-18293]
- Line 65: Duplicate range [18294-18314]
- Line 83: Duplicate range [18315-18331]
- Line 120: Duplicate range [18332-18349]
- Line 131: Duplicate range [18350-18358]
- Line 163: Duplicate range [18359-18405]
- Line 218: Duplicate range [18406-18422]
- Line 234: Duplicate range [18423-18441]
- Line 257: Duplicate range [18442-18464]
- Line 301: Duplicate range [18465-18495]
- Line 364: Duplicate range [18496-18569]
- Line 415: Duplicate range [18570-18572]
- Line 426: Duplicate range [18573-18609]

---

### File: dynamic/scholar/01-14-05-01.txt

**Errors:**
- Line 17: Duplicate range [18610-18610]
- Line 34: Duplicate range [18611-18641]
- Line 60: Duplicate range [18643-18655]
- Line 68: Duplicate range [18643-18655]
- Line 87: Duplicate range [18656-18673]
- Line 103: Duplicate range [18656-18673]
- Line 127: Duplicate range [18674-18693]
- Line 136: Duplicate range [18674-18693]
- Line 178: Duplicate range [18694-18718]
- Line 188: Duplicate range [18694-18718]
- Line 217: Duplicate range [18719-18740]
- Line 234: Duplicate range [18719-18740]
- Line 281: Duplicate range [18727-18731]
- Line 288: Duplicate range [18727-18731]
- Line 296: Duplicate range [18732-18743]
- Line 308: Duplicate range [18741-18760]
- Line 316: Duplicate range [18741-18760]
- Line 334: Duplicate range [18744-18780]
- Line 360: Duplicate range [18761-18800]
- Line 372: Duplicate range [18761-18800]
- Line 384: Duplicate range [18761-18800]
- Line 427: Duplicate range [18783-18797]
- Line 434: Duplicate range [18783-18797]
- Line 438: Duplicate range [18783-18797]
- Line 451: Duplicate range [18798-18824]
- Line 457: Duplicate range [18798-18824]
- Line 466: Duplicate range [18798-18824]
- Line 498: Duplicate range [18801-18850]
- Line 527: Duplicate range [18801-18850]
- Line 555: Duplicate range [18825-18853]
- Line 567: Duplicate range [18825-18853]
- Line 604: Duplicate range [18851-18900]
- Line 614: Duplicate range [18851-18900]
- Line 632: Duplicate range [18854-18873]
- Line 638: Duplicate range [18854-18873]
- Line 647: Duplicate range [18854-18873]
- Line 662: Duplicate range [18874-18880]
- Line 676: Duplicate range [18875-18911]
- Line 683: Duplicate range [18875-18911]
- Line 698: Duplicate range [18875-18911]
- Line 708: Duplicate range [18875-18911]
- Line 741: Duplicate range [18901-18950]
- Line 750: Duplicate range [18901-18950]
- Line 770: Duplicate range [18912-18961]
- Line 778: Duplicate range [18912-18961]
- Line 801: Duplicate range [18912-18961]
- Line 833: Duplicate range [18951-19000]
- Line 843: Duplicate range [18951-19000]
- Line 874: Duplicate range [18962-19007]
- Line 881: Duplicate range [18962-19007]
- Line 920: Duplicate range [19008-19039]
- Line 930: Duplicate range [19008-19039]
- Line 945: Duplicate range [19008-19039]
- Line 954: Duplicate range [19008-19039]
- Line 977: Duplicate range [19040-19114]
- Line 983: Duplicate range [19040-19114]
- Line 994: Duplicate range [19040-19114]
- Line 1016: Duplicate range [19057-19114]
- Line 1026: Duplicate range [19057-19114]
- Line 1056: Duplicate range [19115-19168]
- Line 1065: Duplicate range [19115-19168]
- Line 1078: Duplicate range [19115-19168]
- Line 1082: Duplicate range [19115-19168]
- Line 1117: Duplicate range [19167-19225]
- Line 1121: Duplicate range [19167-19225]
- Line 1137: Duplicate range [19167-19225]
- Line 1149: Duplicate range [19167-19225]
- Line 1161: Duplicate range [19167-19225]
- Line 1174: Duplicate range [19167-19225]
- Line 1194: Duplicate range [19169-19220]
- Line 1205: Duplicate range [19169-19220]
- Line 1222: Duplicate range [19169-19220]
- Line 1243: Duplicate range [19221-19275]
- Line 1247: Duplicate range [19221-19275]
- Line 1261: Duplicate range [19221-19275]
- Line 1271: Duplicate range [19221-19275]
- Line 1299: Duplicate range [19226-19278]
- Line 1308: Duplicate range [19226-19278]
- Line 1328: Duplicate range [19226-19278]
- Line 1364: Duplicate range [19226-19278]
- Line 1368: Duplicate range [19226-19278]
- Line 1386: Duplicate range [19276-19302]
- Line 1395: Duplicate range [19276-19302]
- Line 1404: Duplicate range [19276-19302]
- Line 1413: Duplicate range [19276-19302]
- Line 1431: Duplicate range [19279-19302]
- Line 1435: Duplicate range [19279-19302]
- Line 1445: Duplicate range [19279-19302]
- Line 1454: Duplicate range [19279-19302]
- Line 1467: Duplicate range [19279-19302]
- Line 1471: Duplicate range [19279-19302]
- Line 1477: Duplicate range [19279-19302]
- Line 1524: Duplicate range [19300-19302]
- Line 1535: Duplicate range [19300-19302]
- Line 1546: Duplicate range [19300-19302]
- Line 1550: Duplicate range [19300-19302]

---

### File: dynamic/scholar/01-14-06-01.txt

**Errors:**
- Line 28: Duplicate range [19303-19311]
- Line 37: Duplicate range [19303-19311]
- Line 46: Duplicate range [19303-19311]
- Line 55: Duplicate range [19303-19311]
- Line 73: Duplicate range [19303-19332]
- Line 84: Duplicate range [19303-19332]
- Line 95: Duplicate range [19303-19332]
- Line 99: Duplicate range [19303-19332]
- Line 107: Duplicate range [19303-19311]
- Line 113: Duplicate range [19303-19311]
- Line 117: Duplicate range [19303-19311]
- Line 127: Duplicate range [19303-19311]
- Line 136: Duplicate range [19303-19311]
- Line 149: Duplicate range [19303-19311]
- Line 153: Duplicate range [19303-19311]
- Line 159: Duplicate range [19303-19311]
- Line 188: Duplicate range [19312-19366]
- Line 196: Duplicate range [19312-19366]
- Line 206: Duplicate range [19312-19366]
- Line 218: Duplicate range [19312-19366]
- Line 231: Duplicate range [19312-19353]
- Line 239: Duplicate range [19312-19353]
- Line 252: Duplicate range [19312-19353]
- Line 264: Duplicate range [19312-19353]
- Line 275: Duplicate range [19312-19353]
- Line 282: Duplicate range [19312-19353]
- Line 290: Duplicate range [19312-19353]
- Line 300: Duplicate range [19312-19353]
- Line 312: Duplicate range [19354-19384]
- Line 322: Duplicate range [19354-19384]
- Line 338: Duplicate range [19354-19384]
- Line 348: Duplicate range [19354-19384]
- Line 363: Duplicate range [19354-19384]
- Line 367: Duplicate range [19354-19384]
- Line 383: Duplicate range [19367-19403]
- Line 392: Duplicate range [19367-19403]
- Line 402: Duplicate range [19367-19403]
- Line 415: Duplicate range [19385-19403]
- Line 424: Duplicate range [19385-19403]
- Line 435: Duplicate range [19385-19403]
- Line 439: Duplicate range [19385-19403]
- Line 454: Duplicate range [19385-19403]
- Line 463: Duplicate range [19385-19403]

---

### File: dynamic/scholar/01-14-07-04.txt

**Errors:**
- Line 18: Duplicate range [19421-19440]
- Line 28: Duplicate range [19421-19440]

---

### File: dynamic/scholar/01-14-08-01.txt

**Errors:**
- Line 422: Non-sequential range [19565-19582] - Start (19565) < Previous start (19582)
- Line 436: Non-sequential range [19563-19565] - Start (19563) < Previous start (19565)
- Line 5: Duplicate range [19441-19511]
- Line 19: Duplicate range [19441-19511]
- Line 37: Duplicate range [19441-19511]
- Line 53: Duplicate range [19441-19511]
- Line 57: Duplicate range [19441-19511]
- Line 78: Duplicate range [19441-19511]
- Line 97: Duplicate range [19441-19462]
- Line 109: Duplicate range [19441-19462]
- Line 127: Duplicate range [19441-19462]
- Line 136: Duplicate range [19441-19462]
- Line 145: Duplicate range [19441-19462]
- Line 149: Duplicate range [19441-19462]
- Line 156: Duplicate range [19441-19462]
- Line 168: Duplicate range [19483-19511]
- Line 180: Duplicate range [19483-19511]
- Line 193: Duplicate range [19483-19511]
- Line 207: Duplicate range [19483-19511]
- Line 228: Duplicate range [19483-19511]
- Line 232: Duplicate range [19483-19511]
- Line 236: Duplicate range [19483-19511]
- Line 251: Duplicate range [19483-19511]
- Line 259: Duplicate range [19532-19561]
- Line 267: Duplicate range [19532-19561]
- Line 280: Duplicate range [19532-19561]
- Line 293: Duplicate range [19532-19561]
- Line 297: Duplicate range [19532-19561]
- Line 301: Duplicate range [19532-19561]
- Line 307: Duplicate range [19532-19561]
- Line 315: Duplicate range [19532-19561]
- Line 319: Duplicate range [19532-19561]
- Line 327: Duplicate range [19532-19561]
- Line 335: Duplicate range [19532-19561]
- Line 342: Duplicate range [19532-19561]
- Line 350: Duplicate range [19532-19561]
- Line 354: Duplicate range [19532-19561]
- Line 372: Duplicate range [19582-19607]
- Line 383: Duplicate range [19582-19607]
- Line 391: Duplicate range [19582-19607]
- Line 399: Duplicate range [19582-19607]
- Line 407: Duplicate range [19582-19607]
- Line 414: Duplicate range [19582-19607]
- Line 577: Duplicate range [19628-19635]
- Line 596: Duplicate range [19628-19635]
- Line 616: Duplicate range [19628-19635]
- Line 620: Duplicate range [19628-19635]
- Line 629: Duplicate range [19628-19635]
- Line 637: Duplicate range [19656-19656]
- Line 642: Duplicate range [19656-19656]
- Line 650: Duplicate range [19656-19656]
- Line 654: Duplicate range [19656-19656]
- Line 673: Duplicate range [19656-19656]

---

### File: dynamic/scholar/01-14-09-01.txt

**Errors:**
- Line 5: Duplicate range [19657-19677]
- Line 10: Duplicate range [19657-19677]
- Line 18: Duplicate range [19657-19677]
- Line 22: Duplicate range [19657-19677]
- Line 41: Duplicate range [19657-19677]

---

### File: dynamic/scholar/01-14-11-01.txt

**Errors:**
- Line 17: Duplicate range [20147-20176]
- Line 41: Duplicate range [20147-20176]
- Line 72: Duplicate range [20147-20176]
- Line 123: Duplicate range [20177-20208]
- Line 146: Duplicate range [20177-20208]
- Line 178: Duplicate range [20177-20208]

---

### File: dynamic/scholar/02-15-03-01.txt

**Errors:**
- Line 17: Duplicate range [670-676]

---

### File: dynamic/scholar/02-16-04-01.txt

**Errors:**
- Line 4: Duplicate range [1589-1598]
- Line 7: Duplicate range [1589-1598]
- Line 10: Duplicate range [1589-1598]
- Line 13: Duplicate range [1589-1598]
- Line 16: Duplicate range [1589-1598]
- Line 22: Duplicate range [1599-1609]
- Line 25: Duplicate range [1599-1609]
- Line 28: Duplicate range [1599-1609]
- Line 31: Duplicate range [1599-1609]
- Line 34: Duplicate range [1599-1609]
- Line 40: Duplicate range [1610-1621]
- Line 43: Duplicate range [1610-1621]
- Line 46: Duplicate range [1610-1621]
- Line 49: Duplicate range [1610-1621]
- Line 52: Duplicate range [1610-1621]
- Line 58: Duplicate range [1622-1636]
- Line 61: Duplicate range [1622-1636]
- Line 64: Duplicate range [1622-1636]
- Line 67: Duplicate range [1622-1636]
- Line 70: Duplicate range [1622-1636]

---

### File: dynamic/scholar/02-16-05-01.txt

**Errors:**
- Line 16: Duplicate range [1638-1647]
- Line 45: Duplicate range [1649-1662]
- Line 71: Duplicate range [1663-1664]
- Line 94: Duplicate range [1665-1670]
- Line 115: Duplicate range [1671-1679]
- Line 135: Duplicate range [1711-1725]

---

### File: dynamic/scholar/02-17-01-01.txt

**Errors:**
- Line 15: Duplicate range [1754-1768]
- Line 38: Duplicate range [1799-1813]
- Line 57: Duplicate range [1849-1858]
- Line 65: Duplicate range [1849-1858]
- Line 69: Duplicate range [1849-1858]
- Line 79: Duplicate range [1859-1860]
- Line 85: Duplicate range [1859-1860]
- Line 89: Duplicate range [1859-1860]

---

### File: dynamic/scholar/02-17-02-01.txt

**Errors:**
- Line 7: Duplicate range [1861-1863]
- Line 17: Duplicate range [1861-1908]
- Line 37: Duplicate range [1894-1908]
- Line 75: Duplicate range [1944-1958]
- Line 88: Duplicate range [1944-1958]
- Line 92: Duplicate range [1944-1958]
- Line 100: Duplicate range [1944-1958]
- Line 134: Duplicate range [1975-1990]
- Line 157: Duplicate range [1991-2005]
- Line 169: Duplicate range [1991-2005]
- Line 173: Duplicate range [1991-2005]

---

### File: dynamic/scholar/02-17-03-01.txt

**Errors:**
- Line 5: Duplicate range [2051-2063]
- Line 8: Duplicate range [2051-2063]
- Line 11: Duplicate range [2051-2063]

---

### File: dynamic/scholar/02-17-04-01.txt

**Errors:**
- Line 470: Non-sequential range [2100-2143] - Start (2100) < Previous start (2500)
- Line 85: Duplicate range [2064-2096]
- Line 139: Duplicate range [2097-2145]
- Line 518: Duplicate range [2100-2143]
- Line 548: Duplicate range [2100-2143]
- Line 572: Duplicate range [2100-2143]

---

### File: dynamic/scholar/02-17-05-01.txt

**Errors:**
- Line 7: Duplicate range [2689-2702]
- Line 10: Duplicate range [2689-2702]
- Line 13: Duplicate range [2689-2702]
- Line 19: Duplicate range [2703-2717]
- Line 22: Duplicate range [2703-2717]
- Line 25: Duplicate range [2703-2717]
- Line 31: Duplicate range [2718-2738]
- Line 34: Duplicate range [2718-2738]
- Line 37: Duplicate range [2718-2738]
- Line 40: Duplicate range [2718-2738]

---

### File: dynamic/scholar/02-17-06-01.txt

**Errors:**
- Line 4: Duplicate range [2779-2802]
- Line 7: Duplicate range [2779-2802]
- Line 10: Duplicate range [2779-2802]
- Line 16: Duplicate range [2803-2836]
- Line 19: Duplicate range [2803-2836]
- Line 22: Duplicate range [2803-2836]
- Line 28: Duplicate range [2837-2910]
- Line 31: Duplicate range [2837-2910]
- Line 34: Duplicate range [2837-2910]
- Line 40: Duplicate range [2911-2958]
- Line 43: Duplicate range [2911-2958]
- Line 46: Duplicate range [2911-2958]
- Line 52: Duplicate range [2959-2970]
- Line 55: Duplicate range [2959-2970]
- Line 58: Duplicate range [2959-2970]

---

### File: dynamic/scholar/02-17-07-01.txt

**Errors:**
- Line 7: Duplicate range [3005-3014]
- Line 10: Duplicate range [3005-3014]
- Line 13: Duplicate range [3005-3014]
- Line 19: Duplicate range [3015-3044]
- Line 22: Duplicate range [3015-3044]
- Line 25: Duplicate range [3015-3044]
- Line 28: Duplicate range [3015-3044]
- Line 34: Duplicate range [3045-3056]
- Line 37: Duplicate range [3045-3056]
- Line 40: Duplicate range [3045-3056]
- Line 43: Duplicate range [3045-3056]

---

### File: dynamic/scholar/02-17-08-01.txt

**Errors:**
- Line 7: Duplicate range [3057-3058]
- Line 10: Duplicate range [3057-3058]
- Line 13: Duplicate range [3057-3058]
- Line 19: Duplicate range [3059-3073]
- Line 22: Duplicate range [3059-3073]
- Line 25: Duplicate range [3059-3073]
- Line 31: Duplicate range [3074-3088]
- Line 37: Duplicate range [3089-3103]
- Line 43: Duplicate range [3104-3118]
- Line 49: Duplicate range [3119-3123]
- Line 52: Duplicate range [3119-3123]

---

### File: dynamic/scholar/02-17-09-01.txt

**Errors:**
- Line 7: Duplicate range [3124-3129]
- Line 10: Duplicate range [3124-3129]
- Line 13: Duplicate range [3124-3129]
- Line 19: Duplicate range [3130-3144]
- Line 22: Duplicate range [3130-3144]
- Line 25: Duplicate range [3130-3144]
- Line 31: Duplicate range [3145-3168]
- Line 34: Duplicate range [3145-3168]
- Line 37: Duplicate range [3145-3168]
- Line 40: Duplicate range [3145-3168]

---

### File: dynamic/scholar/02-17-09-02.txt

**Errors:**
- Line 123: Duplicate range [3198-3306]
- Line 299: Duplicate range [3198-3306]
- Line 388: Duplicate range [3198-3306]

---

### File: dynamic/scholar/02-17-10-01.txt

**Errors:**
- Line 52: Duplicate range [3307-3316]
- Line 87: Duplicate range [3307-3316]
- Line 131: Duplicate range [3317-3336]
- Line 158: Duplicate range [3317-3336]
- Line 185: Duplicate range [3317-3336]

---

### File: dynamic/scholar/02-17-11-01.txt

**Errors:**
- Line 4: Duplicate range [3354-3356]
- Line 7: Duplicate range [3354-3356]
- Line 10: Duplicate range [3354-3356]
- Line 13: Duplicate range [3354-3356]
- Line 19: Duplicate range [3357-3371]
- Line 22: Duplicate range [3357-3371]
- Line 25: Duplicate range [3357-3371]
- Line 28: Duplicate range [3357-3371]
- Line 34: Duplicate range [3372-3393]
- Line 37: Duplicate range [3372-3393]
- Line 40: Duplicate range [3372-3393]
- Line 43: Duplicate range [3372-3393]
- Line 49: Duplicate range [3394-3404]
- Line 52: Duplicate range [3394-3404]
- Line 55: Duplicate range [3394-3404]
- Line 58: Duplicate range [3394-3404]
- Line 64: Duplicate range [3405-3419]
- Line 67: Duplicate range [3405-3419]
- Line 70: Duplicate range [3405-3419]
- Line 73: Duplicate range [3405-3419]
- Line 79: Duplicate range [3420-3434]
- Line 82: Duplicate range [3420-3434]
- Line 85: Duplicate range [3420-3434]
- Line 88: Duplicate range [3420-3434]
- Line 94: Duplicate range [3435-3461]
- Line 97: Duplicate range [3435-3461]
- Line 100: Duplicate range [3435-3461]
- Line 103: Duplicate range [3435-3461]
- Line 109: Duplicate range [3462-3476]
- Line 112: Duplicate range [3462-3476]
- Line 115: Duplicate range [3462-3476]
- Line 118: Duplicate range [3462-3476]
- Line 124: Duplicate range [3477-3499]
- Line 127: Duplicate range [3477-3499]
- Line 130: Duplicate range [3477-3499]
- Line 133: Duplicate range [3477-3499]

---

### File: dynamic/scholar/02-17-12-01.txt

**Errors:**
- Line 7: Duplicate range [3600-3612]
- Line 10: Duplicate range [3600-3612]
- Line 13: Duplicate range [3600-3612]
- Line 19: Duplicate range [3613-3640]
- Line 22: Duplicate range [3613-3640]
- Line 25: Duplicate range [3613-3640]
- Line 28: Duplicate range [3613-3640]
- Line 34: Duplicate range [3641-3651]
- Line 37: Duplicate range [3641-3651]
- Line 40: Duplicate range [3641-3651]
- Line 43: Duplicate range [3641-3651]

---

### File: dynamic/scholar/02-17-13-01.txt

**Errors:**
- Line 7: Duplicate range [3709-3714]
- Line 10: Duplicate range [3709-3714]
- Line 13: Duplicate range [3709-3714]
- Line 19: Duplicate range [3715-3731]
- Line 22: Duplicate range [3715-3731]
- Line 25: Duplicate range [3715-3731]
- Line 28: Duplicate range [3715-3731]
- Line 34: Duplicate range [3732-3750]
- Line 37: Duplicate range [3732-3750]
- Line 40: Duplicate range [3732-3750]
- Line 43: Duplicate range [3732-3750]
- Line 49: Duplicate range [3751-3762]
- Line 52: Duplicate range [3751-3762]
- Line 55: Duplicate range [3751-3762]
- Line 58: Duplicate range [3751-3762]

---

### File: dynamic/scholar/02-17-14-01.txt

**Errors:**
- Line 4: Duplicate range [3852-3864]
- Line 7: Duplicate range [3852-3864]
- Line 10: Duplicate range [3852-3864]
- Line 13: Duplicate range [3852-3864]
- Line 19: Duplicate range [3865-3894]
- Line 22: Duplicate range [3865-3894]
- Line 25: Duplicate range [3865-3894]
- Line 28: Duplicate range [3865-3894]
- Line 34: Duplicate range [3895-3921]
- Line 37: Duplicate range [3895-3921]
- Line 40: Duplicate range [3895-3921]
- Line 43: Duplicate range [3895-3921]

---

### File: dynamic/scholar/02-18-01-01.txt

**Errors:**
- Line 7: Duplicate range [3922-3932]
- Line 10: Duplicate range [3922-3932]
- Line 13: Duplicate range [3922-3932]
- Line 19: Duplicate range [3933-3947]
- Line 22: Duplicate range [3933-3947]
- Line 25: Duplicate range [3933-3947]
- Line 28: Duplicate range [3933-3947]
- Line 34: Duplicate range [3948-3962]
- Line 37: Duplicate range [3948-3962]
- Line 40: Duplicate range [3948-3962]
- Line 43: Duplicate range [3948-3962]
- Line 49: Duplicate range [3963-3983]
- Line 52: Duplicate range [3963-3983]
- Line 55: Duplicate range [3963-3983]
- Line 58: Duplicate range [3963-3983]
- Line 64: Duplicate range [3984-4015]
- Line 67: Duplicate range [3984-4015]
- Line 70: Duplicate range [3984-4015]
- Line 73: Duplicate range [3984-4015]
- Line 79: Duplicate range [4016-4065]
- Line 82: Duplicate range [4016-4065]
- Line 85: Duplicate range [4016-4065]
- Line 88: Duplicate range [4016-4065]
- Line 94: Duplicate range [4066-4119]
- Line 97: Duplicate range [4066-4119]
- Line 100: Duplicate range [4066-4119]
- Line 103: Duplicate range [4066-4119]
- Line 109: Duplicate range [4120-4155]
- Line 112: Duplicate range [4120-4155]
- Line 115: Duplicate range [4120-4155]
- Line 118: Duplicate range [4120-4155]

---

### File: dynamic/scholar/02-18-02-01.txt

**Errors:**
- Line 4: Duplicate range [4156-4214]
- Line 7: Duplicate range [4156-4214]
- Line 10: Duplicate range [4156-4214]
- Line 16: Duplicate range [4215-4300]
- Line 19: Duplicate range [4215-4300]
- Line 22: Duplicate range [4215-4300]
- Line 28: Duplicate range [4300-4400]
- Line 31: Duplicate range [4300-4400]
- Line 34: Duplicate range [4300-4400]
- Line 40: Duplicate range [4400-4400]
- Line 43: Duplicate range [4400-4400]
- Line 46: Duplicate range [4400-4400]

---

### File: dynamic/scholar/02-18-02-02.txt

**Errors:**
- Line 18: Duplicate range [4401-4403]
- Line 66: Duplicate range [4401-4405]

---

### File: dynamic/scholar/02-18-02-03.txt

**Errors:**
- Line 11: Duplicate range [4406-4424]
- Line 20: Duplicate range [4406-4424]
- Line 27: Duplicate range [4406-4424]

---

### File: dynamic/scholar/02-18-03-04.txt

**Errors:**
- Line 7: Duplicate range [4428-4433]
- Line 10: Duplicate range [4428-4433]
- Line 13: Duplicate range [4428-4433]
- Line 19: Duplicate range [4434-4467]
- Line 22: Duplicate range [4434-4467]
- Line 25: Duplicate range [4434-4467]
- Line 28: Duplicate range [4434-4467]
- Line 31: Duplicate range [4434-4467]
- Line 34: Duplicate range [4434-4467]
- Line 37: Duplicate range [4434-4467]
- Line 40: Duplicate range [4434-4467]

---

### File: dynamic/scholar/02-18-04-01.txt

**Errors:**
- Line 10: Duplicate range [4468-4475]
- Line 21: Duplicate range [4468-4475]
- Line 31: Duplicate range [4468-4475]
- Line 52: Duplicate range [4476-4502]
- Line 62: Duplicate range [4476-4502]
- Line 71: Duplicate range [4476-4502]
- Line 93: Duplicate range [4503-4546]
- Line 102: Duplicate range [4503-4546]
- Line 111: Duplicate range [4503-4546]
- Line 128: Duplicate range [4547-4565]
- Line 138: Duplicate range [4547-4565]
- Line 147: Duplicate range [4547-4565]
- Line 165: Duplicate range [4566-4596]
- Line 175: Duplicate range [4566-4596]
- Line 184: Duplicate range [4566-4596]
- Line 202: Duplicate range [4597-4600]
- Line 212: Duplicate range [4597-4600]
- Line 221: Duplicate range [4597-4600]

---

### File: dynamic/scholar/02-18-06-01.txt

**Errors:**
- Line 36: Duplicate range [4720-4733]

---

### File: dynamic/scholar/02-18-07-01.txt

**Errors:**
- Line 23: Duplicate range [4749-4767]
- Line 65: Duplicate range [4789-4801]
- Line 104: Duplicate range [4812-4830]
- Line 202: Duplicate range [4891-4905]
- Line 206: Duplicate range [4891-4905]

---

### File: dynamic/scholar/02-18-08-01.txt

**Errors:**
- Line 22: Duplicate range [4926-4953]
- Line 32: Duplicate range [4926-4953]
- Line 70: Duplicate range [4954-4983]
- Line 110: Duplicate range [4984-5011]

---

### File: dynamic/scholar/02-18-08-02.txt

**Errors:**
- Line 10: Duplicate range [5035-5037]
- Line 40: Duplicate range [5038-5062]
- Line 51: Duplicate range [5038-5062]

---

### File: dynamic/scholar/02-18-09-01.txt

**Errors:**
- Line 5: Duplicate range [5085-5087]
- Line 20: Duplicate range [5085-5087]

---

### File: dynamic/scholar/02-18-10-01.txt

**Errors:**
- Line 5: Duplicate range [5125-5130]

---

### File: dynamic/scholar/02-18-11-01.txt

**Errors:**
- Line 7: Duplicate range [5159-5161]
- Line 10: Duplicate range [5159-5161]
- Line 13: Duplicate range [5159-5161]
- Line 19: Duplicate range [5162-5168]
- Line 22: Duplicate range [5162-5168]
- Line 25: Duplicate range [5162-5168]
- Line 31: Duplicate range [5169-5176]
- Line 34: Duplicate range [5169-5176]
- Line 37: Duplicate range [5169-5176]
- Line 40: Duplicate range [5169-5176]
- Line 46: Duplicate range [5177-5189]
- Line 49: Duplicate range [5177-5189]
- Line 52: Duplicate range [5177-5189]
- Line 55: Duplicate range [5177-5189]
- Line 61: Duplicate range [5190-5203]
- Line 64: Duplicate range [5190-5203]
- Line 67: Duplicate range [5190-5203]
- Line 70: Duplicate range [5190-5203]
- Line 76: Duplicate range [5204-5218]
- Line 79: Duplicate range [5204-5218]
- Line 82: Duplicate range [5204-5218]
- Line 85: Duplicate range [5204-5218]
- Line 91: Duplicate range [5219-5241]
- Line 94: Duplicate range [5219-5241]
- Line 97: Duplicate range [5219-5241]
- Line 100: Duplicate range [5219-5241]

---

### File: dynamic/scholar/02-18-12-01.txt

**Errors:**
- Line 7: Duplicate range [5242-5245]
- Line 10: Duplicate range [5242-5245]
- Line 13: Duplicate range [5242-5245]
- Line 19: Duplicate range [5246-5253]
- Line 22: Duplicate range [5246-5253]
- Line 25: Duplicate range [5246-5253]
- Line 31: Duplicate range [5254-5260]
- Line 34: Duplicate range [5254-5260]
- Line 37: Duplicate range [5254-5260]
- Line 43: Duplicate range [5261-5268]
- Line 46: Duplicate range [5261-5268]
- Line 49: Duplicate range [5261-5268]

---

### File: dynamic/scholar/02-18-13-01.txt

**Errors:**
- Line 5: Duplicate range [5269-5281]
- Line 36: Duplicate range [5285-5300]
- Line 71: Duplicate range [5316-5332]
- Line 150: Duplicate range [5402-5411]
- Line 237: Duplicate range [5482-5498]
- Line 291: Duplicate range [5524-5539]
- Line 321: Duplicate range [5540-5542]
- Line 329: Duplicate range [5543-5545]
- Line 339: Duplicate range [5546-5557]
- Line 374: Duplicate range [5590-5591]
- Line 408: Duplicate range [5600-5615]

---

### File: dynamic/scholar/02-18-14-01.txt

**Errors:**
- Line 4: Duplicate range [5640-5645]
- Line 7: Duplicate range [5640-5645]
- Line 10: Duplicate range [5640-5645]
- Line 13: Duplicate range [5640-5645]
- Line 16: Duplicate range [5640-5645]
- Line 19: Duplicate range [5640-5645]
- Line 22: Duplicate range [5640-5645]

---

### File: dynamic/scholar/02-18-15-01.txt

**Errors:**
- Line 18: Duplicate range [5646-5718]
- Line 51: Duplicate range [5646-5718]
- Line 98: Duplicate range [5646-5718]
- Line 236: Duplicate range [5719-5752]
- Line 261: Duplicate range [5719-5752]

---

### File: dynamic/scholar/02-18-16-01.txt

**Errors:**
- Line 7: Duplicate range [5911-5920]
- Line 10: Duplicate range [5911-5920]
- Line 13: Duplicate range [5911-5920]
- Line 19: Duplicate range [5921-5922]
- Line 22: Duplicate range [5921-5922]
- Line 25: Duplicate range [5921-5922]

---

### File: dynamic/scholar/02-18-16-02.txt

**Errors:**
- Line 5: Duplicate range [5923-5924]
- Line 8: Duplicate range [5923-5924]
- Line 11: Duplicate range [5923-5924]

---

### File: dynamic/scholar/02-18-16-03.txt

**Errors:**
- Line 11: Duplicate range [5925-5927]
- Line 36: Duplicate range [5925-5927]
- Line 49: Duplicate range [5925-5927]

---

### File: dynamic/scholar/02-18-16-04.txt

**Errors:**
- Line 7: Duplicate range [5928-5929]
- Line 17: Duplicate range [5928-5930]
- Line 75: Duplicate range [5931-5945]
- Line 85: Duplicate range [5946-5960]

---

### File: dynamic/scholar/02-19-00-01.txt

**Errors:**
- Line 29: Duplicate range [5963-6028]
- Line 81: Duplicate range [5963-6028]
- Line 130: Duplicate range [5963-6028]
- Line 240: Duplicate range [6029-6061]
- Line 289: Duplicate range [6029-6061]
- Line 335: Duplicate range [6029-6061]
- Line 451: Duplicate range [6062-6411]
- Line 508: Duplicate range [6062-6411]
- Line 557: Duplicate range [6062-6411]
- Line 726: Duplicate range [6339-6411]
- Line 803: Duplicate range [6339-6411]
- Line 862: Duplicate range [6339-6411]

---

### File: dynamic/scholar/02-19-01-01.txt

**Errors:**
- Line 1441: Non-sequential range [6744-6765] - Start (6744) < Previous start (8052)
- Line 173: Duplicate range [6495-6501]
- Line 250: Duplicate range [6523-6527]
- Line 261: Duplicate range [6528-6532]
- Line 306: Duplicate range [6549-6551]
- Line 374: Duplicate range [6581-6589]
- Line 397: Duplicate range [6590-6595]
- Line 427: Duplicate range [6625-6675]
- Line 467: Duplicate range [6643-6648]
- Line 483: Duplicate range [6649-6656]
- Line 498: Duplicate range [6660-6675]
- Line 521: Duplicate range [6676-6693]
- Line 595: Duplicate range [6740-6792]
- Line 622: Duplicate range [6793-6837]
- Line 649: Duplicate range [6838-6879]
- Line 676: Duplicate range [6880-6918]
- Line 703: Duplicate range [6919-6956]
- Line 730: Duplicate range [6957-6995]
- Line 757: Duplicate range [6996-7037]
- Line 784: Duplicate range [7038-7084]
- Line 811: Duplicate range [7085-7150]
- Line 838: Duplicate range [7151-7195]
- Line 865: Duplicate range [7196-7230]
- Line 892: Duplicate range [7231-7263]
- Line 919: Duplicate range [7264-7290]
- Line 946: Duplicate range [7291-7320]
- Line 973: Duplicate range [7321-7357]
- Line 1000: Duplicate range [7358-7394]
- Line 1027: Duplicate range [7395-7451]
- Line 1095: Duplicate range [7491-7532]
- Line 1122: Duplicate range [7533-7582]
- Line 1149: Duplicate range [7583-7627]
- Line 1191: Duplicate range [7672-7674]
- Line 1200: Duplicate range [7672-7717]
- Line 1243: Duplicate range [7718-7764]
- Line 1270: Duplicate range [7765-7816]
- Line 1297: Duplicate range [7817-7870]
- Line 1324: Duplicate range [7871-7922]
- Line 1351: Duplicate range [7923-7964]
- Line 1378: Duplicate range [7965-8012]
- Line 1405: Duplicate range [8013-8051]
- Line 1432: Duplicate range [8052-8082]
- Line 1464: Duplicate range [6744-6765]
- Line 1489: Duplicate range [6744-6765]
- Line 1513: Duplicate range [6744-6765]
- Line 1574: Duplicate range [6766-6806]
- Line 1609: Duplicate range [6766-6806]
- Line 1629: Duplicate range [6766-6806]
- Line 1691: Duplicate range [6807-6850]
- Line 1710: Duplicate range [6807-6850]
- Line 1730: Duplicate range [6807-6850]

---

### File: dynamic/scholar/02-20-01-01.txt

**Errors:**
- Line 249: Non-sequential range [8083-8162] - Start (8083) < Previous start (8571)
- Line 7: Duplicate range [8083-8084]
- Line 10: Duplicate range [8083-8084]
- Line 13: Duplicate range [8083-8084]
- Line 28: Duplicate range [8126-8128]
- Line 31: Duplicate range [8126-8128]
- Line 34: Duplicate range [8126-8128]
- Line 52: Duplicate range [8165-8167]
- Line 55: Duplicate range [8165-8167]
- Line 58: Duplicate range [8165-8167]
- Line 73: Duplicate range [8195-8197]
- Line 76: Duplicate range [8195-8197]
- Line 79: Duplicate range [8195-8197]
- Line 94: Duplicate range [8251-8253]
- Line 97: Duplicate range [8251-8253]
- Line 100: Duplicate range [8251-8253]
- Line 115: Duplicate range [8303-8305]
- Line 118: Duplicate range [8303-8305]
- Line 121: Duplicate range [8303-8305]
- Line 136: Duplicate range [8375-8377]
- Line 139: Duplicate range [8375-8377]
- Line 142: Duplicate range [8375-8377]
- Line 157: Duplicate range [8415-8417]
- Line 160: Duplicate range [8415-8417]
- Line 163: Duplicate range [8415-8417]
- Line 178: Duplicate range [8457-8459]
- Line 181: Duplicate range [8457-8459]
- Line 184: Duplicate range [8457-8459]
- Line 199: Duplicate range [8491-8493]
- Line 202: Duplicate range [8491-8493]
- Line 205: Duplicate range [8491-8493]
- Line 220: Duplicate range [8531-8545]
- Line 223: Duplicate range [8531-8545]
- Line 226: Duplicate range [8531-8545]
- Line 241: Duplicate range [8571-8573]
- Line 244: Duplicate range [8571-8573]
- Line 247: Duplicate range [8571-8573]
- Line 276: Duplicate range [8083-8162]
- Line 299: Duplicate range [8083-8162]
- Line 344: Duplicate range [8083-8162]

---

### File: dynamic/scholar/02-20-02-01.txt

**Errors:**
- Line 7: Duplicate range [8831-8844]
- Line 10: Duplicate range [8831-8844]
- Line 13: Duplicate range [8831-8844]
- Line 16: Duplicate range [8831-8844]
- Line 31: Duplicate range [8880-8895]
- Line 34: Duplicate range [8880-8895]
- Line 37: Duplicate range [8880-8895]
- Line 40: Duplicate range [8880-8895]
- Line 55: Duplicate range [8925-8936]
- Line 58: Duplicate range [8925-8936]
- Line 61: Duplicate range [8925-8936]
- Line 64: Duplicate range [8925-8936]
- Line 76: Duplicate range [8960-8969]
- Line 79: Duplicate range [8960-8969]
- Line 82: Duplicate range [8960-8969]
- Line 85: Duplicate range [8960-8969]

---

### File: dynamic/scholar/02-20-03-01.txt

**Errors:**
- Line 11: Duplicate range [8970-8971]
- Line 41: Duplicate range [8970-8971]
- Line 50: Duplicate range [8970-8971]

---

### File: dynamic/scholar/02-20-04-01.txt

**Errors:**
- Line 7: Duplicate range [8972-8976]
- Line 10: Duplicate range [8972-8976]
- Line 13: Duplicate range [8972-8976]
- Line 28: Duplicate range [9002-9015]
- Line 31: Duplicate range [9002-9015]
- Line 34: Duplicate range [9002-9015]

---

### File: dynamic/scholar/02-20-05-01.txt

**Errors:**
- Line 7: Duplicate range [9027-9029]
- Line 10: Duplicate range [9027-9029]
- Line 13: Duplicate range [9027-9029]
- Line 25: Duplicate range [9043-9063]
- Line 28: Duplicate range [9043-9063]
- Line 31: Duplicate range [9043-9063]
- Line 34: Duplicate range [9043-9063]

---

### File: dynamic/scholar/02-20-06-01.txt

**Errors:**
- Line 18: Duplicate range [9069-9078]
- Line 57: Duplicate range [9069-9078]
- Line 71: Duplicate range [9069-9078]

---

### File: dynamic/scholar/02-20-07-01.txt

**Errors:**
- Line 7: Duplicate range [9079-9083]
- Line 10: Duplicate range [9079-9083]
- Line 13: Duplicate range [9079-9083]
- Line 25: Duplicate range [9103-9116]
- Line 28: Duplicate range [9103-9116]
- Line 31: Duplicate range [9103-9116]
- Line 46: Duplicate range [9143-9165]
- Line 49: Duplicate range [9143-9165]
- Line 52: Duplicate range [9143-9165]
- Line 67: Duplicate range [9209-9219]
- Line 70: Duplicate range [9209-9219]
- Line 73: Duplicate range [9209-9219]

---

### File: dynamic/scholar/02-20-08-01.txt

**Errors:**
- Line 7: Duplicate range [9223-9238]
- Line 10: Duplicate range [9223-9238]
- Line 13: Duplicate range [9223-9238]
- Line 25: Duplicate range [9239-9274]
- Line 28: Duplicate range [9239-9274]
- Line 31: Duplicate range [9239-9274]
- Line 34: Duplicate range [9239-9274]
- Line 49: Duplicate range [9275-9314]
- Line 52: Duplicate range [9275-9314]
- Line 55: Duplicate range [9275-9314]
- Line 58: Duplicate range [9275-9314]
- Line 73: Duplicate range [9315-9352]
- Line 76: Duplicate range [9315-9352]
- Line 79: Duplicate range [9315-9352]
- Line 82: Duplicate range [9315-9352]
- Line 97: Duplicate range [9353-9384]
- Line 100: Duplicate range [9353-9384]
- Line 103: Duplicate range [9353-9384]
- Line 106: Duplicate range [9353-9384]
- Line 121: Duplicate range [9385-9403]
- Line 124: Duplicate range [9385-9403]
- Line 127: Duplicate range [9385-9403]
- Line 130: Duplicate range [9385-9403]

---

### File: dynamic/scholar/02-20-09-01.txt

**Errors:**
- Line 12: Duplicate range [9404-9412]
- Line 21: Duplicate range [9404-9412]

---

### File: dynamic/scholar/02-21-00-01.txt

**Errors:**
- Line 7: Duplicate range [9413-9455]
- Line 10: Duplicate range [9413-9455]
- Line 13: Duplicate range [9413-9455]
- Line 28: Duplicate range [9456-9494]
- Line 31: Duplicate range [9456-9494]
- Line 34: Duplicate range [9456-9494]
- Line 49: Duplicate range [9495-9537]
- Line 52: Duplicate range [9495-9537]
- Line 55: Duplicate range [9495-9537]
- Line 70: Duplicate range [9538-9584]
- Line 73: Duplicate range [9538-9584]
- Line 76: Duplicate range [9538-9584]
- Line 91: Duplicate range [9585-9616]
- Line 94: Duplicate range [9585-9616]
- Line 97: Duplicate range [9585-9616]
- Line 112: Duplicate range [9617-9653]
- Line 115: Duplicate range [9617-9653]
- Line 118: Duplicate range [9617-9653]
- Line 121: Duplicate range [9617-9653]
- Line 136: Duplicate range [9654-9684]
- Line 139: Duplicate range [9654-9684]
- Line 142: Duplicate range [9654-9684]
- Line 157: Duplicate range [9685-9712]
- Line 160: Duplicate range [9685-9712]
- Line 163: Duplicate range [9685-9712]
- Line 166: Duplicate range [9685-9712]

---

### File: dynamic/scholar/02-21-01-01.txt

**Errors:**
- Line 4: Duplicate range [9713-9719]
- Line 7: Duplicate range [9713-9719]
- Line 10: Duplicate range [9713-9719]
- Line 13: Duplicate range [9713-9719]
- Line 22: Duplicate range [9720-9759]
- Line 25: Duplicate range [9720-9759]
- Line 28: Duplicate range [9720-9759]
- Line 43: Duplicate range [9760-9797]
- Line 46: Duplicate range [9760-9797]
- Line 49: Duplicate range [9760-9797]
- Line 64: Duplicate range [9798-9845]
- Line 67: Duplicate range [9798-9845]
- Line 70: Duplicate range [9798-9845]
- Line 85: Duplicate range [9846-9896]
- Line 88: Duplicate range [9846-9896]
- Line 91: Duplicate range [9846-9896]
- Line 106: Duplicate range [9897-9932]
- Line 109: Duplicate range [9897-9932]
- Line 112: Duplicate range [9897-9932]
- Line 127: Duplicate range [9933-9972]
- Line 130: Duplicate range [9933-9972]
- Line 133: Duplicate range [9933-9972]
- Line 148: Duplicate range [9973-10010]
- Line 151: Duplicate range [9973-10010]
- Line 154: Duplicate range [9973-10010]
- Line 169: Duplicate range [10011-10131]
- Line 172: Duplicate range [10011-10131]
- Line 175: Duplicate range [10011-10131]
- Line 190: Duplicate range [10132-10172]
- Line 193: Duplicate range [10132-10172]
- Line 196: Duplicate range [10132-10172]
- Line 211: Duplicate range [10173-10210]
- Line 214: Duplicate range [10173-10210]
- Line 217: Duplicate range [10173-10210]

---

### File: dynamic/scholar/02-22-01-01.txt

**Errors:**
- Line 7: Duplicate range [10211-10256]
- Line 10: Duplicate range [10211-10256]
- Line 13: Duplicate range [10211-10256]
- Line 28: Duplicate range [10257-10322]
- Line 31: Duplicate range [10257-10322]
- Line 34: Duplicate range [10257-10322]
- Line 49: Duplicate range [10323-10384]
- Line 52: Duplicate range [10323-10384]
- Line 55: Duplicate range [10323-10384]
- Line 70: Duplicate range [10385-10427]
- Line 73: Duplicate range [10385-10427]
- Line 76: Duplicate range [10385-10427]
- Line 91: Duplicate range [10428-10468]
- Line 94: Duplicate range [10428-10468]
- Line 97: Duplicate range [10428-10468]
- Line 112: Duplicate range [10469-10516]
- Line 115: Duplicate range [10469-10516]
- Line 118: Duplicate range [10469-10516]
- Line 133: Duplicate range [10517-10550]
- Line 136: Duplicate range [10517-10550]
- Line 139: Duplicate range [10517-10550]
- Line 154: Duplicate range [10551-10574]
- Line 157: Duplicate range [10551-10574]
- Line 160: Duplicate range [10551-10574]
- Line 175: Duplicate range [10575-10606]
- Line 178: Duplicate range [10575-10606]
- Line 181: Duplicate range [10575-10606]
- Line 196: Duplicate range [10607-10661]
- Line 199: Duplicate range [10607-10661]
- Line 202: Duplicate range [10607-10661]
- Line 217: Duplicate range [10662-10709]
- Line 220: Duplicate range [10662-10709]
- Line 223: Duplicate range [10662-10709]
- Line 238: Duplicate range [10710-10760]
- Line 241: Duplicate range [10710-10760]
- Line 244: Duplicate range [10710-10760]
- Line 256: Duplicate range [10761-10765]
- Line 259: Duplicate range [10761-10765]
- Line 262: Duplicate range [10761-10765]
- Line 265: Duplicate range [10761-10765]

---

### File: dynamic/scholar/02-22-02-01.txt

**Errors:**
- Line 7: Duplicate range [10766-10777]
- Line 10: Duplicate range [10766-10777]
- Line 13: Duplicate range [10766-10777]
- Line 25: Duplicate range [10810-10824]
- Line 28: Duplicate range [10810-10824]
- Line 31: Duplicate range [10810-10824]
- Line 34: Duplicate range [10810-10824]
- Line 37: Duplicate range [10810-10824]

---

### File: dynamic/scholar/02-22-03-03.txt

**Errors:**
- Line 49: Duplicate range [11233-11235]
- Line 166: Duplicate range [11298-11310]

---

### File: dynamic/scholar/02-22-04-01.txt

**Errors:**
- Line 126: Duplicate range [11417-11419]
- Line 134: Duplicate range [11420-11421]
- Line 142: Duplicate range [11422-11425]
- Line 150: Duplicate range [11424-11425]

---

### File: dynamic/scholar/02-22-05-01.txt

**Errors:**
- Line 157: Duplicate range [11571-11574]
- Line 199: Duplicate range [11627-11637]
- Line 205: Duplicate range [11638-11655]
- Line 211: Duplicate range [11656-11660]
- Line 219: Duplicate range [11661-11673]
- Line 222: Duplicate range [11661-11673]
- Line 228: Duplicate range [11674-11685]
- Line 245: Duplicate range [11716-11725]
- Line 251: Duplicate range [11724-11735]
- Line 254: Duplicate range [11724-11735]

---

### File: dynamic/scholar/02-22-05-02.txt

**Errors:**
- Line 4: Duplicate range [11736-11744]
- Line 10: Duplicate range [11736-11760]
- Line 18: Duplicate range [11761-11784]
- Line 21: Duplicate range [11761-11784]
- Line 30: Duplicate range [11785-11802]
- Line 33: Duplicate range [11785-11802]
- Line 44: Duplicate range [11803-11823]
- Line 53: Duplicate range [11824-11824]
- Line 56: Duplicate range [11824-11824]
- Line 59: Duplicate range [11824-11824]

---

### File: dynamic/scholar/02-22-06-01.txt

**Errors:**
- Line 4: Duplicate range [11825-11845]
- Line 7: Duplicate range [11825-11845]
- Line 10: Duplicate range [11825-11845]
- Line 18: Duplicate range [11846-11858]
- Line 21: Duplicate range [11846-11858]
- Line 27: Duplicate range [11859-11871]
- Line 30: Duplicate range [11859-11871]
- Line 36: Duplicate range [11872-11890]
- Line 39: Duplicate range [11872-11890]
- Line 47: Duplicate range [11891-11906]
- Line 50: Duplicate range [11891-11906]
- Line 56: Duplicate range [11907-11920]
- Line 59: Duplicate range [11907-11920]
- Line 62: Duplicate range [11907-11920]
- Line 70: Duplicate range [11921-11956]
- Line 85: Duplicate range [11921-11956]
- Line 102: Duplicate range [11977-11990]
- Line 105: Duplicate range [11977-11990]
- Line 108: Duplicate range [11977-11990]
- Line 114: Duplicate range [11991-12002]
- Line 117: Duplicate range [11991-12002]
- Line 120: Duplicate range [11991-12002]

---

### File: dynamic/scholar/02-22-07-01.txt

**Errors:**
- Line 12: Duplicate range [12003-12010]
- Line 28: Duplicate range [12003-12010]

---

### File: dynamic/scholar/02-23-01-01.txt

**Errors:**
- Line 4: Duplicate range [12011-12021]
- Line 7: Duplicate range [12011-12021]
- Line 10: Duplicate range [12011-12021]
- Line 16: Duplicate range [12022-12043]
- Line 19: Duplicate range [12022-12043]
- Line 22: Duplicate range [12022-12043]
- Line 30: Duplicate range [12044-12062]
- Line 33: Duplicate range [12044-12062]
- Line 36: Duplicate range [12044-12062]
- Line 42: Duplicate range [12063-12081]
- Line 45: Duplicate range [12063-12081]
- Line 48: Duplicate range [12063-12081]
- Line 56: Duplicate range [12082-12119]
- Line 59: Duplicate range [12082-12119]
- Line 62: Duplicate range [12082-12119]
- Line 68: Duplicate range [12120-12139]
- Line 71: Duplicate range [12120-12139]
- Line 74: Duplicate range [12120-12139]
- Line 82: Duplicate range [12140-12167]
- Line 85: Duplicate range [12140-12167]
- Line 88: Duplicate range [12140-12167]
- Line 94: Duplicate range [12168-12204]
- Line 97: Duplicate range [12168-12204]
- Line 100: Duplicate range [12168-12204]
- Line 108: Duplicate range [12205-12235]
- Line 111: Duplicate range [12205-12235]
- Line 114: Duplicate range [12205-12235]
- Line 120: Duplicate range [12236-12244]
- Line 123: Duplicate range [12236-12244]
- Line 126: Duplicate range [12236-12244]

---

### File: dynamic/scholar/02-23-02-01.txt

**Errors:**
- Line 4: Duplicate range [12245-12250]
- Line 7: Duplicate range [12245-12250]
- Line 10: Duplicate range [12245-12250]
- Line 18: Duplicate range [12251-12270]
- Line 21: Duplicate range [12251-12270]
- Line 24: Duplicate range [12251-12270]
- Line 30: Duplicate range [12278-12283]
- Line 33: Duplicate range [12278-12283]
- Line 36: Duplicate range [12278-12283]
- Line 44: Duplicate range [12284-12308]
- Line 47: Duplicate range [12284-12308]
- Line 50: Duplicate range [12284-12308]
- Line 56: Duplicate range [12284-12305]
- Line 59: Duplicate range [12284-12305]
- Line 62: Duplicate range [12284-12305]
- Line 68: Duplicate range [12306-12320]
- Line 71: Duplicate range [12306-12320]
- Line 74: Duplicate range [12306-12320]
- Line 82: Duplicate range [12309-12338]
- Line 85: Duplicate range [12309-12338]
- Line 88: Duplicate range [12309-12338]
- Line 96: Duplicate range [12321-12350]
- Line 99: Duplicate range [12321-12350]
- Line 102: Duplicate range [12321-12350]
- Line 108: Duplicate range [12339-12350]
- Line 111: Duplicate range [12339-12350]
- Line 114: Duplicate range [12339-12350]

---

### File: dynamic/scholar/02-23-02-02.txt

**Errors:**
- Line 4: Duplicate range [12351-12368]
- Line 7: Duplicate range [12351-12368]
- Line 10: Duplicate range [12351-12368]
- Line 16: Duplicate range [12351-12384]
- Line 19: Duplicate range [12351-12384]
- Line 22: Duplicate range [12351-12384]
- Line 30: Duplicate range [12369-12400]
- Line 33: Duplicate range [12369-12400]
- Line 36: Duplicate range [12369-12400]
- Line 44: Duplicate range [12385-12413]
- Line 47: Duplicate range [12385-12413]
- Line 50: Duplicate range [12385-12413]
- Line 56: Duplicate range [12414-12433]
- Line 59: Duplicate range [12414-12433]
- Line 62: Duplicate range [12414-12433]
- Line 70: Duplicate range [12434-12493]
- Line 73: Duplicate range [12434-12493]
- Line 76: Duplicate range [12434-12493]
- Line 82: Duplicate range [12494-12519]
- Line 85: Duplicate range [12494-12519]
- Line 88: Duplicate range [12494-12519]
- Line 96: Duplicate range [12520-12521]
- Line 99: Duplicate range [12520-12521]
- Line 102: Duplicate range [12520-12521]

---

### File: dynamic/scholar/02-23-03-01.txt

**Errors:**
- Line 4: Duplicate range [12522-12559]
- Line 7: Duplicate range [12522-12559]
- Line 10: Duplicate range [12522-12559]
- Line 16: Duplicate range [12560-12604]
- Line 19: Duplicate range [12560-12604]
- Line 22: Duplicate range [12560-12604]
- Line 30: Duplicate range [12605-12663]
- Line 33: Duplicate range [12605-12663]
- Line 36: Duplicate range [12605-12663]
- Line 42: Duplicate range [12664-12702]
- Line 45: Duplicate range [12664-12702]
- Line 48: Duplicate range [12664-12702]
- Line 56: Duplicate range [12689-12720]
- Line 59: Duplicate range [12689-12720]
- Line 62: Duplicate range [12689-12720]
- Line 70: Duplicate range [12703-12710]
- Line 73: Duplicate range [12703-12710]
- Line 76: Duplicate range [12703-12710]
- Line 82: Duplicate range [12711-12741]
- Line 85: Duplicate range [12711-12741]
- Line 88: Duplicate range [12711-12741]
- Line 96: Duplicate range [12742-12771]
- Line 99: Duplicate range [12742-12771]
- Line 102: Duplicate range [12742-12771]
- Line 110: Duplicate range [12772-12778]
- Line 113: Duplicate range [12772-12778]
- Line 116: Duplicate range [12772-12778]

---

### File: dynamic/scholar/02-23-03-02.txt

**Errors:**
- Line 4: Duplicate range [12779-12811]
- Line 7: Duplicate range [12779-12811]
- Line 10: Duplicate range [12779-12811]
- Line 18: Duplicate range [12812-12847]
- Line 21: Duplicate range [12812-12847]
- Line 24: Duplicate range [12812-12847]
- Line 32: Duplicate range [12848-12889]
- Line 35: Duplicate range [12848-12889]
- Line 38: Duplicate range [12848-12889]
- Line 46: Duplicate range [12890-12923]
- Line 49: Duplicate range [12890-12923]
- Line 52: Duplicate range [12890-12923]
- Line 60: Duplicate range [12924-12969]
- Line 63: Duplicate range [12924-12969]
- Line 66: Duplicate range [12924-12969]

---

### File: dynamic/scholar/02-23-04-01.txt

**Errors:**
- Line 73: Duplicate range [13304-13694]
- Line 186: Duplicate range [13304-13694]
- Line 293: Duplicate range [13304-13694]

---

### File: dynamic/scholar/02-23-05-01.txt

**Errors:**
- Line 13: Duplicate range [13695-13700]
- Line 43: Duplicate range [13695-13700]
- Line 56: Duplicate range [13695-13700]

---

### File: dynamic/scholar/02-23-06-01.txt

**Errors:**
- Line 373: Non-sequential range [13701-13735] - Start (13701) < Previous start (13975)
- Line 12: Duplicate range [13701-13705]
- Line 28: Duplicate range [13701-13705]
- Line 42: Duplicate range [13701-13705]
- Line 102: Duplicate range [13735-13850]
- Line 123: Duplicate range [13735-13850]
- Line 163: Duplicate range [13850-13908]
- Line 185: Duplicate range [13850-13908]
- Line 199: Duplicate range [13850-13908]
- Line 256: Duplicate range [13909-14019]
- Line 273: Duplicate range [13909-14019]
- Line 303: Duplicate range [13975-14060]
- Line 328: Duplicate range [13975-14060]
- Line 387: Duplicate range [13701-13735]
- Line 400: Duplicate range [13701-13735]
- Line 418: Duplicate range [13701-13735]
- Line 491: Duplicate range [13736-13800]
- Line 504: Duplicate range [13736-13800]
- Line 526: Duplicate range [13736-13800]
- Line 633: Duplicate range [13801-14000]
- Line 643: Duplicate range [13801-14000]
- Line 661: Duplicate range [13801-14000]

---

### File: dynamic/scholar/02-23-06-02.txt

**Errors:**
- Line 7: Duplicate range [14200-14206]
- Line 10: Duplicate range [14200-14206]
- Line 16: Duplicate range [14207-14225]
- Line 19: Duplicate range [14207-14225]
- Line 22: Duplicate range [14207-14225]
- Line 25: Duplicate range [14207-14225]
- Line 31: Duplicate range [14226-14241]
- Line 34: Duplicate range [14226-14241]
- Line 37: Duplicate range [14226-14241]
- Line 40: Duplicate range [14226-14241]
- Line 46: Duplicate range [14242-14277]
- Line 49: Duplicate range [14242-14277]
- Line 52: Duplicate range [14242-14277]
- Line 55: Duplicate range [14242-14277]

---

### File: dynamic/scholar/02-23-07-01.txt

**Errors:**
- Line 89: Duplicate range [14278-14587]
- Line 197: Duplicate range [14278-14587]
- Line 301: Duplicate range [14278-14587]

---

### File: dynamic/scholar/02-23-08-03.txt

**Errors:**
- Line 4: Duplicate range [14590-14615]
- Line 7: Duplicate range [14590-14615]
- Line 10: Duplicate range [14590-14615]
- Line 13: Duplicate range [14590-14615]
- Line 19: Duplicate range [14616-14639]
- Line 22: Duplicate range [14616-14639]
- Line 25: Duplicate range [14616-14639]
- Line 28: Duplicate range [14616-14639]
- Line 31: Duplicate range [14616-14639]
- Line 34: Duplicate range [14616-14639]
- Line 37: Duplicate range [14616-14639]
- Line 40: Duplicate range [14616-14639]

---

### File: dynamic/scholar/02-23-08-05.txt

**Errors:**
- Line 116: Duplicate range [14738-14749]

---

### File: dynamic/scholar/02-23-08-09.txt

**Errors:**
- Line 94: Duplicate range [14753-14822]
- Line 222: Duplicate range [14753-14822]
- Line 293: Duplicate range [14753-14822]

---

### File: dynamic/scholar/02-23-09-01.txt

**Errors:**
- Line 37: Duplicate range [14823-14876]
- Line 179: Duplicate range [14823-15274]

---

### File: dynamic/scholar/02-24-01-01.txt

**Errors:**
- Line 124: Duplicate range [15275-15634]
- Line 304: Duplicate range [15275-15634]
- Line 458: Duplicate range [15275-15634]

---

### File: dynamic/scholar/02-25-01-01.txt

**Errors:**
- Line 131: Duplicate range [15635-16298]
- Line 299: Duplicate range [15635-16298]
- Line 433: Duplicate range [15635-16298]

---

### File: dynamic/scholar/02-25-02-01.txt

**Errors:**
- Line 16: Duplicate range [16329-16351]
- Line 31: Duplicate range [16329-16351]
- Line 40: Duplicate range [16329-16351]
- Line 61: Duplicate range [16352-16359]
- Line 71: Duplicate range [16352-16359]
- Line 80: Duplicate range [16352-16359]

---

### File: dynamic/scholar/02-25-03-01.txt

**Errors:**
- Line 103: Duplicate range [16360-16408]
- Line 224: Duplicate range [16360-16408]
- Line 308: Duplicate range [16360-16408]

---

### File: dynamic/scholar/02-25-04-01.txt

**Errors:**
- Line 18: Duplicate range [16409-16424]
- Line 36: Duplicate range [16409-16424]
- Line 45: Duplicate range [16409-16424]
- Line 75: Duplicate range [16425-16435]
- Line 85: Duplicate range [16425-16435]
- Line 95: Duplicate range [16425-16435]

---

### File: dynamic/scholar/02-25-05-01.txt

**Errors:**
- Line 4: Duplicate range [16436-16533]
- Line 7: Duplicate range [16436-16533]
- Line 10: Duplicate range [16436-16533]
- Line 16: Duplicate range [16533-16650]
- Line 19: Duplicate range [16533-16650]
- Line 22: Duplicate range [16533-16650]
- Line 28: Duplicate range [16650-16718]
- Line 31: Duplicate range [16650-16718]
- Line 34: Duplicate range [16650-16718]

---

### File: dynamic/scholar/02-25-06-01.txt

**Errors:**
- Line 7: Duplicate range [16719-16728]
- Line 10: Duplicate range [16719-16728]
- Line 13: Duplicate range [16719-16728]
- Line 19: Duplicate range [16729-16756]
- Line 22: Duplicate range [16729-16756]
- Line 25: Duplicate range [16729-16756]
- Line 28: Duplicate range [16729-16756]
- Line 34: Duplicate range [16757-16769]
- Line 37: Duplicate range [16757-16769]
- Line 40: Duplicate range [16757-16769]
- Line 43: Duplicate range [16757-16769]

---

### File: dynamic/scholar/02-25-06-02.txt

**Errors:**
- Line 91: Duplicate range [16770-16971]
- Line 216: Duplicate range [16770-16971]
- Line 340: Duplicate range [16770-16971]

---

### File: dynamic/scholar/02-25-07-01.txt

**Errors:**
- Line 90: Duplicate range [16972-17310]
- Line 223: Duplicate range [16972-17310]
- Line 382: Duplicate range [16972-17310]

---

### File: frozen/epistemic/01-03-02-01.txt

**Errors:**
- Line 21: Non-sequential range [1671-1671] - Start (1671) < Previous start (1725)
- Line 26: Duplicate range [1671-1671]
- Line 31: Duplicate range [1671-1671]
- Line 36: Duplicate range [1671-1671]
- Line 41: Duplicate range [1671-1671]
- Line 46: Duplicate range [1671-1671]
- Line 51: Duplicate range [1671-1671]
- Line 56: Duplicate range [1671-1671]
- Line 61: Duplicate range [1671-1671]

---

### File: frozen/epistemic/01-03-03-01.txt

**Errors:**
- Line 37: Non-sequential range [1732-1732] - Start (1732) < Previous start (1896)
- Line 43: Duplicate range [1732-1732]
- Line 48: Duplicate range [1732-1732]
- Line 53: Duplicate range [1732-1732]

---

### File: frozen/epistemic/01-04-03-01.txt

**Errors:**
- Line 11: Duplicate range [2833-2833]
- Line 16: Duplicate range [2833-2833]
- Line 21: Duplicate range [2833-2833]

---

### File: frozen/epistemic/01-04-05-01.txt

**Errors:**
- Line 14: Duplicate range [2849-2849]

---

### File: frozen/epistemic/01-04-06-01.txt

**Errors:**
- Line 28: Non-sequential range [2873-2873] - Start (2873) < Previous start (2952)
- Line 34: Duplicate range [2873-2873]
- Line 39: Duplicate range [2873-2873]
- Line 44: Duplicate range [2873-2873]
- Line 50: Duplicate range [2873-2873]
- Line 55: Duplicate range [2873-2873]
- Line 60: Duplicate range [2873-2873]
- Line 65: Duplicate range [2873-2873]
- Line 70: Duplicate range [2873-2873]

---

### File: frozen/epistemic/01-04-08-01.txt

**Errors:**
- Line 12: Non-sequential range [2989-2989] - Start (2989) < Previous start (3000)
- Line 17: Duplicate range [2989-2989]
- Line 22: Duplicate range [2989-2989]
- Line 27: Duplicate range [2989-2989]
- Line 32: Duplicate range [2989-2989]
- Line 38: Duplicate range [2989-2989]
- Line 43: Duplicate range [2989-2989]

---

### File: frozen/epistemic/01-04-09-01.txt

**Errors:**
- Line 12: Non-sequential range [3017-3017] - Start (3017) < Previous start (3024)
- Line 17: Duplicate range [3017-3017]
- Line 22: Duplicate range [3017-3017]
- Line 27: Duplicate range [3017-3017]

---

### File: frozen/epistemic/01-04-11-01.txt

**Errors:**
- Line 11: Non-sequential range [3040-3040] - Start (3040) < Previous start (3048)
- Line 16: Duplicate range [3040-3040]
- Line 21: Duplicate range [3040-3040]
- Line 26: Duplicate range [3040-3040]
- Line 31: Duplicate range [3040-3040]
- Line 36: Duplicate range [3040-3040]

---

### File: frozen/epistemic/01-04-12-01.txt

**Errors:**
- Line 46: Non-sequential range [3062-3062] - Start (3062) < Previous start (3301)
- Line 51: Duplicate range [3062-3062]
- Line 56: Duplicate range [3062-3062]

---

### File: frozen/epistemic/01-04-18-01.txt

**Errors:**
- Line 11: Duplicate range [3888-3888]

---

### File: frozen/epistemic/01-06-07-01.txt

**Errors:**
- Line 11: Non-sequential range [8687-8687] - Start (8687) < Previous start (8691)
- Line 16: Duplicate range [8687-8687]

---

### File: frozen/epistemic/01-06-07-03.txt

**Errors:**
- Line 11: Non-sequential range [8725-8725] - Start (8725) < Previous start (8751)
- Line 16: Duplicate range [8725-8725]

---

### File: frozen/epistemic/01-06-09-01.txt

**Errors:**
- Line 11: Non-sequential range [8810-8810] - Start (8810) < Previous start (8811)
- Line 11: Duplicate range [8810-8810]
- Line 16: Duplicate range [8810-8810]

---

### File: frozen/epistemic/01-06-10-01.txt

**Errors:**
- Line 11: Non-sequential range [8841-8841] - Start (8841) < Previous start (8871)
- Line 16: Duplicate range [8841-8841]

---

### File: frozen/epistemic/01-07-02-01.txt

**Errors:**
- Line 11: Non-sequential range [9899-9899] - Start (9899) < Previous start (9951)
- Line 16: Duplicate range [9899-9899]

---

### File: frozen/epistemic/01-07-03-01.txt

**Errors:**
- Line 16: Non-sequential range [9990-9990] - Start (9990) < Previous start (10071)

---

### File: frozen/epistemic/01-08-01-01.txt

**Errors:**
- Line 11: Non-sequential range [10472-10472] - Start (10472) < Previous start (10492)
- Line 16: Duplicate range [10472-10472]

---

### File: frozen/epistemic/01-08-03-01.txt

**Errors:**
- Line 11: Non-sequential range [10699-10699] - Start (10699) < Previous start (10716)

---

### File: frozen/epistemic/01-08-04-02.txt

**Errors:**
- Line 11: Non-sequential range [10724-10724] - Start (10724) < Previous start (10731)
- Line 16: Duplicate range [10724-10724]

---

### File: frozen/epistemic/01-14-11-01.txt

**Errors:**
- Line 11: Non-sequential range [20147-20147] - Start (20147) < Previous start (20182)
- Line 16: Duplicate range [20147-20147]

---

### File: frozen/epistemic/01-14-12-01.txt

**Errors:**
- Line 11: Non-sequential range [20212-20212] - Start (20212) < Previous start (20228)
- Line 16: Duplicate range [20212-20212]

---

### File: frozen/epistemic/02-18-11-01.txt

**Errors:**
- Line 37: Duplicate range [5170-5185]

---

### File: frozen/epistemic/02-18-13-01.txt

**Errors:**
- Line 19: Duplicate range [5278-5290]

---

### File: frozen/epistemic/02-18-15-01.txt

**Errors:**
- Line 25: Duplicate range [5654-5910]

---

### File: frozen/epistemic/02-20-02-01.txt

**Errors:**
- Line 7: Duplicate range [8831-8847]
- Line 13: Duplicate range [8831-8847]

---

### File: frozen/epistemic/02-20-04-01.txt

**Errors:**
- Line 7: Duplicate range [8972-8999]
- Line 13: Duplicate range [8972-8999]

---

### File: frozen/epistemic/02-20-05-01.txt

**Errors:**
- Line 7: Duplicate range [9027-9037]
- Line 13: Duplicate range [9027-9037]

---

### File: frozen/epistemic/02-20-06-01.txt

**Errors:**
- Line 7: Duplicate range [9069-9075]
- Line 13: Duplicate range [9069-9075]

---

### File: frozen/epistemic/02-20-07-01.txt

**Errors:**
- Line 7: Duplicate range [9079-9113]
- Line 13: Duplicate range [9079-9113]

---

### File: frozen/epistemic/02-20-08-01.txt

**Errors:**
- Line 7: Duplicate range [9223-9227]
- Line 13: Duplicate range [9223-9227]

---

### File: frozen/epistemic/02-21-00-01.txt

**Errors:**
- Line 7: Duplicate range [9413-9417]
- Line 13: Duplicate range [9413-9417]
- Line 25: Duplicate range [9418-9455]

---

### File: frozen/epistemic/02-21-01-01.txt

**Errors:**
- Line 7: Duplicate range [9713-9721]
- Line 13: Duplicate range [9713-9721]
- Line 25: Duplicate range [9722-9759]

---

### File: frozen/epistemic/02-22-02-01.txt

**Errors:**
- Line 7: Duplicate range [10766-10785]

---

### File: frozen/epistemic/02-22-03-01.txt

**Errors:**
- Line 7: Duplicate range [10826-10861]

---

### File: frozen/epistemic/02-22-03-02.txt

**Errors:**
- Line 7: Duplicate range [10900-10937]

---

### File: frozen/epistemic/02-22-03-03.txt

**Errors:**
- Line 7: Duplicate range [11182-11203]

---

### File: frozen/epistemic/02-22-04-01.txt

**Errors:**
- Line 7: Duplicate range [11322-11355]

---

### File: frozen/epistemic/02-22-05-01.txt

**Errors:**
- Line 7: Duplicate range [11480-11507]

---

### File: frozen/epistemic/02-22-05-02.txt

**Errors:**
- Line 7: Duplicate range [11736-11773]

---

### File: frozen/epistemic/02-22-06-01.txt

**Errors:**
- Line 7: Duplicate range [11825-11849]

---

## Recommended Fixes

### For Non-Sequential Ranges
- Review commentary sections that may intentionally overlap
- Verify that backward references are properly marked
- Consider adding explicit commentary markers for non-sequential ranges

### For Invalid Boundary Errors (End < Start)
- Check for typos in range specifications
- Verify line numbering in source documents
- Ensure proper extraction from original texts

### For Format Errors
- Ensure all ranges use [digits-digits] format
- Remove extra spaces within brackets
- Check for malformed brackets

### For Duplicate Ranges
- Remove redundant range entries
- Consolidate overlapping ranges if appropriate
- Verify intentional duplicates are documented

---

## Validation Methodology

1. All files in /home/opencode/MDZOD/1/text/ were scanned
2. Files containing the pattern [digits-digits] were analyzed
3. Each range was checked for:
   - Proper numeric format
   - Sequential ordering of start values
   - Valid boundaries (end >= start)
   - Duplicate ranges
4. Errors were categorized and reported

## Error Type Breakdown

| Error Type | Count |
|------------|-------|
| Duplicate Range | 10246 |
| Non-Sequential Range | 1140 |
| Invalid Boundary (End < Start) | 64 |
