import multi_file.container as m_con
import single_file.single_file_share_structure as s_con


# multi file container
print("#" * 5 , "Multi file","#" * 5)
m_container = m_con.Container()
m_container.mod1.print_string()
m_container.mod1.root.mod2.print_string()

# single file container
print("#" * 5 , "Single file","#" * 5)
s_container = s_con.Container()
m_container.mod1.print_string()
m_container.mod1.root.mod2.print_string()