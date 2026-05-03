## Equivalence Partitioning - Student Module

| Category | Class | Description | Example |
|----------|------|-------------|---------|
| Grade | G1 | 1 ≤ grade ≤ 10 (valid) | 7 |
| Grade | G2 | grade < 1 (invalid) | -3 |
| Grade | G3 | grade > 10 (invalid) | 15 |
| List size | L1 | 0–6 grades | [5,6,7] |
| List size | L2 | 7 grades (limit) | 7 values |
| List size | L3 | >7 grades | 8+ values |
| Average | A1 | empty list | [] |
| Average | A2 | non-empty list | [5,6,7] |
| Letter Grade | LG1 | avg ≥ 9 | A |
| Letter Grade | LG2 | 8 ≤ avg < 9 | B |
| Letter Grade | LG3 | 7 ≤ avg < 8 | C |
| Letter Grade | LG4 | 5 ≤ avg < 7 | D |
| Letter Grade | LG5 | avg < 5 | F |
| Passing | P1 | avg ≥ 5 | True |
| Passing | P2 | avg < 5 | False |

---

## Equivalence Partitioning - Test Cases

| Test ID | Input | Expected Output |
|----------|------|----------------|
| EP1 | add_grade(7) | accepted |
| EP2 | add_grade(-1) | ValueError |
| EP3 | add_grade(11) | ValueError |
| EP4 | [] | average = 0 |
| EP5 | [5,6,7] | average = 6 |
| EP6 | [9,9,9] | A |
| EP7 | [8,8,8] | B |
| EP8 | [7,7,7] | C |
| EP9 | [5,5,5] | D |
| EP10 | [4,4,4] | F |
| EP11 | avg ≥ 5 | is_passing = True |
| EP12 | avg < 5 | is_passing = False |

---

## Boundary Value Analysis - Student Module

| Feature | Boundary | Values | Expected |
|----------|---------|--------|----------|
| Grade | lower invalid | 0 | Error |
| Grade | lower valid | 1 | OK |
| Grade | upper valid | 10 | OK |
| Grade | upper invalid | 11 | Error |
| List size | near max | 6 | OK |
| List size | max | 7 | OK |
| List size | overflow | 8 | Error |
| Letter grade | A threshold | 9 | A |
| Letter grade | B threshold | 8 | B |
| Letter grade | C threshold | 7 | C |
| Letter grade | D threshold | 5 | D |
| Letter grade | F threshold | 4.99 | F |
| Passing | boundary false | 4.99 | False |
| Passing | boundary true | 5 | True |

---

## Boundary Value Analysis - Test Cases

| Test ID | Input | Expected |
|----------|------|----------|
| BV1 | add_grade(0) | ValueError |
| BV2 | add_grade(1) | OK |
| BV3 | add_grade(10) | OK |
| BV4 | add_grade(11) | ValueError |
| BV5 | 7 grades | OK |
| BV6 | 8th grade | ValueError |
| BV7 | [4.97, 5, 5] | F |
| BV8 | [5, 5, 5] | D |
| BV9 | [6.97, 7, 7] | D |
| BV10 | [7, 7, 7] | C |
| BV11 | [7.97, 8, 8] | C |
| BV12 | [8, 8, 8] | B |
| BV13 | [8.97, 9, 9] | B |
| BV14 | [9, 9, 9] | A |
| BV15 | [4.97, 5, 5] | is_passing = False |
| BV16 | [5, 5, 5] | is_passing = True |

---

## Category Partitioning - Filter Functionality

| Category | Class | Description | Condition |
|----------|------|-------------|----------|
| Interval | I1 | valid interval | min ≤ max |
| Interval | I2 | invalid interval | min > max |
| Average Position | AP1 | below interval | avg < min |
| Average Position | AP2 | inside interval | min ≤ avg ≤ max |
| Average Position | AP3 | above interval | avg > max |
| Average Position | AP4 | lower boundary | avg = min |
| Average Position | AP5 | upper boundary | avg = max |
| Students | S1 | empty list | no students |
| Students | S2 | one student | single case |
| Students | S3 | multiple students | mixed values |

---

## Category Partitioning - Test Cases

| Test ID | Categories Covered | Input | Expected Output |
|----------|------------------|------|----------------|
| CP1 | I1 + AP2 + S2 | [6,6], range(5,7) | student included |
| CP2 | I1 + AP1 + S2 | [4,4], range(5,7) | empty result |
| CP3 | I1 + AP3 + S2 | [9,9], range(5,7) | empty result |
| CP4 | I1 + AP4 + S2 | [5,5], range(5,7) | included |
| CP5 | I1 + AP5 + S2 | [7,7], range(5,7) | included |
| CP6 | I2 | range(7,5) | ValueError |
| CP7 | I1 + S3 + AP1/AP2/AP3/AP4/AP5 | mixed students | only valid returned |
| CP8 | I1 + S1 | empty list | empty result |

---

## Independent Circuits - Report Functionality

Nodes:

1. Start  
2. if students list empty  
3. return "NO_DATA"  
4. loop over students  
5. compute average  
6. if passing student  
7. increment passing  
8. if top student  
9. update top student  
10. compute global average  
11. if avg >= 8 (HIGH)  
12. else if avg >= 5 (MEDIUM)  
13. else (LOW)  
14. return report  

CFG (text form):


1 → 2 → (3 or 4)
3 → END
4 → 5 → 6 → (7)
6 → (8)
8 → (9)
loop back to 4
4 → 10 → 11 → 12 → 13 → 14


---


Using formula:

V(G) = e − n + 2

Where:
- n = 14 nodes
- e = 16 edges

V(G) = 16 − 14 + 2 = 4

Number of independent circuits = 4

| Circuit ID | Path | Description |
|------------|------|-------------|
| C1 | 1 → 2 → 3 | Empty dataset → NO_DATA return |
| C2 | 1 → 2 → 4 → 10 → 14 | Single/multiple students, normal execution |
| C3 | loop with passing + non-passing students | triggers passing branch |
| C4 | top student update + HIGH performance path | max avg + classification |

---

## Independent Circuits - Test Cases

| Test ID | Circuit |
|----------|--------|
| test_C1_empty_data | C1 |
| test_C2_basic_execution | C2 |
| test_C3_passing_students | C3 |
| test_C4_performance_and_top | C4 |

---

## Statement Coverage Tests

Pentru testarea la nivel de instructiune primul pas este transformarea programului intr-un graf orientat (graful din stanga este graful pentru functia ui.menu, cel din dreapta este pentru functia ui.filter_students)

![graph](./docs/menu_graph2.png)
![graph](./docs/filter_graph.png)

Pentru a obtine un set de teste care acopera toate instructiunile din funcia ui.menu folosim graful orintat corespunzator pentru a identifica un set de date care in urma rulari atinge fiecare instructiune cel putin odata. In urma analizei grafului am obtinut setul urmator de teste:

| Input | Expected Output | Statements Covered |
|-------|----------------|--------------------|
| "0" | program exit | 1...8,55 |
| "1" | student list printed | 1...6,11,55 |
| "2" | format message | 1...6,11,13,14...16,55 |
| "3" | student list + prompt | 1...6,11,13,18,19...22,55 |
| "4" | format message | 1...6,11,13,18,24,25...28,55 |
| "5" | report generated | 1...6,11,13,18,24,30,31...3355 |
| "6 invalid input" | error message | 1...6,11,13,18,24,30,35,36...38,39,40...42,55 |
| "6 valid" | filtered students printed | 1...6,11,13,18,24,30,35,36...38,39,43,44,53...5455 |
| "6 empty result" | No students found | 1...6,11,13,18,24,30,35,36...38,39,43,44,54...46,47,48,55 |
| "6 invalid range" | error message | 1...6,11,13,18,24,30,35,36...38,39,43,44,54...46,47,50,51,55 |

Aceasi metoda este folosita si pentru functia ui.filter_students pentru a obtine acest set de date.

| Input | Expected Output | Statements Covered |
|-------|----------------|--------------------|
| 6 4 | value error | 1,2 |
| 4 6 | student list | 1,3-9 |


## Decision Coverage Tests

Pentru testare la nivel de decizie analizam programul si graful orientat al acestuia pentru a extrage instructiunile de decizie (if, for, while, try except) in ui.menu am gasit urmatoarele decizi

| Nr | Decisions |
|----|-----------|
| 1 | while not should_exit |
| 2 | if opcode == 0 |
| 3 | if opcode == 1 |
| 4 | if opcode == 2 |
| 5 | if opcode == 3 |
| 6 | if opcode == 4 |
| 7 | if opcode == 5 |
| 8 | if opcode == 6 |
| 9 | try map(float, in_string.split()) |
| 10 | try self.filter_students(min_avg, max_avg) |
| 11 | if not result |
| 12 | for s in result |

Setul de date de test urmaotare a fost ales astfel incat fiecare dintre cele 12 decizi sa fie cel putin odata adevarate si odata false

| Input | Output | Decisions |
|-------|--------|-----------|
| 0 | program exit | 1 True False, 2 True |
| 1 | student list printed | 1 True, 2 False, 3 True|
| 2 | format message | 1 True, 2-3 False, 4 True |
| 3 | student list + prompt | 1 True, 2-4 False, 5 True |
| 4 | format message | 1 True, 2-5 False, 6 True |
| 5 | report generated | 1 True, 2-6 False, 7 True |
| 6 "invalid input" | error message | 1 True False, 2-7 False, 8 True, 9 False |
| 6 "valid" | filtered students printed | 1 True, 2-7 False, 8 True, 9 True, 10 True, 11 False, 12 True False |
| 6 "empty result" | No students found | 1 True, 2-7 False, 8 True, 9 True 10 True, 11 True |
| 6 "invalid range" | error message | 1 True, 2-7 False, 8 True, 9 True, 10 False |
| 7 | input igonred wait for other operation | 1 True, 2-8 False |

Aceasi metoda a fost utilizata pentru functia ui.filter_students

| Nr | Decisions |
|----|-----------|
| 1 | if min_avg > max_avg: |
| 2 | for s in self.students: |
| 3 | if min_avg <= avg <= max_avg: |

| Input | Output | Decisions |
|-------|--------|-----------|
| 6 4 | value error | 1 True |
| 4 6 (student with average in range) | student list | 1 False, 2 True False, 3 True |
| 1 2 (student not in range) | student list | 1 False, 2 True False, 3 False |

## Condition Coverage Tests

Pentru testare la nivel de impartim deciziile identificate anterior in mai multe conditii (daca este posibil).

| Nr | Decisions | Conditions |
|----|-----------|------------|
| 1 | while not should_exit | not should_exit |
| 2 | if opcode == 0 | opcode == 0 |
| 3 | if opcode == 1 | opcode == 1 |
| 4 | if opcode == 2 | opcode == 2 |
| 5 | if opcode == 3 | opcode == 3 |
| 6 | if opcode == 4 | opcode == 4 |
| 7 | if opcode == 5 | opcode == 5 |
| 8 | if opcode == 6 | opcode == 6 |
| 9 | try map(float, in_string.split()) | map(float, in_string.split()) throws |
| 10 | try self.filter_students(min_avg, max_avg) | self.filter_students(min_avg, max_avg) throws |
| 11 | if not result | not result |
| 12 | for s in result | s in result |

Cum deciziile din functia ui.menu nu pot fi imparite in mai multe decizii setul de teste gasit este identic cu cel de la testare la nivel de decizie

| Input | Expected | Conditions |
|-------|----------|------------|
| 0 | program exit | 1 True False, 2 True |
| 1 | student list printed | 1 True, 2 False, 3 True|
| 2 | format message | 1 True, 2-3 False, 4 True |
| 3 | student list + prompt | 1 True, 2-4 False, 5 True |
| 4 | format message | 1 True, 2-5 False, 6 True |
| 5 | report generated | 1 True, 2-6 False, 7 True |
| 6 "invalid input" | error message | 1 True False, 2-7 False, 8 True, 9 False |
| 6 "valid" | filtered students printed | 1 True, 2-7 False, 8 True, 9 True, 10 True, 11 False, 12 True False |
| 6 "empty result" | No students found | 1 True, 2-7 False, 8 True, 9 True 10 True, 11 True |
| 6 "invalid range" | error message | 1 True, 2-7 False, 8 True, 9 True, 10 False |
| 7 | input igonred wait for other operation | 1 True, 2-8 False |

In funcita ui.filter_students are mai multe conditii in decizia 3 astfel setul de date de test gasite aici este diferit.

| Nr | Decisions | Conditions |
|----|-----------|------------|
| 1 | if min_avg > max_avg: | min_avg > max_avg |
| 2 | for s in self.students: | s in self.students |
| 3 | if min_avg <= avg <= max_avg: | min_avg <= avg |
| 4 | if min_avg <= avg <= max_avg: | avg <= max_avg |

| Input | Output | Decisions |
|-------|--------|-----------|
| 6 4 | value error | 1 True |
| 1 2 (student above range) | student list | 1 False, 2 True False, 3 True, 4 False |
| 9 10 (student bellow range) | student list | 1 False, 2 True False, 3 False, 4 True |


## Muatation testing
Testarea la nivel de mutatii pentru cele doua functii ui.menu si ui.filter_students a fost realizata cu unealta mutmut pentru a genera mutatii dupa utilizarea acestuia am agsit urmaotarele rezultate:
- pentru ui.menu singuri mutanti neeliminati sunt cei care modifica codul folosit pentru iesirea din program (astfel programul nu se mai opreste singur)
- pentru ui.filter_students singuri mutatii neelimintai sunt cei care modifica mesajul de la exceptia ValueError
