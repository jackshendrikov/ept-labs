bold_color = "\033[1m"
reset_color = "\x1B[0m"


def fix_eq(eq):
    return eq.replace("--", "").replace("-+", "-").replace("+-", "-")\
        .replace("- -", "+ ").replace("- +", "- ").replace("+ -", "- ")


print(f"\n{bold_color}{'p²y + a₁py + a₀y = b₂p²x + b₁px + b₀x = c₂p²z + c₁pz + c₀z'}{reset_color}")

a1, a0 = 1, 2
b2, b1, b0 = 4, -2, -6
c2, c1, c0 = 0, 7, 8

C1, C2 = 0, 6
D1, D2 = 2, 3
E1, E2 = 9, 1

print(f"\n{bold_color}{'————————————————Початкові умови————————————————'}{reset_color}\n",
      "\t\tb₂=", b2, "\tc₂=", c2, "\tC₂=", C2, "\tD₂=", D2, "\tE₂=", E2,
      "\na₁=", a1, "\tb₁=", b1, "\tc₁=", c1, "\tC₁=", C1, "\tD₁=", D1, "\tE₁=", E1,
      "\na₀=", a0, "\tb₀=", b0, "\tc₀=", c0, "\n\nФорма: НФЗ")
print(f"{bold_color}{'———————————————————————————————————————————————'}{reset_color}")

print(f"\t{bold_color}{'1 - Запис еквівалентної форми УВЗ'}{reset_color}")

print("y = y₁ + α₂x + β₂z",
      "\npy₁ = y₂ + α₁x + β₁z",
      "\npy₂ = -a₁y₂ - a₀y₁ + α₀x + β₀z\n")

system = "y = y₁ + α₂x + β₂z" + \
          "\npy₁ = y₂ + α₁x + β₁z" + \
          "\npy₂ = -" + str(a1) + "y₂ -" + str(a0) + "y₁ + α₀x + β₀z\n"

print(fix_eq(system))

print("Р-ня заміни:", "\n\ty₁ = y - α₂x - β₂z",
      "\n\ty₂ = py₁ - α₁x - β₁z = py - α₂px - β₂pz - α₁x - β₁z\n")

print("Зробимо підстановку:", f"\n{bold_color}{'p²y - α₂p²x - β₂p²z - α₁px - β₁pz = -a₁py + α₂a₁px + β₂a₁pz + α₁a₁x + β₁a₁z - a₀y + α₂a₀x + β₂a₀z + α₀x + β₀z'}{reset_color}")
print("\nПеренесемо все, що з `y` ліворуч:", f"\n{bold_color}{'p²y + a₁py + a₀y = α₂p²x + β₂p²z + α₁px + β₁pz  + α₂a₁px + β₂a₁pz + α₁a₁x + β₁a₁z + α₂a₀x + β₂a₀z + α₀x + β₀z'}{reset_color}")
print("\nЗгрупуємо:", f"\n{bold_color}{'p²y + a₁py + a₀y = (α₂)p²x + (β₂)p²z + (α₁ + α₂a₁)px + (β₁ + β₂a₁)pz  + (α₀ + α₁a₁ + α₂a₀)x + (β₀ + β₁a₁ + β₂a₀)z'}{reset_color}")


print(f"{bold_color}{'———————————————————————————————————————————————'}{reset_color}")
print(f"\t{bold_color}{'2 - С-ма лін. алгебраїнчих рівнянь для αᵢ, βᵢ (i=0,2)'}{reset_color}")
print("α₂ = b₂", "\t\t\t\t\tβ₂ = c₂",
      "\nα₁ + α₂a₁ = b₁", "\t\t\t\tβ₁ + β₂a₁ = c₁",
      "\nα₀ + α₁a₁ + α₂a₀ = b₀", "\t\tβ₀ + β₁a₁ + β₂a₀ = c₀")

alpha2 = b2
alpha1 = b1 - alpha2 * a1
alpha0 = b0 - alpha1 * a1 - alpha2 * a0

beta2 = c2
beta1 = c1 - beta2 * a1
beta0 = c0 - beta1 * a1 - beta2 * a0

print(f"{bold_color}{'———————————————————————————————————————————————'}{reset_color}")
print(f"\t{bold_color}{'3 - Розрахунок значень для αᵢ, βᵢ (i=0,2)'}{reset_color}")
print("α₂ = ", '{: d}'.format(alpha2), "\t\tβ₂ =", '{: d}'.format(beta2),
      "\nα₁ =", '{: d}'.format(alpha1), "\t\tβ₁ =", '{: d}'.format(beta1),
      "\nα₀ =", '{: d}'.format(alpha0), "\t\tβ₀ =", '{: d}'.format(beta0))

print(f"{bold_color}{'———————————————————————————————————————————————'}{reset_color}")
print(f"\t{bold_color}{'4 - Рівняння заміни для yᵢ (i=1,2)'}{reset_color}")
print("y₁ = y - α₂x - β₂z",
      "\ny₂ = py - α₂px - β₂pz - α₁x - β₁z")

system = "\ny₁ = y - " + str(alpha2) + "x - " + str(beta2) + "z" + \
         "\ny₂ = py - " + str(alpha2) + "px - " + str(beta2) + "pz - " + \
         str(alpha1) + "x - " + str(beta1) + "z"

print(fix_eq(system))

print(f"{bold_color}{'———————————————————————————————————————————————'}{reset_color}")
print(f"\t{bold_color}{'5 - Знаходження нових початкових умов y₁(0) та y₂(0)'}{reset_color}")
system = "y₁(0) = y(0) - " + str(alpha2) + "x(0) - " + str(beta2) + "z(0)" + \
         "\ny₂(0) = py(0) - " + str(alpha2) + "px(0) - " + str(beta2) + "pz(0) - " +\
         str(alpha1) + "x(0) - " + str(beta1) + "z(0)\n"

print(fix_eq(system))

print("y₁(0) = C₁ - α₂D₁ - β₂E₁",
      "\ny₂(0) = C₂ - α₂D₂ - β₂E₂ - α₁D₁ - β₁E₁\n")

print(' y(0) = C₁ =', '{: d}'.format(C1), '\t\t x(0) = D₁ =', '{: d}'.format(D1), '\t\t z(0) = E₁ =', '{: d}'.format(E1),
      '\npy(0) = C₂ =', '{: d}'.format(C2), '\t\tpx(0) = D₂ =', '{: d}'.format(D2), '\t\tpz(0) = E₂ =', '{: d}'.format(E2))

system = '\ny₁(0) = ' + str(C1) + ' - ' + str(alpha2) + '*' + str(D1) + ' - ' + str(beta2) + '*' + str(E1) +\
         '\ny₂(0) = ' + str(C2) + ' - ' + str(alpha2) + '*' + str(D2) + ' - ' + str(beta2) + '*' + str(E2) + ' - ' + \
         str(alpha1) + '*' + str(D1) + ' - ' + str(beta1) + '*' + str(E1)

print(fix_eq(system))

print('\ny₁(0) = ', C1 - alpha2*D1 - beta2*E1,
      '\ny₂(0) =', C2 - alpha2*D2 - beta2*E2 - alpha1*D1 - beta1*E1)
